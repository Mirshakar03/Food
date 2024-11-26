from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    postal_code = models.CharField(max_length=10)
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Card(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=20)
    expiry_date = models.DateField()
    CVV = models.PositiveIntegerField()
    address = models.TextField()

    def __str__(self):
        return f"Card of {self.user.username}"


class Contact(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class Payment(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    pyment_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment by {self.user.username}"
