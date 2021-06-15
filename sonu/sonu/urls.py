
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('',include('calc.urls')),
        path('',include('travello.urls')),

    path('admin/', admin.site.urls),
]
