from django.contrib import admin
from django.urls import path
from device.views import *

urlpatterns = [
    path("index",index),


    # 被动
    path("infoSet", infoSet),
    path("netInfo", netInfo),
    path("routeAdd", routeAdd),
    path("routeDel", routeDel),
    path("routeList", routeList),
    path("verifyAdd", verifyAdd),
    path("verifyDel", verifyDel),
    path("verifyList", verifyList),
    path("deviceInfo", deviceInfo),
    path("log", log),
    path("vpn", vpn),
]
