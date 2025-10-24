from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employee.urls')),   # ✅ This line sends home URL to employee app
    path('api/', include('employee.urls')),  # keep this if you still want API access
]
