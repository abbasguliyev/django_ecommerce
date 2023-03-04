from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django_ecommerce.common.models import BaseModel
from .managers import UserManager

class User(AbstractUser):
    MAN = "man"
    WOMAN = "woman"
    GENDER_CHOICE = (
        (MAN, "man"),
        (WOMAN, "woman"),
    )
    username = None
    email = models.EmailField(_('email_address'), unique=True)
    is_customer = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=100,
        choices=GENDER_CHOICE,
        default=MAN
    )
    phone = models.CharField(_("phone"), max_length=50, blank=True, null=True)
    address = models.TextField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserManager

    def __str__(self) -> str:
        return self.email