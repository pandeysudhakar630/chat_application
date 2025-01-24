from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message  # Ensure the Message model is correctly implemented
from django.db.models import Q  # Import Q for complex queries
from django.contrib import messages  # To show error messages
from django.http import HttpResponse

# Sign-Up View
def signup(request):
    """
    Handles user registration.
    Displays a registration form and creates a new user account upon valid input.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Your account has been created successfully!")  # Success message
            return redirect('chat_home')  # Redirect to chat homepage after signing up
        else:
            messages.error(request, "Error: Please ensure your password matches the requirements.")  # Error message
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Login View
def login_view(request):
    """
    Checks if the username and password are correct.
    If login fails, shows an error message.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in successfully!")  # Success message
            return redirect('chat_home')  # Redirect to chat homepage upon successful login
        else:
            messages.error(request, "Invalid username or password. Please try again. If you are a new user, kindly sign up.")  # Error message for invalid login

    return render(request, 'login.html')  # Render the login page if GET request

# Chat Homepage View
@login_required
def chat_home(request):
    """
    Displays the chat homepage.
    Shows a list of users to chat with, excluding the logged-in user.
    """
    users = User.objects.exclude(id=request.user.id)  # Exclude the logged-in user
    return render(request, 'chat_home.html', {'users': users})

# Chat Room View
@login_required
def chat_room(request, user_id):
    """
    Displays the chat room between the logged-in user and the selected user.
    Fetches messages between the two users, ordered by timestamp.
    Handles sending new messages.
    """
    user_to_chat = get_object_or_404(User, id=user_id)  # Get the user to chat with
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(receiver=user_to_chat)) |
        (Q(sender=user_to_chat) & Q(receiver=request.user))
    ).order_by('timestamp')  # Fetch all messages between the two users, ordered by timestamp

    # Handle message sending
    if request.method == 'POST':
        message_content = request.POST.get('message')
        if message_content:
            Message.objects.create(sender=request.user, receiver=user_to_chat, content=message_content)
    
    return render(request, 'chat_room.html', {'user_to_chat': user_to_chat, 'messages': messages})

# Chat View with WebSocket Integration
@login_required
def chat_view(request):
    """
    Displays the chat interface with WebSocket integration.
    """
    return render(request, 'chat_room.html')  # Ensure 'chat_room.html' exists in your templates directory

# Index View
def index(request): 
    """
    Simple welcome view for the chat app.
    """
    return HttpResponse("Hello, this is the chat app!")

# WebSocket-Specific View
@login_required
def websocket_chat_view(request, user_id):
    """
    Handles WebSocket requests for real-time chat communication.
    """
    user_to_chat = get_object_or_404(User, id=user_id)
    return render(request, 'chat_room.html', {'user_to_chat': user_to_chat})
