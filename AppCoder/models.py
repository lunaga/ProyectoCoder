from django.db.models import Model, CharField, IntegerField, EmailField, DateField, BooleanField

class Curso(Model):
    nombre = CharField(max_length=40)
    camada = IntegerField()


class Estudiante(Model):
    nombre = CharField(max_length=30)
    apellido = CharField(max_length=30)
    email = EmailField()
    
class Profesores(Model):
     nombre = CharField(max_length=30)
     apellido = CharField(max_length=30)
     email = EmailField()
     profesion = CharField(max_length=30)

class Entregables(Model):
    nombre = CharField(max_length=30)
    fecha_de_entrega = DateField()
    entregado = BooleanField()
    