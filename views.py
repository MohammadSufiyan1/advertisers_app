from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2
from laravelapp.models import Lender,Loan

def industry_portal(request, industry):
    lenders = Lender.objects.filter(industry=industry)
    context = {'lenders': lenders}
    return render(request, 'industry_portal.html', context)

def geolocate_and_show_loans(request):
    # Use GeoIP2 to get user's location
    g = GeoIP2()
    user_location = g.city(request.META.get('REMOTE_ADDR'))

    loans = Loan.objects.filter(latitude=user_location.latitude, longitude=user_location.longitude)

    context = {'loans': loans}
    return render(request, 'loan_list.html', context)