from django.urls import path
from contatos.views import index

urlpatterns = [
    path('', index)
]