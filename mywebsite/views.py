# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
import Constants


def home(request):
    return render_to_response("myhomepage.html")

def regions(request):
    region_list = Constants.regions
    context = {
       'regions' : region_list
    }
    return render_to_response("regions.html",context, context_instance=RequestContext(request))
    
def region(request,region):
    if region == "telangana":
        district_list = Constants.telangana_districts
    else:
        district_list = Constants.regions
    context = {
        'list':district_list
    }
    return render_to_response("success.html",context,context_instance=RequestContext(request))       

    
def districts(request):
    district_list = Constants.all_districts
    return render_to_response("districts.html",{"districts":district_list})

def district(request,district):
    if district == "hyderabad":
        return render_to_response("hyderabad.html")
    return render_to_response("other.html")