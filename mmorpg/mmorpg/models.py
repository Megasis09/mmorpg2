from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ('tank', 'Танки'),
    ('heal', 'Хилы'),
    ('dd', 'ДД'),
    ('trader', 'Торговцы'),
    ('guildmaster', 'Гилдмастеры'),
    ('questgiver', 'Квестгиверы'),
    ('blacksmith', 'Кузнецы'),
    ('leatherworker', 'Кожевники'),
    ('alchemist', 'Зельевары'),
    ('enchanter', 'Мастера заклинаний')
)

class Ad(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='ad_images/', blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class AdResponse(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)