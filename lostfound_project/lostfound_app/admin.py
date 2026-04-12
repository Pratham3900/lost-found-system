from django.contrib import admin
from .models import LostItem, FoundItem, ClaimRequest, Notification

admin.site.register(LostItem)
admin.site.register(FoundItem)
admin.site.register(ClaimRequest)
admin.site.register(Notification)