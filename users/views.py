from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Basic validation (you can add more)
        if not all([firstname, lastname, email, password]):
            messages.error(request, 'All fields are required.')
            return render(request, 'signup.html', request.POST) # Pass POST data back to prefill form

        if User.objects.filter(email=email).exists():
            messages.error(request, 'An account with this email already exists.')
            return render(request, 'signup.html', request.POST)

        try:
            # Assuming your custom User model has set_password method (common for AbstractBaseUser)
            # and email is the username field.
            user = User(
                username=email,
                email=email,
                first_name=firstname,
                last_name=lastname
            )
            user.set_password(password) # Hashes the password
            user.save()
            messages.success(request, 'Account created successfully! Please sign in.')
            return redirect('signin') # Replace 'signin' with your actual signin URL name
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
            return render(request, 'signup.html', request.POST)    
    return render(request, 'signup.html')

    
def signin_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print('Received args:', email, password)

        if not email or not password:
            messages.error(request, 'Email and password are required.')
            return render(request, 'signin.html', {'email': email})

        user = authenticate(request, username=email, password=password) # Django's authenticate

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'signin.html', {'email': email}) # Keep email in form
    return render(request, 'signin.html')

def signout_view(request):
    logout(request)
    messages.info(request, "You have been successfully signed out.")
    return redirect('home') # Redirect to home page or login page


# API Testing
def getUsers(request):
    users = User.objects.all()
    print('Users objects =', users)
    for user in users:
        print('Username:',user.username, 'Email:', user.email, 'Password:', user.password)
    return JsonResponse({'Users': 'Test!'}, status=200)
