from django.db import models
from django.template.context_processors import request

from apps.core.models import ClassModel
from django.core.validators import MinValueValidator, MaxValueValidator


# Robots apps
class Robot(ClassModel):
    """Robot model """
    ROBOT_STATUS_CHOICES = [
        ('available', 'Disponible'),
        ('busy', 'Ocupado'),
        ('maintenance', 'Mantenimiento'),
        ('charging', 'Cargando'),
    ]
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    battery_level = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    capacity = models.PositiveIntegerField(help_text="Maximum number of items it can carry")
    status = models.CharField(max_length=20, choices=ROBOT_STATUS_CHOICES, default='available')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        self.model = self.model.upper()
        super(Robot, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Robot'
        verbose_name_plural = 'Robots'


class Location(models.Model):
    """ Location for robot """
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE, null=False, blank=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.robot.name - self.update}"