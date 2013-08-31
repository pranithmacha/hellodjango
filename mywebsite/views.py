# Create your views here.

from django.shortcuts import render_to_response
import Constants


def home(request):
    return render_to_response("myhomepage.html")

def regions(request):
    region_list = Constants.regions
    return render_to_response("regions.html",{"regions":region_list})
    
def region(request,region):
    if region == "telangana":
        district_list = Constants.telangana_districts
    else:
        district_list = Constants.regions
    return render_to_response("success.html",{"list":district_list})       

    
def districts(request):
    district_list = Constants.all_districts
    return render_to_response("districts.html",{"districts":district_list})
