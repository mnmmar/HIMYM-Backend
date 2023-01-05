from django.urls import path
from .import views

urlpatterns = [
    path('api/blog', views.BlogList.as_view(), name='blog_list'),
    path('api/blog/<int:pk>', views.BlogDetail.as_view(), name='blog_detail')

]