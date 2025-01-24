from django.contrib import admin
from django.urls import path, include  # 'include' allows including app-specific URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin panel
    path('', include('chat.urls')),  # Include URLs from the 'chat' app
]
 