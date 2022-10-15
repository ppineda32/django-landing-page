from django.urls import path
from . import views

# domain.com/my_app/
urlpatterns = [
    path('', views.index_view, name='index'),
]