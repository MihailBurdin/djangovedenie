"""
URL configuration for Burdin project.

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
from django.urls import path,re_path
from Mihail import views
urlpatterns = [
    path('',views.index, kwargs = {"name":"Бурдин Михаил Павлович","age":16,"interes":"Нравиться рисовать,ещё люблю плавать"}),
    path('about',views.about,kwargs = {"arrived":"Я приехал из Уфы","grade":"успеваемость в школе у меня была хорошей ,но я не был отличником","like_stude":"Я люблю учиться"}),
    path("contact",views.contact,kwargs= {"telephone":"+79962911378"})
]
