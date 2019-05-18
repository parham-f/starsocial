from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Group)

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        GroupMemberInline,
    ]
