

from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
    def __str__(self):
        return "Grupo de estudiantes: "+ self._grupo

    def listadoAsignaturas(self, **kwargs):
        if self._asignaturas is not None:
            for x in kwargs:
                self._asignaturas.append(kwargs[x])
        else:
            self._asignaturas=[]
            for x in kwargs:
                self._asignaturas.append(kwargs[x])


    def agregarAlumno(self, alumno, lista=None):
        if(lista is None):
            if self.listadoAlumnos is None:
                self.listadoAlumnos= [alumno]
            else:
                self.listadoAlumnos = self.listadoAlumnos + [alumno]
        else:
            if self.listadoAlumnos is None:
                self.listadoAlumnos = lista
                self.listadoAlumnos.append(alumno)
            else:
                self.listadoAlumnos = self.listadoAlumnos + lista
                self.listadoAlumnos.append(alumno)

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    
