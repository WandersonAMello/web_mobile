"""
URL configuration for sistema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from sistema.views import Login, Logout

urlpatterns = [
    path('', Login.as_view(), name='Login'), #redireciona a url raiz para a view de login
    path('logout/', Logout.as_view(), name='Logout'), #redireciona a url /logout para a view de logout
    path('admin/', admin.site.urls), #redireciona todas as urls /admin para o admin do django
    path('veiculo/', include('veiculo.urls'), name='veiculo'), #redireciona todas as urls /veiculo para o app veiculo
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
