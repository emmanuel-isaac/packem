from __future__ import unicode_literals

from django.contrib.auth import models


class UserManager(models.UserManager):
    def create(self, **kwargs):
        username = kwargs.get('email').strip()
        return super(UserManager, self).create_user(username, **kwargs)


class User(models.AbstractUser):
    objects = UserManager()
