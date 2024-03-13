from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from core.utils import uuid_filepath


class UserManager(BaseUserManager):
    """
    Custom User Manager

    User authentication is made by access token.

    Therefore password of normal user is `None`.

    """

    use_in_migrations = True

    def create_user(self, username, password):
        """Create user object"""
        
        user = self.model(username=username)
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        """Create superuser object"""
        
        user = self.create_user(username, password)

        # Set admin permissions
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model
    
    It serves minimal user information, limited to username and password.

    """

    import uuid

    objects = UserManager()

    # Core user informations for authentication
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=16, unique=True)

    # Basic permissions overwritten
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "username"


# User Profile Model
class Profile(models.Model):
    """
    User Profile Model

    This model provided additional information of user.
    Isolated from login information, it seems more secured.

    """

    user = models.OneToOneField("user.User", on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(
        "Profile image",
        upload_to=uuid_filepath,
        default="/static/image/profile-default.png",
    )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
