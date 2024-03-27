
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login2', views.login2, name='login2'),
    path('student',views.student, name='student'),
    path('lecturer',views.lecturer, name='lecturer'),
]
