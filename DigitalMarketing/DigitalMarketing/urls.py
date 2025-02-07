"""
URL configuration for DigitalMarketing project.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings  # good idea
from django.views.generic import TemplateView
# from FirstProj import settings # bad idea

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('catalogue/', include('catalogue.urls')),
    path('basket/', include('basket.urls')),
    path('shipping/', include('shipping.urls')),
    # path('about/', about, name='about-us'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about-us'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  
    # path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
