from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the device index.")

def registe(request):
    return HttpResponse("Hello, world. You're at the device registe.")

def netInfo(request):
    return HttpResponse("Hello, world. You're at the device netInfo.")

def routeAdd(request):
    return HttpResponse("Hello, world. You're at the device routeAdd.")

def routeDel(request):
    return HttpResponse("Hello, world. You're at the device routeDel.")

def routeList(request):
    return HttpResponse("Hello, world. You're at the device routeList.")

def verifyAdd(request):
    return HttpResponse("Hello, world. You're at the device verifyAdd.")

def verifyDel(request):
    return HttpResponse("Hello, world. You're at the device verifyDel.")

def verifyList(request):
    return HttpResponse("Hello, world. You're at the device verifyList.")

def throughput(request):
    return HttpResponse("Hello, world. You're at the device throughput.")

def filterCount(request):
    return HttpResponse("Hello, world. You're at the device filterCount.")

def avgDelay(request):
    return HttpResponse("Hello, world. You're at the device avgDelay.")

def log(request):
    return HttpResponse("Hello, world. You're at the device log.")

def vpn(request):
    return HttpResponse("Hello, world. You're at the device vpn.")


