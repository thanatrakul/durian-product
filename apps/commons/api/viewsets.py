from rest_framework.viewsets import ModelViewSet


class CRUDViewsetMixin(ModelViewSet):
    # prefetch_fields = []  # Here is for M2M fields
    # related_fields = []  # Here is for ForeignKeys

    # action_serializer_class = {
    #     "list": None,
    #     "create": None,
    #     "update": None,
    #     "partial_update": None,
    #     "destroy": None
    # }
    # serializer_class = UserSerializer
    # serializer_detail_class = UserDetailSerializer

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return self.serializer_class

    #     elif self.action == 'list':
    #         return self.list_serializer_class

    #     else:
    #         return self.serializer_class

    # def get_permissions(self):
    #     """
    #     Instantiates and returns the list of permissions that this view requires.
    #     """
    #     if self.action == 'list':
    #         permission_classes = [IsAuthenticated]
    #     else:
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]

    # def get_related_queries(self, queryset):
    #     # This method we will use in our ViewSet
    #     # for modify queryset, based on RELATED_FIELDS and PREFETCH_FIELDS

    #     if self.related_fields:
    #         queryset = queryset.select_related(*self.related_fields)

    #     if self.prefectch_fields:
    #         queryset = queryset.prefetch_related(*self.prefectch_fields)

    #     return queryset

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = self.get_related_queries(queryset)
    #     return queryset
    pass
