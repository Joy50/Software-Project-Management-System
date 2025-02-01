from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Custom user manager
class UserManager(BaseUserManager):
    def create_user(self, email, dgfi_id, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, dgfi_id=dgfi_id)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, dgfi_id, password=None):
        user = self.create_user(email, dgfi_id, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


# Custom User model
class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    dgfi_id = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # Add other fields as needed
    # ...

    # User manager
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['dgfi_id']  # Fields required for superuser creation

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
