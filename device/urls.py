from django.contrib import admin
from django.urls import path
from device.views import *

urlpatterns = [
    # 主动
    path("registe", registe),

    # 被动
    path("deviceInfo", netInfo),
    path("routeAdd", routeAdd),
    path("routeDel", routeDel),
    path("routeList", routeList),
    path("verifyAdd", verifyAdd),
    path("verifyDel", verifyDel),
    path("verifyList", verifyList),
    path("throughput", throughput),
    path("filterCount",filterCount),
    path("avgDelay",avgDelay),
    path("log", log),
    path("vpn", vpn),
]
