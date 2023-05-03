from django.urls import path, include

from src.infrastructure.api.routes.users.routers import UserRouter
from src.infrastructure.api.views.users import UserViewSet

user_router = UserRouter()
user_router.register('', viewset=UserViewSet, basename='users')

urlpatterns = [
    path('', include(user_router.urls)),
]
