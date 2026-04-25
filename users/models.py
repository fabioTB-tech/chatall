from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

# Create your models here.
class CustomUser(AbstractUser):
    def __str__(self):
        return self.username


class Perfil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='perfil')
    follows = models.ManyToManyField('self',
        related_name='followed_by',
        symmetrical=False,
        blank=True)
    avatar = models.ImageField(upload_to='avatars/%Y/%M/', default='/default_pfp.png', null=True, blank=True)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return f"Perfil de: {self.user.username}"


# Cria o perfil automaticamente ao criar um usuário
def criar_perfil(sender, instance, created, **kwargs):
    if created:
        user_profile = Perfil(user=instance)
        user_profile.save()
        # Ao criar o perfil ele segue a si mesmo automaticamente
        user_profile.follows.set([instance.perfil.id])
        user_profile.save()

post_save.connect(criar_perfil, sender=CustomUser)