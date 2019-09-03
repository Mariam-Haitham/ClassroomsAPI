from rest_framework.generics import (ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, 
		DestroyAPIView, CreateAPIView)

from datetime import datetime

from classes.models import Classroom
from .serializers import (
	ClassroomSerializer, ClassroomDetailsSerializer, 
	ClassroomUpdateSerializer, ClassroomCreateSerializer)

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


class ClassroomList(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomSerializer


class ClassroomDetails(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class ClassroomUpdate(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class ClassroomCancel(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class ClassroomCreate(CreateAPIView):
	serializer_class = ClassroomCreateSerializer


	def perform_create(self, serializer):
		serializer.save(teacher = self.request.user)
