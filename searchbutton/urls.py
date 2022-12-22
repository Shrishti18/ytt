"""searchbutton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from projectApp import views
from django.conf.urls.static import static
from searchbutton import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index,name='index'),
    path('',views.index2,name='index2'),
    path("add_video/", views.add_video, name="add_blogs"),
    # path("hi/",views.Import_Excel_pandas,name="Import_Excel_pandas"),
    # path('Import_Excel_pandas/', views.Import_Excel_pandas,name="Import_Excel_pandas"), 
    # path('Import_excel',views.Import_excel,name="Import_excel"),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)