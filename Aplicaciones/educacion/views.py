from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.
from django.shortcuts import render
from.models import Contacto

# Create your views here.
def home(request):
    return render(request,'home.html')

def contacto(request):
    cargos = Contacto.objects.all()  # O el modelo correcto
    return render(request, 'contacto.html', {'cargos': cargos})

def nuevoContacto(request):
    return render(request,'nuevoContacto.html')

#almacenado los datos de nuevo contacto
def guardarContacto(request):

    nombre=request.POST["nombre"]
    descripcion=request.POST["descripcion"]
    funciones=request.POST["funciones"]
    horario=request.POST["horario"]
    sueldo=request.POST["sueldo"].replace(',',',')
    #subiendo archivos con parentesis
    logo=request.FILES.get("logo")
    
    nuevoContacto=Contacto.objects.create(nombre=nombre, descripcion=descripcion,funciones=funciones, horario=horario, sueldo=sueldo, logo=logo)

    #MENSAAJE DE CONFIRMACION
    messages.success(request,"Contacto guardado exitosamente")
    return redirect('contacto')


def eliminarContacto (request,id):
    contactoEliminar=Contacto.objects.get(id=id)
    contactoEliminar.delete()
    #MENSAJE DE ACEPTCION
    
    return redirect('contacto')  


def editarContacto(request,id):
    cargoEditar=Contacto.objects.get(id=id)
    return render(request,"editarContacto.html", {'cargoEditar':cargoEditar})


def procesarEdicionContacto(request):
    id=request.POST["id"]
    nombre=request.POST["nombre"]
    descripcion=request.POST["descripcion"]
    funciones=request.POST["funciones"]
    horario=request.POST["horario"]
    sueldo=request.POST["sueldo"].replace(',',',')
    logo = request.FILES.get("logo")
    contacto=Contacto.objects.get(id=id)#buscando el cargo a editar por ID
    contacto.nombre=nombre
    contacto.descripcion=descripcion
    contacto.funciones=funciones
    contacto.horario=horario
    contacto.sueldo=sueldo
    if request.FILES.get("logo"):
         contacto.logo = request.FILES["logo"]
    contacto.save()
    #mensaje de confirmacion
    messages.success(request,"Cargo actualizado exitosamente")
    return redirect('contacto')


    #TABLAS

    from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Estudiante, Docente, Curso, Matricula

# --- Estudiante ---

def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes.html', {'estudiantes': estudiantes})

def nuevoEstudiante(request):
    return render(request, 'nuevoEstudiante.html')

def guardarEstudiante(request):
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    fecha_nacimiento = request.POST["fecha_nacimiento"]
    correo_electronico = request.POST["correo_electronico"]
    telefono = request.POST["telefono"]

    Estudiante.objects.create(
        nombre=nombre,
        apellido=apellido,
        fecha_nacimiento=fecha_nacimiento,
        correo_electronico=correo_electronico,
        telefono=telefono
    )
    messages.success(request, "Estudiante guardado exitosamente")
    return redirect('estudiantes')

def eliminarEstudiante(request, id_estudiante):
    estudiante = get_object_or_404(Estudiante, id_estudiante=id_estudiante)
    estudiante.delete()
    messages.success(request, "Estudiante eliminado exitosamente")
    return redirect('estudiantes')

def editarEstudiante(request, id_estudiante):
    estudiante = get_object_or_404(Estudiante, id_estudiante=id_estudiante)
    return render(request, 'editarEstudiante.html', {'estudiante': estudiante})

def procesarEdicionEstudiante(request):
    id_estudiante = request.POST["id_estudiante"]
    estudiante = get_object_or_404(Estudiante, id_estudiante=id_estudiante)

    estudiante.nombre = request.POST["nombre"]
    estudiante.apellido = request.POST["apellido"]
    estudiante.fecha_nacimiento = request.POST["fecha_nacimiento"]
    estudiante.correo_electronico = request.POST["correo_electronico"]
    estudiante.telefono = request.POST["telefono"]
    estudiante.save()

    messages.success(request, "Estudiante actualizado exitosamente")
    return redirect('estudiantes')

# --- Docente ---

def docentes(request):
    docentes = Docente.objects.all()
    return render(request, 'docentes.html', {'docentes': docentes})

def nuevoDocente(request):
    return render(request, 'nuevoDocente.html')

def guardarDocente(request):
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    especialidad = request.POST["especialidad"]
    correo_electronico = request.POST["correo_electronico"]
    telefono = request.POST["telefono"]

    Docente.objects.create(
        nombre=nombre,
        apellido=apellido,
        especialidad=especialidad,
        correo_electronico=correo_electronico,
        telefono=telefono
    )
    messages.success(request, "Docente guardado exitosamente")
    return redirect('docentes')

def eliminarDocente(request, id_docente):
    docente = get_object_or_404(Docente, id_docente=id_docente)
    docente.delete()
    messages.success(request, "Docente eliminado exitosamente")
    return redirect('docentes')

def editarDocente(request, id_docente):
    docente = get_object_or_404(Docente, id_docente=id_docente)
    return render(request, 'editarDocente.html', {'docente': docente})

def procesarEdicionDocente(request):
    id_docente = request.POST["id_docente"]
    docente = get_object_or_404(Docente, id_docente=id_docente)

    docente.nombre = request.POST["nombre"]
    docente.apellido = request.POST["apellido"]
    docente.especialidad = request.POST["especialidad"]
    docente.correo_electronico = request.POST["correo_electronico"]
    docente.telefono = request.POST["telefono"]
    docente.save()

    messages.success(request, "Docente actualizado exitosamente")
    return redirect('docentes')

# --- Curso ---

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})

def nuevoCurso(request):
    docentes = Docente.objects.all()  # Para seleccionar docente al crear curso
    return render(request, 'nuevoCurso.html', {'docentes': docentes})

def guardarCurso(request):
    nombre_curso = request.POST["nombre_curso"]
    descripcion = request.POST["descripcion"]
    id_docente = request.POST["id_docente"]
    creditos = request.POST["creditos"]

    docente = get_object_or_404(Docente, id_docente=id_docente)

    Curso.objects.create(
        nombre_curso=nombre_curso,
        descripcion=descripcion,
        id_docente=docente,
        creditos=creditos
    )
    messages.success(request, "Curso guardado exitosamente")
    return redirect('cursos')

def eliminarCurso(request, id_curso):
    curso = get_object_or_404(Curso, id_curso=id_curso)
    curso.delete()
    messages.success(request, "Curso eliminado exitosamente")
    return redirect('cursos')

def editarCurso(request, id_curso):
    curso = get_object_or_404(Curso, id_curso=id_curso)
    docentes = Docente.objects.all()
    return render(request, 'editarCurso.html', {'curso': curso, 'docentes': docentes})

def procesarEdicionCurso(request):
    id_curso = request.POST["id_curso"]
    curso = get_object_or_404(Curso, id_curso=id_curso)

    curso.nombre_curso = request.POST["nombre_curso"]
    curso.descripcion = request.POST["descripcion"]
    id_docente = request.POST["id_docente"]
    curso.id_docente = get_object_or_404(Docente, id_docente=id_docente)
    curso.creditos = request.POST["creditos"]
    curso.save()

    messages.success(request, "Curso actualizado exitosamente")
    return redirect('cursos')

# --- Matricula ---

def matriculas(request):
    matriculas = Matricula.objects.select_related('id_estudiante', 'id_curso').all()
    return render(request, 'matriculas.html', {'matriculas': matriculas})

def nuevaMatricula(request):
    estudiantes = Estudiante.objects.all()
    cursos = Curso.objects.all()
    return render(request, 'nuevaMatricula.html', {'estudiantes': estudiantes, 'cursos': cursos})

def guardarMatricula(request):
    id_estudiante = request.POST["id_estudiante"]
    id_curso = request.POST["id_curso"]
    fecha_matricula = request.POST["fecha_matricula"]
    estado = request.POST["estado"]

    estudiante = get_object_or_404(Estudiante, id_estudiante=id_estudiante)
    curso = get_object_or_404(Curso, id_curso=id_curso)

    Matricula.objects.create(
        id_estudiante=estudiante,
        id_curso=curso,
        fecha_matricula=fecha_matricula,
        estado=estado
    )
    messages.success(request, "Matrícula guardada exitosamente")
    return redirect('matriculas')

def eliminarMatricula(request, id_matricula):
    matricula = get_object_or_404(Matricula, id_matricula=id_matricula)
    matricula.delete()
    messages.success(request, "Matrícula eliminada exitosamente")
    return redirect('matriculas')

def editarMatricula(request, id_matricula):
    matricula = get_object_or_404(Matricula, id_matricula=id_matricula)
    estudiantes = Estudiante.objects.all()
    cursos = Curso.objects.all()
    estados = ['activo', 'inactivo', 'cancelado']
    return render(request, 'editarMatricula.html', {
        'matricula': matricula,
        'estudiantes': estudiantes,
        'cursos': cursos,
        'estados': estados
    })

def procesarEdicionMatricula(request):
    id_matricula = request.POST["id_matricula"]
    matricula = get_object_or_404(Matricula, id_matricula=id_matricula)

    id_estudiante = request.POST["id_estudiante"]
    id_curso = request.POST["id_curso"]
    fecha_matricula = request.POST["fecha_matricula"]
    estado = request.POST["estado"]

    matricula.id_estudiante = get_object_or_404(Estudiante, id_estudiante=id_estudiante)
    matricula.id_curso = get_object_or_404(Curso, id_curso=id_curso)
    matricula.fecha_matricula = fecha_matricula
    matricula.estado = estado
    matricula.save()

    messages.success(request, "Matrícula actualizada exitosamente")
    return redirect('matriculas')
