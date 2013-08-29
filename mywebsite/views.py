# Create your views here.

from django.shortcuts import render_to_response


def home(request):
    return render_to_response("myhomepage.html")

def regions(request):
    region_list = ['Telangana','Andhra','RayalaSeema']
    return render_to_response("result.html",{"list":region_list})
    
def districts(request):
    district_list = ["mahaboobnagar","warangal","adilabad","nalgonda","hyderabad","nizamabad","karimnagar","khammam","rangareddy","medhak","kurnool","kadapa","chittoor","anantapur","prakasham","vishakapatanam","guntur","krishna","east godavari","west godavari","srikakulam","vijayanagaram","nellore"]
    return render_to_response("result.html",{"list":district_list})
