from rest_framework.routers import SimpleRouter, Route
from src.infrastructure.factories.users import UserViewSetFactory
from src.interfaces.routes.users import user_router


class UserRouter(SimpleRouter):
    routes = [
         Route(
            url=user_router.get_url('users_list'),
            mapping=user_router.map('users_list'),
            initkwargs={'viewset_factory': UserViewSetFactory},
            name='{basename}-list',
            detail=False,
        ),
    ]
