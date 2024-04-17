import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from device.models import *


def index(request):
    return HttpResponse("Hello, world. You're at the device index.")




def infoSet(request):
    response = {'infoSet success'}
    return HttpResponse(response)

def netInfo(request):
    try:
        infos = netInfoModel.objects.all()
    except Exception as e:
        return HttpResponse(type(e).__name__+" "+str(e),status=500)

    response = {}
    for info in infos:
        response[info.id] = {
            'port_speed': info.port_speed,
            'link_speed': info.link_speed
        }
    return JsonResponse(response)


def routeAdd(request):
    response = {'routeAdd success'}
    return HttpResponse(response)


def routeDel(request):
    response = {'routeDel success'}
    return HttpResponse(response)


def routeList(request):
    response = ['10.0.0.0/24 => 0', '10.0.1.0/24 => 1']
    return JsonResponse(response, safe=False)


def verifyAdd(request):
    response = {'verifyAdd success'}
    return HttpResponse(response)


def verifyDel(request):
    response = {'verifyDel success'}
    return HttpResponse(response)


def verifyList(request):
    response = ['10.0.0.0/24 & 0', '10.0.1.0/24 & 1']
    return JsonResponse(response, safe=False)


def deviceInfo(request):
    throughput = 100
    filterCount = 50
    def avgDelay():
        return 0.1
    avgDelay = avgDelay()
    response = {'throughput': throughput, 'filterCount': filterCount, 'avgDelay': avgDelay}
    return JsonResponse(response)



def log(request):
    response = {"log......"}
    return HttpResponse(response)


def vpn(request):
    return HttpResponse("Hello, world. You're at the device vpn.")
