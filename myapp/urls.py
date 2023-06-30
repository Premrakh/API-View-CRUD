from django.urls import path
from .views import *

urlpatterns = [
    path('get/',GetData.as_view()),
    path('post/',PostData.as_view()),
    path('update/<int:pk>',UpdateData.as_view()),
    path('delete/<int:pk>',DelData.as_view()),
    path('patch/<int:pk>',PatchData.as_view()),
]
