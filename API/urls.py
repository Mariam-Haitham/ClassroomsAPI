from API import views
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [

	path('classes/', views.ClassroomList.as_view(), name="classes-list"),
     
    path('classes/<int:classroom_id>/detail', views.ClassroomDetails.as_view(), name="classes-details"),
    path('classes/<int:classroom_id>/update/', views.ClassroomUpdate.as_view(), name="classes-update"),
    path('classes/<int:classroom_id>/delete/', views.ClassroomCancel.as_view(), name="classes-cancel"),
    path('classes/create', views.ClassroomCreate.as_view(), name = 'classes-create'),

    path('api/token/', TokenObtainPairView.as_view(), name='login'),

]