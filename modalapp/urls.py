from django.urls import path
from . import views

app_name = 'modalapp'

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('get_modal_content', views.get_modal_content, name='get_modal_content'),
]
