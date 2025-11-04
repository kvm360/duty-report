from django.db import models
from django.contrib.auth.models import User
import pytz

class TeamMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timezone = models.CharField(max_length=100, default='UTC')

    def __str__(self):
        return self.user.username

class Shift(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start_time_utc = models.DateTimeField()
    end_time_utc = models.DateTimeField()
    created_by = models.ForeignKey(User, related_name='created_shifts', on_delete=models.SET_NULL, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.member.username} - {self.title}"

class PTORequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.user.username} ({self.status})"
