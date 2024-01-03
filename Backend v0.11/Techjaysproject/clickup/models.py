from django.db import models
#
# # Create your models here.
# from django.conf import settings
#
#
# class Credential(models.Model):
#     """ A user can have many generated credentials """
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     value = models.CharField()
#
#     # Here we override the save method to avoid that each user request create new credentials on top of the existing one
#
#     def __str__(self):
#         return f"{self.user.username} - {self.value}"