"""p5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from p5 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index,name="index"),
    path('first/',views.first,name="first"),
    path('second/',views.second,name="second"),
    path('third/',views.third,name="third"),
    path('fourth/',views.fourth,name="fourth"),
    path('fifth/',views.fifth,name="fifth"),
    path('urls_data/<name>',views.urls_data,name="urls_data"),
    path('urls_data1/<ab>',views.urls_data1,name="urls_data1"),
    path('urls_data2/<c>/<d>',views.urls_data2,name="urls_data2"),
    path('urls_data3/<greater>',views.urls_data3,name="urls_data3"),
    path('urls_data4/<string>',views.urls_data4,name="urls_data4")
]
