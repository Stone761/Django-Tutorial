from django.http import HttpResponse


def index(request):
    return HttpResponse("HAHA I DID IT!!")

def pizza(request):
    return HttpResponse('Pizza is better with pineapple.')

def trains(request):
    return HttpResponse('Trains are one of the coolest things in Factorio.')