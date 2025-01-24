from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Sign-up and authentication URLs
    path('signup/', views.signup, name='signup'),  # Sign-up page
    path('', views.login_view, name='login'),  # Custom login page using login_view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout page

    # Chat-related URLs
    path('chat/', views.chat_home, name='chat_home'),  # Chat homepage
    path('chat/<int:user_id>/', views.chat_room, name='chat_room'),  # Chat room view with dynamic user_id

    # WebSocket-related URL for real-time chat
    path('ws/chat/<int:user_id>/', views.websocket_chat_view, name='websocket_chat'),  # WebSocket chat endpoint
]
