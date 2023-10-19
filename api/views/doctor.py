from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Patient, Doctor
from api.permissions import DoctorAccessPermission
from api.serializers.doctor import DoctorListSerializer, DoctorRetrieveSerializer, DoctorCreateSerializer, \
    DoctorUpdateSerializer
from api.serializers.patient import PatientListSerializer


class DoctorView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'

    permission_classes = [IsAuthenticated, DoctorAccessPermission]

    def get_serializer_class(self):
        if self.action == 'list':
            return DoctorListSerializer
        if self.action == 'retrieve':
            return DoctorRetrieveSerializer
        if self.action == 'create':
            return DoctorCreateSerializer
        if self.action == 'update':
            return DoctorUpdateSerializer
        if self.action == 'list_patient':
            return PatientListSerializer

    def get_queryset(self):
        if self.action == 'list_patient':
            return Patient.objects.all()

        return Doctor.objects.all()

    def list_patient(self, request, id):
        queryset = self.get_queryset().filter(visits__doctor_id=id).all()

        serializer = self.get_serializer(queryset, many=True)

        return Response(data=serializer.data)
