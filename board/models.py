from django.db import models

import uuid


class Post(models.Model):
    """
    Board Model

    It's named after its application,
    but model is for saving posts for board.

    """

    # Identifier
    id = models.UUIDField(
        "Post id",
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    # Basic information
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    # Post body fields
    post_category = models.CharField(
        "Category of Post",
        max_length=32,
        choices=[
            ("notice", "Notice Board"),
            ("free", "Free Board"),
            ("qa", "Q&A Board"),
        ],
    )
    post_title = models.CharField("Title of Post", max_length=64)
    post_contents = models.TextField("Contents of Post")


class Reply(models.Model):
    """
    Board Model

    It's named after its application,
    but model is for saving posts for board.

    """

    # Identifier
    id = models.UUIDField(
        "Reply id",
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    # Basic information
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    post = models.ForeignKey("board.Post", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    # Post body fields
    reply_contents = models.TextField("Contents of Reply")
