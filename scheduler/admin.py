from django.contrib import admin
from .models import TeamMember, Shift, PTORequest

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'timezone']
    list_filter = ['timezone']

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ['member', 'title', 'start_time_utc', 'end_time_utc', 'created_by']
    list_filter = ['member', 'start_time_utc']
    search_fields = ['member__username', 'title']

@admin.register(PTORequest)
class PTORequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'start_date', 'end_date', 'status']
    list_filter = ['status', 'start_date']
    search_fields = ['user__username', 'reason']
