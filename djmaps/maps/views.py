from django.shortcuts import render


def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'default.html',
                  { 'mapbox_access_token': mapbox_access_token })


def vulIndex_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'vulIndex.html',
                  { 'mapbox_access_token': mapbox_access_token })


def medIncome_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'medIncome.html',
                  { 'mapbox_access_token': mapbox_access_token })


def totalPop_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'totalPop.html',
                  { 'mapbox_access_token': mapbox_access_token })


def underlyHealth_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'underlyHealth.html',
                  { 'mapbox_access_token': mapbox_access_token })


def healthInfra_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'healthInfra.html',
                  { 'mapbox_access_token': mapbox_access_token })