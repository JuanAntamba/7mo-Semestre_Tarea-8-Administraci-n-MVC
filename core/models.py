from django.db import models
from django.core.exceptions import ValidationError

class Local(models.Model):
    nombre = models.CharField(max_length=100)

class Producto(models.Model):
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    precio_base = models.FloatField()

class Promocion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    porcentaje_descuento = models.FloatField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def clean(self):
        #(Evita que se rompa el Score del Core)
        if self.porcentaje_descuento <= 0 or self.porcentaje_descuento >= 100:
            raise ValidationError('Error crítico: El descuento debe ser un porcentaje real para el Matchmaking.')
        
        if self.hora_inicio >= self.hora_fin:
            raise ValidationError('Error de lógica: La hora de fin debe ser posterior a la de inicio.')

    def save(self, *args, **kwargs):
        self.full_clean() # Fuerza a ejecutar clean() antes de tocar la base de datos
        super().save(*args, **kwargs)