from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.models import LogEntry
User=get_user_model()
# Django's built-in UserAdmin manages creation, editing, active status, groups and permissions.
@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
 list_display=("action_time","user","content_type","object_repr","action_flag")
 list_filter=("action_flag","content_type")
 search_fields=("object_repr","change_message")
 readonly_fields=("action_time","user","content_type","object_id","object_repr","action_flag","change_message")
 def has_add_permission(self,request): return False
 def has_change_permission(self,request,obj=None): return False
 def has_delete_permission(self,request,obj=None): return False
