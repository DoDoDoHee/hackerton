"""hackerton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import light.views
import heavy.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mypage/', light.views.mypage, name="mypage"),
    # light앱관련 url
    path('light/', light.views.index, name="index"),
    path('light/oneselection/', light.views.oneselection, name="oneselection"),
    path('light/twoselection/', light.views.twoselection, name="twoselection"),
    path('light/threeselection/', light.views.threeselection, name="threeselection"),
    path('light/buy/', light.views.buy, name="buy"),
    # path('light/<int:light_id>', lv.detail, name="detail")
    path('heavy/', heavy.views.heavymain , name="heavymain"),
    path('heavydetail/', heavy.views.heavydetail , name="heavydetail"),
    path('heavyfirst/', heavy.views.heavyfirst , name="heavyfirst"),
]
