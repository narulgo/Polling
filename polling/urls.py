from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from polls import views

urlpatterns = [
    path('', RedirectView.as_view(url='polls/', permanent=True)),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]