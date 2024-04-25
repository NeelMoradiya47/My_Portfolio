from django.contrib import admin
from .models import Contact, Projects

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email_id', 'mobile_no', 'message')
    
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'description', 'image', 'url_link')
    
admin.site.register(Contact, ContactAdmin)
admin.site.register(Projects, ProjectsAdmin)
