from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework import viewsets


class CreateListViewSet(
    ListModelMixin,
    CreateModelMixin,
    viewsets.GenericViewSet
):
    pass
