#snakecase
usuario_momentaneo=""
from time import sleep

from hashlib import md5
from getpass import getpass
from typing import cast
def us_momentaneo(nombre):
    usuario_momentaneo=nombre




def limpiar_terminal():
    print (chr(27) + "[2J")
def cifrar (entrada):
    entrada_binaria=entrada.encode('ascii')
    resultado = md5(entrada_binaria)
    return (resultado.hexdigest())

def obtener_clave(mensaje):
    pswd = getpass(mensaje+": ")
    return (pswd)

usuarios_estudiante=[{'id':1 ,'Nombre':'Jeison Blanco Rojas', 'Carrera':'computacion', 'autenticacion':{'usuario':'jeisonb1','contraseña':'jei123'},
'cursos_matriculados': {'taller de programacion': '','introduccion a la programacion':'reprobado'}, 'actividades':{'futbol':{'dia':'lunes','horas':'4'}}}]

usuarios_admin=[{'id':1,'Nombre':'Fernando Chaves Calvo', 'telefono':'83220200', 'autenticacion':{'usuario':'admin','contraseña':'admin'}}]
def registrar_estudiante():
    limpiar_terminal()
    nuevo_estudiante = dict()
    nuevo_estudiante['Nombre'] = input("Nombre: ")
    nuevo_estudiante['Carrera'] = input("Carrera: ")

    print("Autenticacion")
    usuario = input("\tNombre de usuario: ")
    contraseña = cifrar(obtener_clave("Digite su contraseña: "))
    nuevo_estudiante['autenticacion'] = {'usuario':usuario, 'contraseña': contraseña}
    usuarios_estudiante.append(nuevo_estudiante)



def registrar_admin():

    limpiar_terminal
    nuevo_admin=dict()
    nuevo_admin['Nombre']=input("Nombre: ")
    nuevo_admin['Telefono']=input("telefono: ")

    print("Autenticacion")
    usuario=input ("\tNombre de usuario: ")
    contraseña=cifrar(obtener_clave("Digite su contraseña: "))


    nuevo_admin['autenticacion']={'usuario':usuario, 'contraseña': contraseña}
    usuarios_admin.append(nuevo_admin)


def validar_estudiante(usuario,contraseña):
    
    resp=False
    for value in usuarios_estudiante:
        if value['autenticacion']['usuario']==usuario and value['autenticacion']['contraseña']==contraseña:
            resp=True
            us_momentaneo(value['Nombre'])
            break
    return(resp)
def validar_admin(usuario,contraseña):
    resp=False
    for value in usuarios_admin:
        if value['autenticacion']['usuario']==usuario and value['autenticacion']['contraseña']==contraseña:
            resp=True
            break
    return(resp)


    

cursos=[{'nombre': 'taller de programacion','creditos':'2','horas lectivas':'3','inicia':'07-02-22','finaliza':'23-06-22','horario de clases':'Jueves y viernes a las 5pm','carreras':'computacion'}]
def registros_de_cursos():
    curso_nuevo=dict()
    
    curso_nuevo['nombre']=c=input("Nombre del curso: ")
    
    curso_nuevo['creditos']=int(input("creditos: "))
    curso_nuevo['horas lectivas']=int(input("horas lectivas: "))
    curso_nuevo['inicia']=input ("fecha de inicio del curso: ")
    curso_nuevo['finaliza']=input ("fecha de finalizacion del curso: ")
    curso_nuevo['horario de clases']=input("horarios del curso: ")
    curso_nuevo['carreras']=carre=input("carreras que pertenece el curso: ")
    cursos.append(curso_nuevo)
    for value in carerras_cursos:
        if value['nombre']==carre:
            carerras_cursos['cursos_esp']+=c
   
carerras_cursos=[{'nombre':'computacion','cursos_esp':['taller de programacion','introduccion a la programacion']}]
carreras={'computacion',"agronomia"}
def registros_de_carreras():
    print("Carreras existentes:")   
    print(carreras)
    carre_nueva=(input("Nombre de la carrera: "))
    carreras.add(carre_nueva)
    carerras_cursos.append(carre_nueva)

def cambiar_carrera():
    
    carreranueva= input("nueva carrera:" )

    for x in usuarios_estudiante:
        if x['Nombre']==usuario_momentaneo:
            x['Carrera']=carreranueva
            x['cursos matriculados']=[]
            

    

def matricular_cursos():
    global usuario_momentaneo
    a_matricular = input("Cual curso desea matricular:")
    for x in usuarios_estudiante:
        if x['Nombre'] == usuario_momentaneo:
            for curso in cursos:
                if curso['carreras'] == x['Carrera']:
                    x['cursos_matriculados'][a_matricular] = ""




        




'''             prueba de funciones 
'''
