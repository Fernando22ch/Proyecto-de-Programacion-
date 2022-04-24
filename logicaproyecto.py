#snakecase
from sre_constants import JUMP
from time import sleep
from hashlib import md5
from getpass import getpass
import datetime as dt
from xmlrpc.server import SimpleXMLRPCDispatcher
usuario_momentaneo=''





def limpiar_terminal():
    print (chr(27) + "[2J")
def cifrar (entrada):
    entrada_binaria=entrada.encode('ascii')
    resultado = md5(entrada_binaria)
    return (resultado.hexdigest())

def obtener_clave(mensaje):
    pswd = getpass(mensaje+": ")
    return (pswd)

usuarios_estudiante=[{'Nombre':'Jeison Blanco Rojas', 'Carrera':'computacion', 'autenticacion':{'usuario':'jeisonb1','contraseña':'3e47c3e9bf25d1058ad95b4d9f5d0281'},
'cursos_matriculados':[{'nombre':'taller de programacion','estado': ''}, {'nombre':'introduccion a la programacion','estado': ''}], 'actividades':{'futbol':{'dia':'lunes','horas':'4'}}}]

usuarios_admin=[{'Nombre':'Fernando Chaves Calvo', 'telefono':'83220200', 'autenticacion':{'usuario':'admin','contraseña':'21232f297a57a5a743894a0e4a801fc3'}}]
def registrar_estudiante():
    limpiar_terminal()
    nuevo_estudiante = dict()
    nuevo_estudiante['Nombre'] = input("Nombre: ")
    nuevo_estudiante['Carrera'] = input("Carrera: ")
    nuevo_estudiante['cursos_matriculados']=[]

    print("Autenticacion")
    usuario = input("\tNombre de usuario: ")
    contraseña = cifrar(obtener_clave("Digite su contraseña: "))
    nuevo_estudiante['autenticacion'] = {'usuario':usuario, 'contraseña': contraseña}
    usuarios_estudiante.append(nuevo_estudiante)



def registrar_admin():

    limpiar_terminal()
    nuevo_admin=dict()
    nuevo_admin['Nombre']=input("Nombre: ")
    nuevo_admin['Telefono']=input("telefono: ")

    print("Autenticacion")
    usuario=input ("\t Nombre de usuario: ")
    contraseña=cifrar(obtener_clave("\t Digite su contraseña: "))


    nuevo_admin['autenticacion']={'usuario':usuario, 'contraseña': contraseña}
    usuarios_admin.append(nuevo_admin)


def validar_estudiante(usuario,contraseña):
    global usuario_momentaneo
    resp=False
    contraseña=cifrar(contraseña)
    for value in usuarios_estudiante:
        
        if value['autenticacion']['usuario']==usuario and value['autenticacion']['contraseña']==contraseña:
            resp=True
            usuario_momentaneo=(value)
            break
    return(resp)

def validar_admin(usuario,contraseña):
    resp=False
    contraseña=cifrar(contraseña)
    for value in usuarios_admin:
        
        if value['autenticacion']['usuario']==usuario and value['autenticacion']['contraseña']==contraseña:
            resp=True
            break
    return(resp)


    

cursos=[{'nombre': 'taller de programacion','creditos':'3','horas totales de dedicacion': 9,'horas lectivas':'3','inicia': dt.time(8,00,00),'finaliza':dt.time(11,00,00),'dia de clases':'martes','carreras':'computacion'},
{'nombre':'introduccion a la programacion','creditos':'3','horas totales de dedicacion': 9,'horas lectivas':'3','inicia': dt.time(8,00,00),'finaliza':dt.time(11,00,00),'dia de clases':'lunes','carreras':'computacion'}]

# funciones para los administradores
def registros_de_cursos():
    curso_nuevo=dict()
    
    curso_nuevo['nombre']=c=input("Nombre del curso: ")
    
    curso_nuevo['creditos']=int(input("creditos: "))
    curso_nuevo['horas lectivas']=int(input("horas lectivas: "))
    hora_i=(input("Hora de inicio: "))
    curso_nuevo['inicia']=dt.time(int(hora_i),0,0)
    hora_f=(input("Hora de finalizacion : "))
    curso_nuevo['finaliza']=dt.time(int(hora_f),0,0)
    curso_nuevo['dia de clases']=input("dia del curso: ")
    curso_nuevo['horas totales de dedicacion']=input("horas totales de dedicacion: ")
    curso_nuevo['carreras']=carre=input("carreras que pertenece el curso: ")
    cursos.append(curso_nuevo)

    # for carrera in carerras_cursos:
    #     if carrera['nombre']==carre:
    #          carerras_cursos['cursos_esp']=list
    #          carerras_cursos['cursos_esp']+=c
   
carerras_cursos=[{'nombre':'computacion','cursos_esp':['taller de programacion','introduccion a la programacion']}]
carreras={'computacion','agronomia'}

def registros_de_carreras():
    limpiar_terminal()
    print("Carreras existentes:")   
    print(carreras)
    carre_nueva=(input("Nombre de la carrera: "))
    carreras.add(carre_nueva)

   # carerras_cursos.append['nombre']=(carre_nueva)




# funciones para los estudiantes 

def cambiar_carrera():
    global usuario_momentaneo
    limpiar_terminal()
    carreranueva= input("nueva carrera:" )

    for x in usuarios_estudiante:
        if x['Nombre']==usuario_momentaneo['Nombre']:
            x['Carrera']=carreranueva
            x['cursos matriculados']=[]
            

def matricular_cursos():
    limpiar_terminal()
    global usuario_momentaneo
    print("Cursos disponibles")
    print(cursos)
    a_matricular = input("Escriba el nombre del curso que desea matricular:")
    resp=False
    for curso in cursos:
        if curso['nombre']==a_matricular:
            if curso['carreras'] == usuario_momentaneo['Carrera']:     
                if len(usuario_momentaneo['cursos_matriculados']) > 0:
                    for curso_M in usuario_momentaneo['cursos_matriculados']:
                        if curso_M['nombre']==a_matricular:
                            print("Curso ya matriculado")
                            resp=True
                            break
                    if not resp:
                        curso_nuevo={'nombre':a_matricular,'estado':''}
                        usuario_momentaneo['cursos_matriculados'].append(curso_nuevo)
                else:
                    curso_nuevo={'nombre':a_matricular,'estado':''}
                    usuario_momentaneo['cursos_matriculados'].append(curso_nuevo)
            else:
                print("Curso de otra carrera")
    else:
        print("Curso invalido")


def aprobar_reprobar_cursos():
    limpiar_terminal()
    global usuario_momentaneo
    for x in usuarios_estudiante:
        
        if x['Nombre'] == usuario_momentaneo['Nombre']:
            print(x['cursos_matriculados'])
            curso_modificar = input("Cual curso desea modificar el estado:")
            for curso_matri in x['cursos_matriculados']:
                if curso_matri['nombre']==curso_modificar:
                    curso_matri['estado']=input("Curso aprobado o reprobado:")
            # for curso in cursos:
            #     if curso['carreras'] == x['Carrera'] and x['cursos_matriculados'] == curso_modificar:
            #         x['cursos_matriculados'][curso_modificar]['estado']= estado = input("Curso aprobado o reprobado:")
                else:
                    print("Curso Incorrecto o no matriculado")



#erroresd
def calendario():

    lunes=[]
    martes=[]
    miercoles=[]
    jueves=[]
    viernes=[]
    sabado=[]
    domingo=[]
   
    for x in usuarios_estudiante:
        if x['Nombre'] == usuario_momentaneo['Nombre']:
            curso_pendiente=x['cursos_matriculados']
            for y in curso_pendiente:
                if y['estado']=='':
                    for curso in cursos:
                        if curso['nombre']==y['nombre']:
                            dia=curso['dia de clases']
                            if dia=='lunes':

                                lunes.append(curso['nombre'])
                                lunes.append(curso['inicia'])
                                lunes.append(curso['finaliza'])
                                break
                            elif dia=='martes':
                                martes.append(curso['nombre'])
                                martes.append(curso['inicia'])
                                martes.append(curso['finaliza'])
                                break
                            elif dia=='miercoles':
                                miercoles.append(curso['nombre'])
                                miercoles.append(curso['inicia'])
                                miercoles.append(curso['finaliza'])
                                break
                            elif dia=='jueves':
                                jueves.append(curso['nombre'])
                                jueves.append(curso['inicia'])
                                jueves.append(curso['finaliza'])
                                break
                            elif dia=='viernes':
                                viernes.append(curso['nombre'])
                                viernes.append(curso['inicia'])
                                viernes.append(curso['finaliza'])
                                break
                            elif dia=='sabado':
                                sabado.append(curso['nombre'])
                                sabado.append(curso['inicia'])
                                sabado.append(curso['finaliza'])
                                break
                            elif dia=='domingo':
                                domingo.append(curso['nombre'])
                                domingo.append(curso['inicia'])
                                domingo.append(curso['finaliza'])
                                break
    limpiar_terminal()
    #aqui va registrar actividades que modifica las listas ya creadas que tambien tienen cursos
    print("Lunes:")
    print(lunes)
    print("Martes:")
    print(martes)
    print("Miercoles:")
    print(miercoles)
    print("Jueves:")
    print(jueves)
    print("Viernes:")
    print(viernes)
    print("Sabado:")
    print(sabado)
    print("Domingo:")
    print(domingo)
    opptt=input("Envie 1 tecla para regresar al menu:")        
    if opptt==1:
        JUMP 

                       







        




# '''             prueba de funciones 
# '''
