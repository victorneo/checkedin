from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from crypto.rsa_utils import generate_rsa_key_pair


class User(AbstractUser):
    # Stores the public and private key for the user in strings
    public_key = models.TextField(blank=False)
    private_key = models.TextField(blank=False)


@receiver(pre_save, sender=User)
def populate_keys(sender, instance, *args, **kwargs):
    if instance.pk is None and not instance.public_key\
            and not instance.private_key:
        private_key, public_key = generate_rsa_key_pair()
        instance.private_key = private_key.decode()
        instance.public_key = public_key.decode()
