from distutils.command.upload import upload
from django import db
from django.db import models

# Create your models here.


class PersonaModel(models.Model):
    personaId = models.AutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_column='id'
    )
    personaNombre = models.CharField(
        max_length=50,
        unique=False,
        null=False,
        db_column='nombre'
    )
    personaApellido = models.CharField(
        max_length=50,
        unique=False,
        null=False,
        db_column='apellido'
    )
    personaEmail = models.EmailField(
        max_length=50,
        unique=True,
        null=False,
        db_column='email'
    )
    personaFechaNac = models.DateField(
        db_column='fec_nac'
    )
    # Una tupla sirve para agrupar, como si fueran un único valor, varios valores que, por su naturaleza, deben ir juntos.
    opcionesEstadoCivil = [
        # (en el back, en la bd),
        ('SOLTERO', 'SOLTERO'),
        ('CASADO', 'CASADO'),
        ('VIUDO', 'VIUDO'),
        ('DIVORCIADO', 'DIVORCIADO'),
        ('COMPLICADO', 'COMPLICADO')
        ('NO_ESPECIFICA', 'NO_ESPECIFICA')
    ]
    personaEstadoCivil = models.CharField(
        choices=opcionesEstadoCivil,
        db_column='estado_civil',
        default='NO_ESPECIFICA'
    )
    # imageField guarda la ubicacion, el archivo es guardado dentro del proyecto
    personaFoto = models.ImageField(
        db_column='foto',
        upload_to='personas/',  # almacenamiento dentro del proyecto
        null=True
    )
