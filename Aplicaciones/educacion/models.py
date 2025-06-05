from django.db import models

# Create your models here.
class Contacto(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField()
    funciones=models.TextField()
    horario=models.CharField(max_length=500)
    sueldo= models.DecimalField(max_digits=10, decimal_places=2)
    logo=models.FileField(upload_to='cargos',null=True,blank=True) #subir archivos
    def _str_(self):
        fila="{0}: {1} {2}"
        return fila.format(self.id, self.nombre, self.descripcion, self.funciones, self.horario, self.sueldo, self.logo )
from django.db import models


# TABLAS
class Estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    correo_electronico = models.EmailField(max_length=254, unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id_estudiante}: {self.nombre} {self.apellido}"

class Docente(models.Model):
    id_docente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    correo_electronico = models.EmailField(max_length=254, unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id_docente}: {self.nombre} {self.apellido} ({self.especialidad})"

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=200)
    descripcion = models.TextField()
    id_docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    creditos = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.id_curso}: {self.nombre_curso} ({self.creditos} créditos)"

class Matricula(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('cancelado', 'Cancelado'),
    ]

    id_matricula = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_matricula = models.DateField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='activo')

    def __str__(self):
        return (f"{self.id_matricula}: {self.id_estudiante.nombre} {self.id_estudiante.apellido} "
                f"- {self.id_curso.nombre_curso} ({self.estado})")
