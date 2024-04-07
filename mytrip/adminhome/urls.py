from . import views

from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),
    path('insert_country',views.insert_country,name='insert_country'),
    path('updatecountry/<cid>', views.updatecountry,name='upcountry'),
    path('delcountry/<cid>',views.delcountry,name='delcountry'),
    path('insert_state',views.insert_state,name='insert_state'),
    path('updatestate/<stid>', views.updatestate,name='updatestate'),
    path('delstate/<stid>',views.delstate,name='delstate'),
    path('insert_district',views.insert_district,name='insert_district'),
    path('updatedistrict/<distid>', views.updatedistrict,name='updatedistrict'),
    path('deldistrict/<distid>',views.deldistrict,name='deldistrict'),

    path('insert_location',views.insert_location,name='insert_location'),
    path('updatelocation/<locid>', views.updatelocation,name='updatelocation'),
    path('dellocation/<locid>',views.dellocation,name='dellocation'),

    path('insert_destination_cat',views.insert_destination_cat,name='insert_destination_cat'),
    path('updateDestination_cat/<destcatid>', views.updateDestination_cat,name='updateDestination_cat'),
    path('delDestination_cat/<destcatid>',views.delDestination_cat,name='delDestination_cat'),

    path('insert_destination',views.insert_destination,name='insert_destination'),
    path('updateDestination/<destid>', views.updateDestination,name='updateDestination'),
    path('delDestination/<destid>',views.delDestination,name='delDestination'),
]

