from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout, get_user


def user_login(request):
    """
    Handles user login.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered page for user login.
    """
    user_login = True
    input_username = request.POST.get('username')
    input_password = request.POST.get('password')

    if request.method == 'POST':
        try:
            user = User.objects.get(username=input_username)
            user_auth = authenticate(request, username=input_username, password=input_password)
            if user_auth is not None:
                login(request, user_auth)
                messages.info(request, f'Welcome {user.username.capitalize()}!')
                return redirect('home')
            else:
                messages.error(request, 'Username or password does not exist!')
        except Exception:
            messages.error(request, "User does not exist!")

    context = {'user_login': user_login}
    return render(request, 'users/user_login.html', context)


def user_logout(request):
    """
    Handles user logout.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Redirects to the 'home' page after logging the user out.
    """
    current_user = request.user
    logout(request)
    messages.info(request, 'Successfully logged out!')
    return redirect('home')


def user_register(request):
    """
    Handles user registration.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered page for user registration or a redirect to the 'home' page upon successful registration.
    """
    user_login = False
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')

    context = {'user_login': user_login, 'form': form}
    return render(request, 'users/user_login.html', context)
