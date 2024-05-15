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
        return HttpResponse(type(e).__name__ + " " + str(e), status=500)

    response = {}
    for info in infos:
        response[info.id] = {
            'ipAddress': info.ipAddress,
            'mask': info.mask,
            'arriveSpeed': info.arriveSpeed,
        }
    return JsonResponse(response)


def portInfo(request):
    try:
        infos = portInfoModel.objects.all()
    except Exception as e:
        return HttpResponse(type(e).__name__ + " " + str(e), status=500)

    response = {}
    for info in infos:
        response[info.id] = {
            'ipAddress': info.ipAddress,
            'mask': info.mask,
            'arriveSpeed': info.arriveSpeed,
            'rx': info.rx,
            'tx': info.tx,
        }
    # response = [{'rx': 10690, 'tx': 2},
    #             {'rx': 2, 'tx': 10690},
    #             {'rx': 0, 'tx': 0},
    #             {'rx': 0, 'tx': 0},
    #            ]
    return JsonResponse(response)

def verifySwitch(request):
    # set verify mode
    info = deviceInfoModel.objects.first()
    info.verifyMode = not info.verifyMode
    info.save()

    response = deviceInfoModel.objects.first().verifyMode
    return JsonResponse(response, safe=False)

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
    try:
        info = deviceInfoModel.objects.get(pk=1)
    except Exception as e:
        return HttpResponse(type(e).__name__ + " " + str(e), status=500)
    throughput = info.throughput
    verifySpeed = info.verifySpeed
    avgDelay = info.avgDelay
    verifyMode = info.verifyMode
    tableUsage = info.tableUsage
    response = {'throughput': throughput, 'verifySpeed': verifySpeed, 'avgDelay': avgDelay, 'verifyMode': verifyMode, 'tableUsage': tableUsage}
    return JsonResponse(response)


def log(request):
    response = {"log......"}
    return HttpResponse(response)


def vpn(request):
    return HttpResponse("Hello, world. You're at the device vpn.")
