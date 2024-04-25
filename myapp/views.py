from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from myapp.forms import StudentLoginForm
from myapp.forms import LecturerLoginForm
from .models import Hall
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Hall,Booking
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import BookingRequest
from django.http import HttpResponse
from .forms import BookingRequestForm
from .models import Announcement
# Create your views here.
def home(request):
    return render(request, 'home.html')

def login3(request):
    return render(request, 'login3.html')

def select(request):
    return render(request, 'select.html')

def display(request):
    return render(request, 'display.html')

def book_hall_form(request):
    return render(request, 'book_hall_form.html')

@login_required
def student(request):
    return render(request, 'student.html')
@login_required
def lecturer(request):
    return render(request, 'lecturer.html')


def login2(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')  # Using password as it's the first password field
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('student')  # Redirect to student after successful login
    else:
        form = StudentLoginForm()
    return render(request, 'login2.html', {'form': form})


def login3(request):
    if request.method == 'POST':
        form = LecturerLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')  # Using password as it's the first password field
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('lecturer')  
    else:
        form = LecturerLoginForm()
    return render(request, 'login3.html', {'form': form})

def available(request):
    halls = Hall.objects.all()
    return render (request, 'available.html', {'halls' : halls})

# def book_hall(request):
#     if request.method == 'POST':
#         hall_id = request.POST.get('hall_id')
#         hall = Hall.objects.get(pk=hall_id)
#         if hall.is_available:
#             # Proceed with the booking logic
#             # Update the 'is_available' attribute if the hall is successfully booked
#             hall.is_available = False
#             hall.save()
#             # Redirect or render a success message
#             return redirect('booking_success')
#         else:
#             # Render a message indicating that the hall is not available
#             return render(request, 'hall_not_available.html')
#     else:
#         # Handle GET requests to this view
#         # Render the form to book a hall
#         return render(request, 'book_hall_form.html')
    
def book_time_slot(request):
    if request.method == 'POST':
        hall_id = request.POST.get('hall_id')
        time_slot = request.POST.get('time_slot')
        hall = Hall.objects.get(id=hall_id)
        # Perform booking logic here
        # For example, update the corresponding time slot field in the Hall model
        setattr(hall, f'slot_{time_slot}', False)
        hall.save()
        messages.success(request, f"Hall {hall.name} booked successfully for time slot {time_slot}!")
        return redirect('available')
    else:
        # Handle GET request if needed
        return redirect('available')  # Redirect to the available halls page
    
# def book_hall(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Optionally, redirect to a success page or another URL
#             return redirect('success_url')
#     else:
#         form = BookingForm()
#     return render(request, 'available.html', {'form': form})

def book_hall(request, hall_id):
    hall = get_object_or_404(Hall, pk=hall_id)
    # Assuming you have a BookingForm
    form = BookingForm()
    context = {
        'hall': hall,
        'form': form
    }
    return render(request, 'book_hall_form.html', context)

# def cancel_booking(request, booking_id):
#     # Retrieve the booking object
#     try:
#         booking = Booking.objects.get(id=booking_id)
#     except Booking.DoesNotExist:
#         messages.error(request, "Booking not found.")
#         return redirect('available')  # Redirect to the available halls page or any other appropriate page
    
#     # Perform cancellation logic (example: delete the booking)
#     booking.delete()

# def update_hall_status(request, hall_id):
#     if request.method == 'POST':
#         hall = Hall.objects.get(id=hall_id)
#         status = request.POST.get('status')

#         if status == 'occupied':
#             hall.is_available = False
#             hall.save()
#             messages.success(request, f'Hall {hall.name} is now occupied.')
#         elif status == 'vacant':
#             hall.is_available = True
#             hall.save()
#             messages.success(request, f'Hall {hall.name} is now vacant.')
#         else:
#             messages.error(request, 'Invalid status.')
        
#     return redirect('available')  # Redirect to the available halls page after updating status

# def update_hall_status(request, hall_id):
#     if request.method == 'POST':
#         hall = Hall.objects.get(pk=hall_id)
#         status = request.POST.get('status')
#         if status == 'occupied':
#             hall.is_available = False
#         elif status == 'vacant':
#             hall.is_available = True
#         hall.save()
#         messages.success(request, f'Hall status updated successfully.')
#         return redirect('available')
#     else:
#         messages.error(request, f'Invalid request method.')
#         return redirect('available')
def book_hall(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Process the form data and save to the database
            form.save()
            # Redirect to a success page or another URL
            return redirect('booked.html')
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})
    
def booked_halls(request):
    booked_halls = Hall.objects.exclude(booking=None)
    context = {'booked_halls': booked_halls}
    return render(request, 'booked.html', context)

def lecturer_dashboard(request):
    booked_halls = Hall.objects.filter(is_booked=True)  # Query the booked halls from the database
    return render(request, 'available.html.html', {'booked_halls': booked_halls})

def book_hall(request):
    if request.method == 'POST':
        lecturer = request.POST.get('lecturer')
        unit = request.POST.get('unit')
        day = request.POST.get('day')
        time_slot = request.POST.get('time_slot')

        BookingRequest.objects.create(lecturer=lecturer, unit=unit, day=day, time_slot=time_slot)

        return render(request, 'booking_confirmation.html')
    else:
        return render(request, 'booking_form.html')
    
def submit_booking_request(request):
    # Handle the form submission logic here
    if request.method == 'POST':
        # Process the form data
        # Redirect or render appropriate response
        return HttpResponse("Booking request submitted successfully")
    else:
        # Handle GET request (if applicable)
        return HttpResponse("Method not allowed")
    
def submit_booking_request(request):
    if request.method == 'POST':
        # If the request method is POST, it means the form is being submitted
        form = BookingRequestForm(request.POST)
        if form.is_valid():
            # If the form data is valid, save the booking request to the database
            form.save()
            # Optionally, you can redirect the user to a success page
            return redirect('lecturer')  # Replace 'success_page' with the URL name of your success page
        else:
            # If the form data is invalid, render the form again with error messages
            return render(request, 'booking_form.html', {'form': form})
    else:
        # If the request method is not POST, render the empty form
        form = BookingRequestForm()
        return render(request, 'booking_form.html', {'form': form})
    
def view_announcement(request):
    announcements = Announcement.objects.all().order_by('-pub_date')
    return render(request, 'view_announcement.html', {'announcements': announcements})