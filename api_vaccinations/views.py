from itertools import cycle
from rest_framework import mixins, generics, status
from rest_framework.response import Response
from .models import Drug, Vaccination
from .serializers import DrugSerializer, VaccinationSerializer


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


class VaccinationsAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    serializer_class = VaccinationSerializer
    queryset = Vaccination.objects.all()
    lookup_field = 'pk'

    def rut_validator(self, rut):
        reversed_digits = map(int, reversed(str(rut)))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(reversed_digits, factors))
        return 'K' if (-s) % 11 == 10 else str((-s) % 11)

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        if request.content_type == 'application/json':
            rut = request.data['rut'].replace('-', '').upper()
            dose_valid = True if 0.15 <= request.data['dose'] <= 1.0 else False
            if rut[-1] == self.rut_validator(rut[:-1]) and dose_valid:
                return self.create(request)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if request.content_type == 'application/json':
            rut = request.data['rut'].replace('-', '').upper()
            dose_valid = True if 0.15 <= request.data['dose'] <= 1.0 else False
            if rut[-1] == self.rut_validator(rut[:-1]) and dose_valid:
                return self.update(request, pk)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        return self.destroy(request, pk)