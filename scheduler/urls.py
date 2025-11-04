from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add-shift/', views.add_shift, name='add_shift'),
    path('edit-shift/<int:shift_id>/', views.edit_shift, name='edit_shift'),
    path('delete-shift/<int:shift_id>/', views.delete_shift, name='delete_shift'),
    path('my-schedule/', views.my_schedule, name='my_schedule'),
    path('all-members/', views.all_members, name='all_members'),
    path('member-schedule/<str:username>/', views.member_schedule, name='member_schedule'),
    path('pto-requests/', views.pto_requests, name='pto_requests'),
    path('update-pto-status/<int:pto_id>/', views.update_pto_status, name='update_pto_status'),
    path('export-schedule/', views.export_schedule, name='export_schedule'),
    path('profile-settings/', views.profile_settings, name='profile_settings'),
]
