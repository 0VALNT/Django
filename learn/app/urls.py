from django.urls import path, include
from .views import *

urlpatterns = [
    path('index/', BookList.as_view(), name='index'),
    path('create/', BookCreate.as_view(), name='create'),
    path('update/<int:pk>', BookUpdate.as_view(), name='update'),
    path('delete/<int:pk>', BookDelete.as_view(), name='delete'),
]
