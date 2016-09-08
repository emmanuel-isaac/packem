from __future__ import unicode_literals

from django.contrib.auth import models


class UserManager(models.UserManager):
    def create(self, **kwargs):
        username = kwargs.get('email').strip()
        return super(UserManager, self).create_user(username, **kwargs)


class User(models.AbstractUser):
    objects = UserManager()

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        if not self.cart_set.all().count():
            return self.cart_set.create()
