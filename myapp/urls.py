
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login2/', views.login2, name='login2'),
    path('login3/', views.login3, name='login3'),
    path('student/',views.student, name='student'),
    path('lecturer/',views.lecturer, name='lecturer'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('select/',views.select, name='select'),
    path('display/', views.display, name='display'),
    path('available/', views.available, name='available'),
    path('book_hall/', views.book_hall, name='book_hall'),
    path('book_time_slot/', views.book_time_slot, name='book_time_slot'), 
    path('book_hall/book_hall_form/', views.book_hall_form, name='book_hall_form'),
    # path('cancel-booking/', views.cancel_booking, name='cancel_booking'),
    # path('update-hall-status/<int:hall_id>/', views.update_hall_status, name='update_hall_status'),
    path('booked/', views.booked_halls, name='booked'),
    path('submit-booking/', views.submit_booking_request, name='submit_booking_request'),
    path('view_announcement/', views.view_announcement, name='view_announcement'),
]
