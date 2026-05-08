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
    avatar = models.ImageField(upload_to='avatars/%Y/%M/', null=True, blank=True)
    bio = models.TextField(blank=True)

    def number_of_follows(self):
        return self.follows.count() - 1

    def number_of_followers(self):
        return self.followed_by.count() - 1
    
    def __str__(self):
        return f"Perfil de: {self.user.username}"
        

class Galeria(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='posts/%Y/%m/%d')
    description = models.CharField(max_length=200)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)
    publicado_em = models.DateTimeField(auto_now_add=True)

    def likes_count(self):
        return self.likes.count()
    
    def __str__(self):
        return (
            f'{self.user.username} '
            f'({self.publicado_em:%m-%d-%Y %H:%M}): '
            f'{self.description}...'
        )
        
    class Meta:
        ordering = ['-publicado_em']


# Cria o perfil automaticamente ao criar um usuário
def criar_perfil(sender, instance, created, **kwargs):
    if created:
        user_profile = Perfil(user=instance)
        user_profile.save()
        # Ao criar o perfil ele segue a si mesmo automaticamente
        user_profile.follows.set([instance.perfil.id])
        user_profile.save()

post_save.connect(criar_perfil, sender=CustomUser)