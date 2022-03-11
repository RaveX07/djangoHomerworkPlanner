import email
from statistics import mode
from django.db import models
import uuid

from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.utils.translation import gettext_lazy as _
from django.db import models

class CustomAccountManager(UserManager):
    def create_user(self, username: str, email: Optional[str] = ..., password: Optional[str] = ..., **extra_fields: Any) -> _T:
        return super().create_user(username, email, password, **extra_fields)
    
    def create_superuser(self, username: str, email: Optional[str], password: Optional[str], **extra_fields: Any) -> _T:

        if not email:
            raise ValueError

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)

        return super().create_superuser(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    REQUIRED_FIELDS = ['e_mail', 'uuid']