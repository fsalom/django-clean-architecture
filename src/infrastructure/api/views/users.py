from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from src.interfaces.controllers.users import UserController


class CurrencyViewSet(ViewSet):
    viewset_factory = None

    @property
    def controller(self) -> UserController:
        return self.viewset_factory.create()

    def list(self, request: Request, *args, **kwargs) -> Response:
        payload, status = self.controller.list()
        return Response(data=payload, status=status)
