from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('', include(f'{settings.API_ROUTES}.users.urls'))
]
