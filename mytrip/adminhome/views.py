from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from . import locationform
from .Destination_catform import Destination_cat_form
from .Stay_categoryform import stay_categoryform
from .countryform import Country_form
from .destinationform import Destination_form
from .districtform import District_form
from .districtform import District_form
from .locationform import Location_form
from .models import CountryModel, StateModel, DistrictModel, LocationModel, Destination_catModel, DestinationModel, \
    Stay_categoryModel
from .stateform import State_form


def home(request):
    return HttpResponse("Welcome to My Travel Planner<br>"
                        "<a href='insert_country'>Country</a><br>"
                        "<a href='insert_state'>State</a><br>"
                        "<a href='insert_district'>District</a><br>"
                        "<a href='insert_location'>Location</a><br>"
                        "<a href='insert_destination_cat'>Destination_category</a><br>"
                        "<a href='insert_destination'>Destination</a><br>"
                        )


#add country details in the country table
def insert_country(request):
    context={}
    form= Country_form(request.POST or None)
    c=request.POST.get('Country') #text box name

    if CountryModel.objects.filter(Country=c).exists():

        messages.info(request,'Country already exist')
        return redirect('/adminhm/insert_country')
    else:

        if form.is_valid():
            form.save()
            return redirect('/adminhm/insert_country')
    context['form1']=form
    context["coun"]=CountryModel.objects.all()
    return render(request,"insert_country.html",context)


#views country details
def viewcountry(request):
    context={}
    context["coun"]=CountryModel.objects.all()
    return render(request,"insert_country.html",context)



#update country details
def updatecountry(request,cid):
    context={}
    obj=get_object_or_404(CountryModel,id=cid)
    form3=Country_form(request.POST or None,instance=obj)
    if form3.is_valid():
        form3.save()
        return HttpResponseRedirect('/adminhm/insert_country')
    context['f3']=form3
    return render(request,"updatecountry.html",context)
#delete country
def delcountry(request,cid):
    context={}
    obj=get_object_or_404(CountryModel,id=cid)
    obj.delete()
    return HttpResponseRedirect('/adminhm/insert_country')

#insert state details in the state table
def insert_state(request):
    context={}
    form= State_form(request.POST or None)
    st=request.POST.get('State') #textbox name

    if StateModel.objects.filter(State=st).exists():

        messages.info(request,'State already exist')
        return redirect('/adminhm/insert_state')
    else:

        if form.is_valid():
            form.save()
            return redirect('/adminhm/insert_state')
    context['form1']=form
    context["state"]=StateModel.objects.all()
    return render(request,"insert_state.html",context)
#update state details
def updatestate(request,stid):
    context={}
    obj=get_object_or_404(StateModel,id=stid)
    form3=State_form(request.POST or None,instance=obj)
    if form3.is_valid():
        form3.save()
        return HttpResponseRedirect('/adminhm/insert_state')
    context['f3']=form3
    return render(request,"updatestate.html",context)
#delete state
def delstate(request,stid):
    context={}
    obj=get_object_or_404(StateModel,id=stid)
    obj.delete()
    return HttpResponseRedirect('/adminhm/insert_state')



#insert district details in the district table
def insert_district(request):
    context={}
    form= District_form(request.POST or None)
    dist=request.POST.get('District') #textbox name

    if DistrictModel.objects.filter(District=dist).exists():
        messages.info(request,'District already exist')
        return redirect('/adminhm/insert_district')
    else:

        if form.is_valid():
            form.save()
            return redirect('/adminhm/insert_district')
    context['form1']=form
    context["district"]=DistrictModel.objects.all()
    return render(request,"insert_district.html",context)
#views country details
def viewdistrict(request):
    context={}
    context["district"]=DistrictModel.objects.all()
    return render(request,"insert_district.html",context)

#update district details
def updatedistrict(request,distid):
    context={}
    obj=get_object_or_404(DistrictModel,id=distid)
    form3=District_form(request.POST or None,instance=obj)
    if form3.is_valid():
        form3.save()
        return HttpResponseRedirect('/adminhm/insert_district')
    context['f3']=form3
    return render(request,"updatedistrict.html",context)
#delete district
def deldistrict(request,distid):
    context={}
    obj=get_object_or_404(DistrictModel,id=distid)
    obj.delete()
    return HttpResponseRedirect('/adminhm/insert_district')


#insert location details in the location table
def insert_location(request):
    context={}
    locationform= Location_form(request.POST or None)
    loc=request.POST.get('Location') #textbox name

    if LocationModel.objects.filter(Location=loc).exists():
        messages.info(request,'Location is already exist')
        return redirect('/adminhm/insert_location')
    else:
        if locationform.is_valid():
            locationform.save()
            return redirect('/adminhm/insert_location')
    context['form1']=locationform
    context["location"]=LocationModel.objects.all()
    return render(request,"insert_location.html",context)
#update location details
def updatelocation(request, locid):
    context={}
    locat=get_object_or_404(LocationModel,id=locid)
    locationform=Location_form(request.POST or None,instance=locat)
    if locationform.is_valid():
        locationform.save()
        return HttpResponseRedirect('/adminhm/insert_location')
    context['f3']=locationform
    return render(request,"updatelocation.html",context)
#delete location
def dellocation(request,locid):
    context={}
    locat=get_object_or_404(LocationModel,id=locid)
    locat.delete()
    return HttpResponseRedirect('/adminhm/insert_location')

#insert destination category details  in destination category the  table
def insert_destination_cat(request):
    context={}
    destination_cat= Destination_cat_form(request.POST or None)
    destcat=request.POST.get('Destination_cat') #text box name

    if Destination_catModel.objects.filter(Destination_cat=destcat).exists():

        messages.info(request,'Destination_category is already exist')
        return redirect('/adminhm/insert_destination_cat')
    else:

        if destination_cat.is_valid():
            destination_cat.save()
            return redirect('/adminhm/insert_destination_cat')
    context['form1']=destination_cat
    context["destination_cat"]=Destination_catModel.objects.all()
    return render(request,"insert_Destination_cat.html",context)


#views Destination details
def viewDestination_cat(request):
    context={}
    context["destination_cat"]=Destination_catModel.objects.all()
    return render(request,"insert_Destination_cat.html",context)



#update Destination details
def updateDestination_cat(request,destcatid):
    context={}
    destcat=get_object_or_404(Destination_catModel,id=destcatid)
    destination_cat=Destination_cat_form(request.POST or None,instance=destcat)
    if destination_cat.is_valid():
        destination_cat.save()
        return HttpResponseRedirect('/adminhm/insert_destination_cat')
    context['f3']=destination_cat
    return render(request,"updatedestination_cat.html",context)
#delete Destination
def delDestination_cat(request,destcatid):
    context={}
    destcat=get_object_or_404(Destination_catModel,id=destcatid)
    destcat.delete()
    return HttpResponseRedirect('/adminhm/insert_destination_cat')
#insert destination  details  in destination the  table
def insert_destination(request):
    context={}
    destination= Destination_form(request.POST or None)
    dest=request.POST.get('Destination') #text box name

    if DestinationModel.objects.filter(Destination=dest).exists():

        messages.info(request,'Destination is already exist')
        return redirect('/adminhm/insert_destination')
    else:

        if destination.is_valid():
            destination.save()
            return redirect('/adminhm/insert_destination')
    context['form1']=destination
    context["destination"]=DestinationModel.objects.all()
    return render(request,"insert_Destination.html",context)


#views Destination details
def viewDestination(request):
    context={}
    context["destination"]=DestinationModel.objects.all()
    return render(request,"insert_Destination.html",context)



#update Destination details
def updateDestination(request,destid):
    context={}
    dest=get_object_or_404(DestinationModel,id=destid)
    destination=Destination_form(request.POST or None,instance=dest)
    if destination.is_valid():
        destination.save()
        return HttpResponseRedirect('/adminhm/insert_destination')
    context['f3']=destination
    return render(request,"updatedestination.html",context)
#delete Destination
def delDestination(request,destid):
    context={}
    dest=get_object_or_404(DestinationModel,id=destid)
    dest.delete()
    return HttpResponseRedirect('/adminhm/insert_destination')
# create stay category form
# def insert_stay_category(request):
#     context={}
#     stay_cat= stay_categoryform(request.POST or None)
#     stay=request.POST.get('stay_category') #text box name
#
#     if Stay_categoryModel.objects.filter(stay_category=stay).exists():
#
#         messages.info(request,'Stay_category is already exist')
#         return redirect('/adminhm/insert_stay_category')
#     else:
#
#         if stay_cat.is_valid():
#             stay_cat.save()
#             return redirect('/adminhm/insert_stay_category')
#     context['form1']=stay_cat
#     context["destination"]=DestinationModel.objects.all()
#     return render(request,"insert_Destination.html",context)
#
#
# def viewcust(request):
#     context={}
#     context["cust"]=Customer_model.objects.all()
#     return render(request,"viewcust.html",context)
#
#
# def update_customer(request,cid):
#     context={}
#     obj=get_object_or_404(Customer_model,id=cid)
#     form3= customerform(request.POST or None,request.FILES or None,instance=obj)
#     if form3.is_valid():
#         form3.save()
#         return HttpResponseRedirect('/viewcust')
#     context['f3']=form3
#     return render(request,"updatecustomer.html",context)
#
#
# def delcustomer(request,cid):
#     context={}
#     obj=get_object_or_404(Customer_model,id=cid)
#     obj.delete()
#     return HttpResponseRedirect('/viewcust')
