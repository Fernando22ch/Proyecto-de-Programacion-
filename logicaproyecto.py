#snakecase
from sre_constants import JUMP
from time import sleep
from hashlib import md5
from getpass import getpass
import datetime as dt


usuario_momentaneo=''    #usuario momentaneo para tener toda la informacion del estudiante que inicio sesion





def limpiar_terminal():
    print (chr(27) + "[2J")
def cifrar (entrada):                               # funcion para convertir la contraseña en una cifrada
    entrada_binaria=entrada.encode('ascii')
    resultado = md5(entrada_binaria)
    return (resultado.hexdigest())

def obtener_clave(mensaje):          #funcion que privatiza la contraseña al escribirla
    pswd = getpass(mensaje+": ")
    return (pswd)

usuarios_estudiante=[{'Nombre':'Jeison Blanco Rojas', 'Carrera':'computacion',      #listado de estudiantes registrados
'autenticacion':{'usuario':'jeisonb1','contraseña':'3e47c3e9bf25d1058ad95b4d9f5d0281'},
'cursos_matriculados':[{'nombre':'taller de programacion','estado': ''}, {'nombre':'introduccion a la programacion','estado': ''}], 
'actividades':[{'nombre':'Repaso de syntaxis de programacion','curso':'taller de programacion','dia':'jueves','h_inicio':dt.time(17,00,00),'h_final':dt.time(20,00,00),'estado':''}]}]

usuarios_admin=[{'Nombre':'Fernando Chaves Calvo', 'telefono':'83220200',  #listado de administradores registrados
'autenticacion':{'usuario':'admin','contraseña':'21232f297a57a5a743894a0e4a801fc3'}}]


def registrar_estudiante():       #obtiene los datos del estudiante para despues agregarlo
    limpiar_terminal()
    nuevo_estudiante = dict()
    nuevo_estudiante['Nombre'] = input("Nombre: ")
    nuevo_estudiante['Carrera'] = input("Carrera: ")
    nuevo_estudiante['cursos_matriculados']=[]
    nuevo_estudiante['actividades']=[]
    print("Autenticacion")
    usuario = input("\tNombre de usuario: ")
    contraseña = cifrar(obtener_clave("Digite su contraseña: "))
    nuevo_estudiante['autenticacion'] = {'usuario':usuario, 'contraseña': contraseña}
    usuarios_estudiante.append(nuevo_estudiante)



def registrar_admin():        #obtiene los datos del administrador para despues agregarlo

    limpiar_terminal()
    nuevo_admin=dict()
    nuevo_admin['Nombre']=input("Nombre: ")
    nuevo_admin['Telefono']=input("telefono: ")

    print("Autenticacion")
    usuario=input ("\t Nombre de usuario: ")
    contraseña=cifrar(obtener_clave("\t Digite su contraseña: "))


    nuevo_admin['autenticacion']={'usuario':usuario, 'contraseña': contraseña}
    usuarios_admin.append(nuevo_admin)


def validar_estudiante(usuario,contraseña):     #funcion que verifica si las entradas del inicio de sesion del estudiante, existen.
    global usuario_momentaneo
    resp=False
    contraseña=cifrar(contraseña)
    for value in usuarios_estudiante:
        
        if value['autenticacion']['usuario']==usuario and value['autenticacion']['contraseña']==contraseña:
            resp=True
            usuario_momentaneo=(value)
            break
    return(resp)

def validar_admin(usuario,contraseña):      #funcion que verifica si las entradas del inicio de sesion del administrador, existen.
    resp=False
    contraseña=cifrar(contraseña)
    for value in usuarios_admin:
        
        if value['autenticacion']['usuario']==usuario and value['autenticacion']['contraseña']==contraseña:
            resp=True
            break
    return(resp)


    
# listado de cursos disponibles con sus respectivos datos
cursos=[{'nombre': 'taller de programacion','creditos':'3','horas totales de dedicacion': 9,'horas lectivas':'3','inicia': dt.time(8,00,),'finaliza':dt.time(11,00,),'dia de clases':'martes','carreras':'computacion'},
{'nombre':'introduccion a la programacion','creditos':'3','horas totales de dedicacion': 9,'horas lectivas':'3','inicia': dt.time(8,00,),'finaliza':dt.time(11,00,),'dia de clases':'lunes','carreras':'computacion'}]

# funciones para los administradores
def registros_de_cursos():   #registra los datos dados por el administrador para crear y agregar un curso
    curso_nuevo=dict()
    
    curso_nuevo['nombre']=input("Nombre del curso: ")
    
    curso_nuevo['creditos']=int(input("creditos: "))
    curso_nuevo['horas lectivas']=int(input("horas lectivas: "))
    hora_i=(input("Hora de inicio: "))
    curso_nuevo['inicia']=dt.time(int(hora_i),0,0)
    hora_f=(input("Hora de finalizacion : "))
    curso_nuevo['finaliza']=dt.time(int(hora_f),0,0)
    curso_nuevo['dia de clases']=input("dia del curso: ")
    curso_nuevo['horas totales de dedicacion']=input("horas totales de dedicacion: ")
    curso_nuevo['carreras']=input("carreras que pertenece el curso: ")
    cursos.append(curso_nuevo)

    
   
carerras_cursos=[{'nombre':'computacion','cursos_esp':['taller de programacion','introduccion a la programacion']}]
carreras={'computacion','agronomia'} #listado de carreras disponibles

def registros_de_carreras():    #registra los datos dados por el administrador para crear y agregar una carrera
    limpiar_terminal()
    print("Carreras existentes:")   
    print(carreras)
    carre_nueva=(input("Nombre de la carrera: "))
    carreras.add(carre_nueva)






# funciones para los estudiantes 

def cambiar_carrera():    #el estudiante, puede cambiar su carrera, asi mismo los cursos matriculados 
    global usuario_momentaneo
    limpiar_terminal()
    carreranueva= input("nueva carrera:" )

    for x in usuarios_estudiante:
        if x['Nombre']==usuario_momentaneo['Nombre']:
            x['Carrera']=carreranueva
            x['cursos matriculados']=[]
            

def matricular_cursos():     #el estudiante, puede matricular cursos que previamente se agreguen
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


def aprobar_reprobar_cursos():    #el estudiante, puede cambiar el estado de un curso, dejandolo invalido si es aprobado o reprobado
    limpiar_terminal()
    global usuario_momentaneo
    for x in usuarios_estudiante:
        
        if x['Nombre'] == usuario_momentaneo['Nombre']:
            print(x['cursos_matriculados'])
            curso_modificar = input("Cual curso desea modificar el estado:")
            for curso_matri in x['cursos_matriculados']:
                if curso_matri['nombre']==curso_modificar:
                    curso_matri['estado']=input("Curso aprobado o reprobado:")
         
                else:
                    print("Curso Incorrecto o no matriculado")

def menu_registro_de_actividades():     #menu para que el estudiante registre las actividades que quiera
    limpiar_terminal()
    global usuario_momentaneo   
    nueva_actividad={}
    nueva_actividad['estado']='' 

    nueva_actividad ['nombre']=input('Cual es el nombre de la actividad:')
    nueva_actividad ['curso']=input('si pertenece a algun curso escribalo,si no dejelo en blanco:')
    nueva_actividad ['dia']=input('Que dia es la actividad:')
    hora_inicio=(input("Hora de inicio: "))
    nueva_actividad ['h_inicio']=dt.time(int(hora_inicio),0)
    hora_final=(input("Hora de finalizacion: "))
    nueva_actividad ['h_final']=dt.time(int(hora_final),0)
    for curso in usuario_momentaneo ['cursos_matriculados']:
        if curso['nombre']==nueva_actividad['curso']:
            if curso['estado']=='': 
                  insertar_actividad(nueva_actividad,usuario_momentaneo['actividades'])
            else:
                print("error: curso ya aprobado o reprobado")
        else:
            print("error: actividad no relacionada a ningun curso matriculado")
            
            
        


    
def choque_horario (fi1,ff1,fi2,ff2):       #revisa 2 fechas de inicio y 2 finales para retornar su existe un choque
    return ((fi2>=fi1 and fi2<=ff1)or(ff2>=fi1 and ff2<=ff1))

def insertar_actividad (nueva_actividad,actividad): #comprueba si una actividad a registrar no choca con alguna ya registrada
    choque=False
    if len(usuario_momentaneo['actividades'])>0:
        for actividad in usuario_momentaneo['actividades']:
            if actividad['estado']=='':
                if actividad['dia']==nueva_actividad['dia']:
                
                 if choque_horario(fi1=actividad['h_inicio'],ff1=actividad['h_final'],fi2=nueva_actividad['h_inicio'],ff2=nueva_actividad['h_final']):
                    choque=True
                    break
        if not choque: 
            usuario_momentaneo['actividades'].append(nueva_actividad)
            print ("se agrego la actividad")
        else:
            print ("No se agrega por choque de horarios")
    else:
        return (choque)


def calendario(): #impresion de todos los datos guardado en sus respectivos horarios.

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
            actividades_pen=x['actividades']
            for y in actividades_pen:
                if y['estado']=='':
                    dia=y['dia']
                    if dia=='lunes':
                        lunes.append(y['nombre'])
                        lunes.append(y['curso'])
                        lunes.append(y['h_inicio'])
                        lunes.append(y['h_final'])
                        break
                    elif dia=='martes':
                        martes.append(y['nombre'])
                        martes.append(y['curso'])    
                        martes.append(y['h_inicio'])
                        martes.append(y['h_final'])
                        break
                    elif dia=='miercoles':
                        miercoles.append(y['nombre'])
                        miercoles.append(y['curso'])
                        miercoles.append(y['h_inicio'])
                        miercoles.append(y['h_final'])
                        break
                    elif dia=='jueves':
                        jueves.append(y['nombre'])
                        jueves.append(y['curso'])
                        jueves.append(y['h_inicio'])
                        jueves.append(y['h_final'])
                        break
                    elif dia=='viernes':
                        viernes.append(y['nombre'])
                        viernes.append(y['curso'])
                        viernes.append(y['h_inicio'])
                        viernes.append(y['h_final'])
                        break
                    elif dia=='sabado':
                        sabado.append(y['nombre'])
                        sabado.append(y['curso'])
                        sabado.append(y['h_inicio'])
                        sabado.append(y['h_final'])
                        break
                    elif dia=='domingo':
                        domingo.append(y['nombre'])
                        domingo.append(y['curso'])
                        domingo.append(y['h_inicio'])
                        domingo.append(y['h_final'])
                        break
    limpiar_terminal()
    print("Lunes:")
    for e in lunes:
        print(e)
    print("Martes:")
    for e in martes:
        print(e)
    print("Miercoles:")
    for e in miercoles:
        print(e)
    print("Jueves:")
    for e in jueves:
        print(e)
    print("Viernes:")
    for e in viernes:
        print(e)
    print("Sabado:")
    for e in sabado:
        print(e)
    print("Domingo:")
    for e in domingo:
        print(e)
    opptt=input("Envie 1 tecla para regresar al menu:")        
    if opptt==1:
        JUMP
    
