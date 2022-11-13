import logging

logger = logging.getLogger("app")

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib import auth
from access.models import Doors

User = auth.get_user_model()


@receiver(pre_save, sender=Doors)
def save_or_create_door(sender, instance, **kwargs):
    created = instance.pk is None
    door_all_members_changed = False

    # if we didn't just create the door check if it's all_members property has changed
    if not created:
        door_all_members_changed = (
            instance.all_members != Doors.objects.get(id=instance.id).all_members
        )

    # if the door has all_members set, and it is new or all_members has changed, reset permissions for it
    if instance.all_members and (created or door_all_members_changed):
        # update access
        members = User.objects.all()
        door = Doors.objects.get(pk=instance.id)

        for member in members:
            member.profile.doors.add(door)
            member.profile.save()

        # once we're done, sync changes to the door
        door.sync()

    # if the door has all_members unset, and it is new or all_members has changed, unset permissions for it
    elif instance.all_members is False and door_all_members_changed:
        # update access
        members = User.objects.all()
        door = Doors.objects.get(pk=instance.id)

        for member in members:
            member.profile.doors.remove(door)
            member.profile.save()

        # once we're done, sync changes to the door
        door.sync()
