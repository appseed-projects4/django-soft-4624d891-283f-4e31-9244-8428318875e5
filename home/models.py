# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Item(models.Model):

    #__Item_FIELDS__
    descripcion = models.CharField(max_length=255, null=True, blank=True)

    #__Item_FIELDS__END

    class Meta:
        verbose_name        = _("Item")
        verbose_name_plural = _("Item")


class Categoria(models.Model):

    #__Categoria_FIELDS__
    descripcion = models.CharField(max_length=255, null=True, blank=True)

    #__Categoria_FIELDS__END

    class Meta:
        verbose_name        = _("Categoria")
        verbose_name_plural = _("Categoria")


class Usuario(models.Model):

    #__Usuario_FIELDS__
    usuario = models.CharField(max_length=255, null=True, blank=True)
    nombre = models.CharField(max_length=255, null=True, blank=True)

    #__Usuario_FIELDS__END

    class Meta:
        verbose_name        = _("Usuario")
        verbose_name_plural = _("Usuario")


class Orden(models.Model):

    #__Orden_FIELDS__
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=255, null=True, blank=True)

    #__Orden_FIELDS__END

    class Meta:
        verbose_name        = _("Orden")
        verbose_name_plural = _("Orden")


class Ordenitem(models.Model):

    #__Ordenitem_FIELDS__
    item = models.CharField(max_length=255, null=True, blank=True)
    orden = models.CharField(max_length=255, null=True, blank=True)

    #__Ordenitem_FIELDS__END

    class Meta:
        verbose_name        = _("Ordenitem")
        verbose_name_plural = _("Ordenitem")



#__MODELS__END
