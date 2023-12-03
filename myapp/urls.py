from django.urls import path
from . import views
from .views import MapView
from channels.routing import ProtocolTypeRouter, URLRouter

urlpatterns = [
    path('', views.home, name = "HOME"),
    #path('newPage/', views.users, name = "USER"),
    #path('editPage/<int:user_id>/', views.edit, name = "EDIT"),
    #path('delete/<int:user_id>/', views.delete_user, name='DELETE'),
    path('mysignup/', views.myregister, name = "REGISTER"),
    path('mylogin/', views.mylogin, name = "LOGIN"),
    path('userhome/<int:user_id>/', views.UserHomePage, name = "UserHomePage"),
    path('adminhome/<int:user_id>/', views.AdminHomePage, name = "AdminHomePage"),
    path('arrest/<int:admin_id>/', views.ArrestPage, name = "ArrestPage"),    
    path('arrest/<int:admin_id>/<int:criminal_id>/', views.ArrestPage, name = "ArrestPage"),
    path('emergency/<int:admin_id>/', views.emergency, name = "emergency"),
    path('applyCIS/', views.applyCISLoader, name = "applyCISLoad"),
    path('save_marker/', views.save_marker, name = "save_marker"),
    path('criminalpage/<int:admin_id>', views.allCriminalPage, name = "CriminalPage"),
    path('criminalpage/', views.allCriminalPage, name = "CriminalPage"),
    path('p1complain/<int:user_id>/<int:FIR_id>', views.complain1, name = "UseComplainPage1"),
    path('p2complain/<int:user_id>/<int:FIR_id>', views.complain2, name = "UseComplainPage2"),
    path('p3complain/<int:user_id>/<int:FIR_id>', views.complain3, name = "UseComplainPage3"),
    path('p4complain/<int:user_id>/<int:FIR_id>', views.complain4, name = "UseComplainPage4"),
    path('saveContents/<int:user_id>/', views.saveComplain_1, name = "SAVE1"),
    path('activate/<uidb64>/<token>',views.activatefunction, name="ACTIVATE"),
    path('fetch_user_data/',views.fetch_user_data, name="fetch_user_data"),
    path('fetch_victim_data/',views.fetch_victim_data, name="fetch_victim_data"),
    path('Upload_Victim_Record/',views.upload_victim_record, name="upload_victim_record"),
    path('Upload_WITHNESS_Record/',views.upload_witeness_record, name="upload_witeness_record"),
    path('Upload_Offender_Record/',views.upload_offender_record, name="upload_offender_record"),
    path('your_complaint_view/',views.pdf_view, name="pdf_view"),
    path('page5Fir/<int:user_id>/<int:fir_id>',views.page5Fir, name="page5Fir"),
    path('backtohome/<int:criminal_id>/<int:user_id>', views.backtohome, name="backtohome"),
    path('search_req_user/<int:user_id>/', views.goto_search_page, name = "Search_Page"),
    path('search_req_admin/<int:admin_id>/', views.goto_admin_search_page, name = "goto_admin_search_page"),
    #path('map/', MapView.as_view(), name='map-view'),

    path('map/', views.context_date, name='map-view'),
    path('get-station/', views.near_stations),
]