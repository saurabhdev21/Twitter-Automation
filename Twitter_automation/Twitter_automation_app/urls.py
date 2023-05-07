from django.urls import path
from . import views


app = 'Twitter_automation_app'
urlpatterns = [
    path('', views.main, name='main'),
    path('submit_page/', views.submit_page, name= 'submit_page')
]