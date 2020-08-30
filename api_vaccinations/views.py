from rest_framework import mixins, generics, status
from rest_framework.response import Response
from .models import Drug
from .serializers import DrugSerializer


class DrugsAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = DrugSerializer
    queryset = Drug.objects.all()
    lookup_field = 'pk'

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)


class DrugAPIView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = DrugSerializer
    queryset = Drug.objects.all()
    lookup_field = 'pk'

    def post(self, request):
        if request.content_type == 'application/json':
            return self.create(request)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if request.content_type == 'application/json':
            return self.update(request, pk)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        return self.destroy(request, pk)
