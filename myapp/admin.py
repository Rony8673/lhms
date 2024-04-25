from django.contrib import admin
from myapp.models import Hall
from .models import Booking
from .models import Hall, Booking, BookingRequest
from .models import Announcement
# Register your models here.

admin.site.register(Hall)
admin.register(Booking)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['lecturer', 'unit', 'day', 'start_time', 'end_time']
    search_fields = ['lecturer', 'unit', 'day']

@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ['lecturer', 'unit', 'day', 'time_slot']

admin.site.register(Announcement,)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('message', 'pub_date', 'expiration_date')
