from django.db import models

#Crear los modelos aqui

class Post(models.Model):
    text = models. TextField()

    def __str__(self):
        return self.text[:30]