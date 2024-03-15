from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  avatar = models.ImageField(upload_to="users_avatars", blank=True, null=True, verbose_name="Аватар")
  phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Номер телефона")

  class Meta:
    db_table = 'user'
    verbose_name = "Пользователя"
    verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
      return self.username, self.first_name, self.last_name