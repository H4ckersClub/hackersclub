from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=500, null=True, blank=True)  # Optional field for short description
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    difficulty_level = models.CharField(max_length=50, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])
    image_url = models.URLField(max_length=200, blank=True, null=True)  # Optional field for image URL
    video_url = models.URLField(max_length=200, blank=True, null=True)
    published_date = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    duration = models.DurationField()  # Duration in hours, minutes, etc.
    instructor = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    prerequisites = models.TextField(blank=True, null=True)  # Optional field for prerequisites
    

    def __str__(self):
        return self.title

class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_reference = models.IntegerField(null=True, blank=True)  # Optional field for course reference number
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    price_paid = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    payment_id = models.CharField(max_length=100, unique=True, blank=True)  # Unique identifier for the payment transaction
    payment_status = models.CharField(max_length=30, default='pending')

    def __str__(self):
        if self.course:
            return f"{self.user.username} - {self.course.title}"
        return f"{self.user.username} - Course ID: ({self.course_reference})"