from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator

class UserManager(BaseUserManager):
    username_validator = UnicodeUsernameValidator()

    def create_user(self, email, name, age, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            age=age
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, age, password):
        user = self.create_user(
            email=email,
            name=name,
            age=age,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['name', 'age']
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.name

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField()

    def __str__(self):
        return self.product_nome
        
class Buy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField(default=1)
    total = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.user} comprou {self.amount} x {self.product} em {self.date}"

class Wine(models.Model):
    wine_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.wine_name}"

class Whisky(models.Model):
    whisky_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.whisky_name}"

class Cerveja(models.Model):
    cerveja_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.cerveja_name}"

class Enlatado(models.Model):
    enlatado_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.enlatado_name}"

class Vodka(models.Model):
    vodka_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.vodka_name}"

class Drink(models.Model):
    drink_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.drink_name}"