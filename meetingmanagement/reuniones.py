# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from models import *
from forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import datetime
import linecache
import sys, os
reload(sys)
sys.setdefaultencoding('utf8')

#Funcion V2.0
def ir_detalle_proyecto(request, id_proyecto, acta_id = None):
    #Variables para el panel
    proyecto = Proyecto.objects.get(id=id_proyecto)
    listas_actas = Acta.objects.filter(proyecto_acta=Proyecto.objects.get(id=id_proyecto)).order_by('fecha_acta')
    usuarios_proyecto = Usuario_Proyecto.objects.filter(proyecto=proyecto)

    if not acta_id:
        try:
            acta = listas_actas[0]
            acta_seleccionada = acta.id
        except KeyError:
            acta = None
            acta_seleccionada = None

    #Capturamos todos los compromisos activos (no eliminados)
    elementos_activos = []
    numeraciones = []
    num_acta = 0
    num_elemento = 0
    for ac in listas_actas:
        fecha_acta = ac.fecha_acta
        num_acta = num_acta+1
        for tema in ac.tema_set.all():
            for elemento in tema.elemento_set.all():
                num_elemento = num_elemento + 1
                if elemento.tipo_elemento == "Compromiso":
                        if elemento.estado_elemento != "Eliminado" and elemento.estado_elemento != "Completado":
                            #Si elemento no tiene fecha inicio, no se considera como activo
                            numeracion = str(num_acta)+"."+str(num_elemento)
                            numeraciones.append(numeracion)
                            elementos_activos.append(elemento)
    #Ahora que tenemos los CO activos, para cada acta seleccionamso aquellos que no sean de una reunión futura
    """
    for ac in listas_actas:
        for elemento in elementos_activos:
            if elemento.fecha_inicio is not None:
                if elemento.fecha_inicio < ac.fecha_acta:
    """

    #Variables para el tablero kanban
    actas_con_tema = []
    for ac in listas_actas:
        if len(ac.tema_set.all())>0: #Si el acta tiene temas, se agrega a la lista
            actas_con_tema.append(ac)
    #Compromisos que no tienen temas (es decir, fueron agregados directamente al tablero kanban)
    tareas = Elemento.objects.filter(tipo_elemento='Compromiso')

    #Revisamos si usuario logueado es jefe. Si es jefe, se añaden todas las actas como editables
    es_jefe = False
    usuario_logueado = Usuario.objects.get(user=User.objects.get(username=request.user.username))
    user_proyecto_logueado = Usuario_Proyecto.objects.get(proyecto=proyecto, usuario=usuario_logueado)
    if user_proyecto_logueado.rol_proyecto == "Jefe":
        es_jefe = True
    temas_acta = Tema.objects.filter(acta_tema=acta)

    elementos_tema = Elemento.objects.filter(tema__in=temas_acta)
    data = {
        'acta_seleccionada':acta_seleccionada,
        'es_jefe':es_jefe,
        'tareas':tareas,
        'actas_con_tema':actas_con_tema,
        'temas_acta':temas_acta,
        'elementos_tema':elementos_tema,
        'total_compromisos_activos': zip(elementos_activos, numeraciones),  #Esto es para poder iterar sobre las dos listas en un for
        'cantidad_actas_proyecto' : len(listas_actas)+1, #Esto es para la numeración de los elementos. Para ello, se le suma 1 adicional, pues la siguiente acta deberá ser la cant_actas+1.
        'proyecto' : proyecto,
        'usuarios_proyecto' : usuarios_proyecto,
        'listas_actas' : listas_actas,
        'acta' : acta
    }
    return render(request, 'walo-template/proyectos/reuniones/panel_proyecto.html', data)
