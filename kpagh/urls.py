"""
URL configuration for kpagh project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app_agh.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),
    path('advertsement/<int:ids>', details, name='details'),
    path('serch/', serch, name='serch'),
    path('adv/', save_agh, name='adv'),
    path('profile/', profile, name='profile'),
    path('delete/<int:idss>', delete_agh, name='delete'),
    path('report/<int:idsss>', report_agh, name='report'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
