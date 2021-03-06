from django.urls import path, include
from gender_recog import views

# Template Tagging
app_name = 'gender_recog'

urlpatterns = [
    path('', views.gen_recog, name='explain'),
    path('predict/', views.gen_recog, name='gen_recog'),
]
