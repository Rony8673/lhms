from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login2(request):
    return render(request, 'login2.html')

# def student(request):
#     form = UserCreationForm(request.POST)
#     if request.method == 'POST':
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         form.save()
#         auth_user = authenticate(username=username, password=password)
#         login2(request,auth_user)

#         return redirect('student')
#     return render(request, 'login2.html',{'form': form})

def student(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')  # Using password as it's the first password field
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('student')  # Redirect to student  after successful login
    else:
        form = UserCreationForm()
    return render(request, 'student.html', {'form': form})

def lecturer(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')  # Using password as it's the first password field
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('lecturer')  # Redirect to student  after successful login
    else:
        form = UserCreationForm()
    return render(request, 'lecturer.html', {'form': form})
