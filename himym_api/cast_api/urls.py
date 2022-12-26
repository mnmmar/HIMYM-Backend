from django.urls import path
from .import views

urlpatterns = [
    path('api/cast', views.CastList.as_view(), name='cast_list'),
    path('api/cast/<int:pk>', views.CastDetail.as_view(), name='cast_detail')

]