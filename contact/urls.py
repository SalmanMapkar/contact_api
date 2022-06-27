from django.urls import path
from .views import ContactView

urlpatterns = [
    path('contact/<int:pk>/', ContactView.as_view()),
    path('contact/', ContactView.as_view()),

]