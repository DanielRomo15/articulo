from django.urls import path
from . import views 
urlpatterns = [
    path('',views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('contacto/nuevoContacto/', views.nuevoContacto, name='nuevoContacto'),
    path('contacto/nuevoContacto/guardarContacto',views.guardarContacto, name='guardarContacto'),
    path('contacto/eliminarContacto/<id>', views.eliminarContacto, name='eliminarContacto'),
    path('contacto/editarContacto/<id>', views.editarContacto, name='editarContacto'),
    path('contacto/procesarEdicionContacto/', views.procesarEdicionContacto, name='procesarEdicionContacto'),
    # Estudiantes
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('estudiantes/nuevoEstudiante/', views.nuevoEstudiante, name='nuevoEstudiante'),
    path('estudiantes/guardarEstudiante/', views.guardarEstudiante, name='guardarEstudiante'),
    path('estudiantes/eliminarEstudiante/<int:id_estudiante>/', views.eliminarEstudiante, name='eliminarEstudiante'),
    path('estudiantes/editarEstudiante/<int:id_estudiante>/', views.editarEstudiante, name='editarEstudiante'),
    path('estudiantes/procesarEdicionEstudiante/', views.procesarEdicionEstudiante, name='procesarEdicionEstudiante'),

    # Docentes
    path('docentes/', views.docentes, name='docentes'),
    path('docentes/nuevoDocente/', views.nuevoDocente, name='nuevoDocente'),
    path('docentes/guardarDocente/', views.guardarDocente, name='guardarDocente'),
    path('docentes/eliminarDocente/<int:id_docente>/', views.eliminarDocente, name='eliminarDocente'),
    path('docentes/editarDocente/<int:id_docente>/', views.editarDocente, name='editarDocente'),
    path('docentes/procesarEdicionDocente/', views.procesarEdicionDocente, name='procesarEdicionDocente'),

    # Cursos
    path('cursos/', views.cursos, name='cursos'),
    path('cursos/nuevoCurso/', views.nuevoCurso, name='nuevoCurso'),
    path('cursos/guardarCurso/', views.guardarCurso, name='guardarCurso'),
    path('cursos/eliminarCurso/<int:id_curso>/', views.eliminarCurso, name='eliminarCurso'),
    path('cursos/editarCurso/<int:id_curso>/', views.editarCurso, name='editarCurso'),
    path('cursos/procesarEdicionCurso/', views.procesarEdicionCurso, name='procesarEdicionCurso'),

    # Matrículas
    path('matriculas/', views.matriculas, name='matriculas'),
    path('matriculas/nuevaMatricula/', views.nuevaMatricula, name='nuevaMatricula'),
    path('matriculas/guardarMatricula/', views.guardarMatricula, name='guardarMatricula'),
    path('matriculas/eliminarMatricula/<int:id_matricula>/', views.eliminarMatricula, name='eliminarMatricula'),
    path('matriculas/editarMatricula/<int:id_matricula>/', views.editarMatricula, name='editarMatricula'),
    path('matriculas/procesarEdicionMatricula/', views.procesarEdicionMatricula, name='procesarEdicionMatricula'),

]
