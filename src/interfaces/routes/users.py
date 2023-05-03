from src.domain.core.routing import Router, Route, HTTP_VERB_GET
from src.interfaces.controllers.users import UserController
from src.interfaces.routes.constants import USER_PREFIX


user_router = Router()
user_router.register([
    Route(
        http_verb=HTTP_VERB_GET,
        path=fr'^{USER_PREFIX}/$',
        controller=UserController,
        method='list',
        name='users_list',
    ),
])