from django.contrib import admin
from .models import UserProfile, PetReport, MatchNotification,Shelter, CommunityPost
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(PetReport)
admin.site.register(MatchNotification)
admin.site.register(Shelter)
admin.site.register(CommunityPost)
