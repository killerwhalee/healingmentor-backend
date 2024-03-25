from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import User

import uuid


class Multiplyer(models.Model):
    """
    Multiplyer Data

    Manages user tokens for score multiplying bonus time.

    """

    # Multiplyer extends user
    user = models.OneToOneField("user.User", primary_key=True, on_delete=models.CASCADE)

    # Daily multiplyer
    daily_datetime = models.DateTimeField(
        "Last daily multiplyer creation", auto_now=False, auto_now_add=True
    )
    daily_tokens = models.IntegerField("Daily multiplyer left in seconds", default=900)

    # Hourly multiplyer
    hourly_datetime = models.DateTimeField(
        "Last hourly multiplyer creation", auto_now=False, auto_now_add=True
    )
    hourly_tokens = models.IntegerField(
        "Hourly multiplyer left in seconds", default=300
    )


@receiver(post_save, sender=User)
def create_user_multiplyer(sender, instance, created, **kwargs):
    if created:
        Multiplyer.objects.create(user=instance)


class Session(models.Model):
    """
    ### Base Session Model

    This model is for base of every session model. Also, fields in this model are read-only.

    When you create new specified session model, inherit this model.

    """

    # Identifier
    id = models.UUIDField(
        "Session id",
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    # Basic information
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    # Common fields
    score = models.IntegerField("session points", default=0)


class GuidedMeditation(Session):
    lecture = models.CharField(max_length=64)
    reports = models.JSONField()


class RespiratoryGraph(Session):
    graph_data = models.JSONField("graph data")
    reports = models.JSONField()


class SustainedAttention(Session):
    graph_data = models.JSONField("graph data")
    rate_data = models.JSONField("rating data", default=list)
    reports = models.JSONField()
