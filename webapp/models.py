
from django.contrib.auth.models import User
from django.db import models

# User Profile Model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

# Pet Report Model
class PetReport(models.Model):
    PET_TYPE_CHOICES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Bird', 'Bird'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Lost', 'Lost'),
        ('Found', 'Found'),
    ]
    customer_name = models.CharField (max_length = 20, blank = True, null = True )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pet_reports', blank = True, null = True)
    pet_name = models.CharField (max_length = 20, blank = True, null = True )
    pet_type = models.CharField(max_length=50, choices=PET_TYPE_CHOICES)
    breed = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100)
    markings = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    last_seen_location = models.CharField(max_length=200)
    date_reported = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='pet_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.status}: {self.pet_type} - {self.color}"

# Match Notification Model
class MatchNotification(models.Model):
    pet_report = models.ForeignKey(PetReport, on_delete=models.CASCADE, related_name='notifications')
    matched_with = models.ForeignKey(PetReport, on_delete=models.CASCADE, related_name='matched_notifications')
    is_viewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Match for {self.pet_report} with {self.matched_with}"

# Shelter Model
class Shelter(models.Model):
    name = models.CharField(max_length=150)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

# Community Post Model
class CommunityPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='community_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
