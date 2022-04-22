#snakecase
from time import sleep
from hashlib import md5
from getpass import getpass
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

usuarios_estudiante=[{'Nombre':'Jeison Blanco Rojas', 'Carrera':'computacion', 'autenticacion':{'usuario':'jeisonb1','contraseña':'jei123'},
'cursos_matriculados':[{'nombre':'taller de programacion','estado': ''}, {'nombre':'introduccion a la programacion','estado': ''}], 'actividades':{'futbol':{'dia':'lunes','horas':'4'}}}]

usuarios_admin=[{'Nombre':'Fernando Chaves Calvo', 'telefono':'83220200', 'autenticacion':{'usuario':'admin','contraseña':'admin'}}]
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
            usuario_momentaneo=(value['Nombre'])
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


    

cursos=[{'nombre': 'taller de programacion','creditos':'2','horas lectivas':'3','inicia':'07-02-22','finaliza':'23-06-22','dia de clases':'viernes','hora de clases':'5pm','carreras':'computacion'}]

def registros_de_cursos():
    curso_nuevo=dict()
    
    curso_nuevo['nombre']=c=input("Nombre del curso: ")
    
    curso_nuevo['creditos']=int(input("creditos: "))
    curso_nuevo['horas lectivas']=int(input("horas lectivas: "))
    curso_nuevo['inicia']=input ("fecha de inicio del curso: ")
    curso_nuevo['finaliza']=input ("fecha de finalizacion del curso: ")
    curso_nuevo['dia de clases']=input("dia del curso: ")
    curso_nuevo['hora de clases']=input("hora del curso: ")
    curso_nuevo['carreras']=carre=input("carreras que pertenece el curso: ")
    cursos.append(curso_nuevo)
    # for value in carerras_cursos:
    #     if value['nombre']==carre:
    #         carerras_cursos['cursos_esp']+=c
   
carerras_cursos={'nombre':'computacion','cursos_esp':['taller de programacion','introduccion a la programacion']}
carreras={'computacion',"agronomia"}
def registros_de_carreras():
    limpiar_terminal()
    print("Carreras existentes:")   
    print(carreras)
    carre_nueva=(input("Nombre de la carrera: "))
    carreras.add(carre_nueva)
    # carerras_cursos.append(carre_nueva)

def cambiar_carrera():
    global usuario_momentaneo
    limpiar_terminal()
    carreranueva= input("nueva carrera:" )

    for x in usuarios_estudiante:
        if x['Nombre']==usuario_momentaneo:
            x['Carrera']=carreranueva
            x['cursos matriculados']=[]
            

    

def matricular_cursos():
    limpiar_terminal()
    global usuario_momentaneo
    a_matricular = input("Cual curso desea matricular:")
    for x in usuarios_estudiante:
        
        if x['Nombre'] == usuario_momentaneo:
            
            for curso in cursos:
                if curso['carreras'] == x['Carrera'] and x['cursos_matriculados']!=a_matricular:
                    x['cursos_matriculados'][a_matricular]['estado']=''
                else:
                    print("Curso Incorrecto o ya matriculado")

def aprobar_reprobar_cursos():
    limpiar_terminal()
    global usuario_momentaneo
    for x in usuarios_estudiante:
        
        if x['Nombre'] == usuario_momentaneo:
            curso_modificar = input("Cual curso desea modificar el estado:")

            for curso in cursos:
                if curso['carreras'] == x['Carrera'] and x['cursos_matriculados'] == curso_modificar:
                    x['cursos_matriculados'][curso_modificar]['estado']= estado = input("Curso aprobado o reprobado:")
                else:
                    print("Curso Incorrecto o no matriculado")

lunes=[]
martes=[]
miercoles=[]
jueves=[]
viernes=[{'taller de programacion':'5pm'}]
sabado=[]
domingo=[]


#errores
def registro_de_asistencia_lectiva():
    global usuario_momentaneo
   
    for x in usuarios_estudiante:
        if x['Nombre'] == usuario_momentaneo:
            curso_pendiente=x['cursos_matriculados']
            for y in curso_pendiente:
                if y['estado']=='':
                    for curso in cursos:
                        if curso['nombre']==y['nombre']:
                            dia=curso['dia de clases']
                            if dia==lunes:
                                lunes.append(curso['nombre'] and curso['hora de clases'])
                            elif dia==martes:
                                martes.append(curso['nombre'] and curso['hora de clases'])
                            elif dia==miercoles:
                                miercoles.append(curso['nombre'] and curso['hora de clases'])
                            elif dia==jueves:
                                jueves.append(curso['nombre'] and curso['hora de clases'])
                            elif dia==viernes:
                                viernes.append(curso['nombre'] and curso['hora de clases'])
                            elif dia==sabado:
                                sabado.append(curso['nombre'] and curso['hora de clases'])
                            elif dia==domingo:
                                domingo.append(curso['nombre'] and curso['hora de clases'])

def calendario():
    limpiar_terminal()
    registro_de_asistencia_lectiva()
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
                    
                        
                       







        




# '''             prueba de funciones 
# '''
