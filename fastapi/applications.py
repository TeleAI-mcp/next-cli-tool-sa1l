from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

from fastapi import routing
from fastapi.types import ASGIApp, DecoratedCallable, IncEx


class FastAPI:
    def __init__(
        self,
        *,
        debug: bool = False,
        routes: Optional[List[routing.BaseRoute]] = None,
        title: str = "FastAPI",
        description: str = "",
        version: str = "0.1.0",
        openapi_url: Optional[str] = "/openapi.json",
        openapi_tags: Optional[List[Dict[str, Any]]] = None,
        servers: Optional[List[Dict[str, Union[str, Any]]]] = None,
        docs_url: Optional[str] = "/docs",
        redoc_url: Optional[str] = "/redoc",
        swagger_ui_oauth2_redirect_url: Optional[str] = "/docs/oauth2-redirect",
        swagger_ui_init_oauth: Optional[Dict[str, Any]] = None,
        middleware: Optional[Sequence[routing.Middleware]] = None,
        exception_handlers: Optional[Dict[Union[int, type[Exception]], routing.Callable]] = None,
        on_startup: Optional[Sequence[Callable[[], Any]]] = None,
        on_shutdown: Optional[Sequence[Callable[[], Any]]] = None,
        terms_of_service: Optional[str] = None,
        contact: Optional[Dict[str, Union[str, Any]]] = None,
        license_info: Optional[Dict[str, Union[str, Any]]] = None,
        openapi_prefix: str = "",
        root_path: str = "",
        root_path_in_servers: bool = True,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        callbacks: Optional[List[Dict[str, Any]]] = None,
        webhooks: Optional[routing.APIRouter] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        swagger_ui_parameters: Optional[Dict[str, Any]] = None,
        async: bool = True,
        docs_schema: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.debug = debug
        self.title = title
        self.description = description
        self.version = version
        self.openapi_url = openapi_url
        self.openapi_tags = openapi_tags
        self.servers = servers
        self.docs_url = docs_url
        self.redoc_url = redoc_url
        self.swagger_ui_oauth2_redirect_url = swagger_ui_oauth2_redirect_url
        self.swagger_ui_init_oauth = swagger_ui_init_oauth
        self.middleware = middleware
        self.exception_handlers = exception_handlers
        self.on_startup = on_startup
        self.on_shutdown = on_shutdown
        self.terms_of_service = terms_of_service
        self.contact = contact
        self.license_info = license_info
        self.openapi_prefix = openapi_prefix
        self.root_path = root_path
        self.root_path_in_servers = root_path_in_servers
        self.responses = responses
        self.callbacks = callbacks
        self.webhooks = webhooks
        self.deprecated = deprecated
        self.include_in_schema = include_in_schema
        self.swagger_ui_parameters = swagger_ui_parameters
        self.async = async
        self.docs_schema = docs_schema

        self.routes = routes or []
        self.router = routing.APIRouter()
        self.app = self.build_app()

    def build_app(self) -> ASGIApp:
        return self.router

    def add_route(
        self,
        path: str,
        route: routing.BaseRoute,
        *,
        include_in_schema: bool = True,
    ) -> None:
        self.router.routes.append(route)

    def add_middleware(
        self,
        middleware_class: type[routing.Middleware],
        **kwargs: Any,
    ) -> None:
        self.router.add_middleware(middleware_class, **kwargs)

    def include_router(
        self,
        router: routing.APIRouter,
        *,
        prefix: str = "",
        tags: Optional[List[str]] = None,
        dependencies: Optional[Sequence[routing.Depends]] = None,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        default_response_class: Optional[type[routing.Response]] = None,
        callbacks: Optional[List[Dict[str, Any]]] = None,
        generate_unique_id_function: Optional[Callable[[routing.APIRoute], str]] = None,
    ) -> None:
        self.router.include_router(
            router,
            prefix=prefix,
            tags=tags,
            dependencies=dependencies,
            responses=responses,
            deprecated=deprecated,
            include_in_schema=include_in_schema,
            default_response_class=default_response_class,
            callbacks=callbacks,
            generate_unique_id_function=generate_unique_id_function,
        )

    def get(
        self,
        path: str,
        *,
        response_model: Optional[type] = None,
        status_code: int = 200,
        tags: Optional[List[str]] = None,
        dependencies: Optional[Sequence[routing.Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[IncEx] = None,
        response_model_exclude: Optional[IncEx] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: Optional[type[routing.Response]] = None,
        name: Optional[str] = None,
        callbacks: Optional[List[Dict[str, Any]]] = None,
        openapi_extra: Optional[Dict[str, Any]] = None,
        generate_unique_id_function: Optional[Callable[[routing.APIRoute], str]] = None,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        return self.router.get(
            path,
            response_model=response_model,
            status_code=status_code,
            tags=tags,
            dependencies=dependencies,
            summary=summary,
            description=description,
            response_description=response_description,
            responses=responses,
            deprecated=deprecated,
            operation_id=operation_id,
            response_model_include=response_model_include,
            response_model_exclude=response_model_exclude,
            response_model_by_alias=response_model_by_alias,
            response_model_exclude_unset=response_model_exclude_unset,
            response_model_exclude_defaults=response_model_exclude_defaults,
            response_model_exclude_none=response_model_exclude_none,
            include_in_schema=include_in_schema,
            response_class=response_class,
            name=name,
            callbacks=callbacks,
            openapi_extra=openapi_extra,
            generate_unique_id_function=generate_unique_id_function,
        )

    def post(
        self,
        path: str,
        *,
        response_model: Optional[type] = None,
        status_code: int = 200,
        tags: Optional[List[str]] = None,
        dependencies: Optional[Sequence[routing.Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[IncEx] = None,
        response_model_exclude: Optional[IncEx] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: Optional[type[routing.Response]] = None,
        name: Optional[str] = None,
        callbacks: Optional[List[Dict[str, Any]]] = None,
        openapi_extra: Optional[Dict[str, Any]] = None,
        generate_unique_id_function: Optional[Callable[[routing.APIRoute], str]] = None,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        return self.router.post(
            path,
            response_model=response_model,
            status_code=status_code,
            tags=tags,
            dependencies=dependencies,
            summary=summary,
            description=description,
            response_description=response_description,
            responses=responses,
            deprecated=deprecated,
            operation_id=operation_id,
            response_model_include=response_model_include,
            response_model_exclude=response_model_exclude,
            response_model_by_alias=response_model_by_alias,
            response_model_exclude_unset=response_model_exclude_unset,
            response_model_exclude_defaults=response_model_exclude_defaults,
            response_model_exclude_none=response_model_exclude_none,
            include_in_schema=include_in_schema,
            response_class=response_class,
            name=name,
            callbacks=callbacks,
            openapi_extra=openapi_extra,
            generate_unique_id_function=generate_unique_id_function,
        )
