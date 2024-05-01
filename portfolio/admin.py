from django.contrib import admin

# Register your models here.
# In admin.py

from django.contrib import admin
from .models import ContactSubmission

class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']  # Customize which fields to display in the admin list view
    search_fields = ['name', 'email']              # Add fields to enable searching in the admin interface
    list_filter = ['created_at']                   # Add fields for filtering in the admin interface

admin.site.register(ContactSubmission, ContactSubmissionAdmin)



# portfolio/admin.py


from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')


# portfolio/admin.py

from django.contrib import admin
from .models import Project

admin.site.register(Project)

