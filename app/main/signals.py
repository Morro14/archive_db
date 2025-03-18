from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyUser
from django.contrib.auth.models import Group


# @receiver(post_save, sender=MyUser)
# def add_to_group(sender, insatnce, **kwargs):
#     # TODO

#     if Group.objects.filter("user_group").exists():
#         group = Group.objects.get("user_group")

#     else:
#         pass
