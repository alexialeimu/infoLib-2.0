from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('books.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]
