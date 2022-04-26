from sre_constants import JUMP
from time import sleep
import logicaproyecto as logica




'''                             MENU DEL PROYECTO                                                                              '''
#                               INTERFAZ GRAFICA



def menu_interfaz():  #Este es el menu principal de la interfaz funciona para la division de usuarios y de funciones
    logica.limpiar_terminal()
    while True:
        logica.limpiar_terminal()
        print ("Bienvenido a tu calendario")


        print("¿Usuario estudiante o administrativo?")
        
        print ("1) Estudiante")
        print ("2) Administrador")
        print ("3) Salir")
        opcion= int(input("Digite el numero de opcion que desea:"))
        logica.limpiar_terminal()

        match opcion:
            case 1:
                while True:
                    logica.limpiar_terminal()
                # interfaz que si quiere registrarse, inicar sesion, o salir como estudiante
                    print("Usuario Estudiante")
                    print("1) Iniciar sesion")
                    print("2) Registrarse")

                    print("3) Salir")
                    opt= int(input(" Su opcion es: "))
                    match opt:
                        case 1: 
                        
                            #iniciar sesion estudiante*****
                            usuario= input("Usuario: ")
                            contra= logica.obtener_clave("Contraseña: ")
                            
                            if logica.validar_estudiante(usuario,contra):    #mediante la funcion validar_estudiante, se logra compararlos datos almacenados en una listan de diccionarios con los datos puestos en tiempo real
                                logica.limpiar_terminal()
                                menu_prin_estudiante()  #menu principal para estudiantes
                            else:
                                print("Usuario o contraseña incorrecta")
                                sleep(2)


                        case 2:
                            logica.registrar_estudiante()  #funcion que registra el nuevo estudiante

                        case 3:
                            break
                        case _:
                            print("Opcion invalida")
            case 2:
                print("Usuario Administrativo") #menu de registro o inicio de sesion para administradores
                print("1) Iniciar sesion")
                print("2) Registrarse")
                print("3) Salir")
                optt= int(input(" Su opcion es: "))
                match optt:
                    case 1: #iniciar sesion acomo administrador
                        usuario= input("Usuario: ")
                        contraseña = logica.obtener_clave("Contraseña: ")
                        if logica.validar_admin(usuario,contraseña): #en esta funcion se valida el administrador
                            
                            menu_prin_administrativo()  #menu principal del administrador
                                
                        else:
                            print("Usuario o contraseña incorrecta")
                            sleep(2)
                    case 2:
                        logica.registrar_admin()   #funcion para registrar nuevos datos de un usuario administrador
                        
                    case 3:
                        break
                    case _:
                        print("Opcion invalida")
            
                
            case 3:
                print("\n\t¡Muchas garcias por utilizar nuestro sistema!")
                logica.sleep(3)
                logica.limpiar_terminal()
                break



def menu_prin_estudiante():  #menu principal del estudiante
    while True: 
        JUMP
        logica.limpiar_terminal()
        print("1) Cambio de carrera")
        print("2) Matricular cursos")
        print("3) Agregar actividades")
        print("4) Mostar calendario")
        print("5) Salir")
        opt= int(input(" Su opcion es: "))

        match opt: 
            case 1:
                # Cambio de Carrera:
                logica.cambiar_carrera()    # hace que la carrera previamente guardada se cambie por una nueva
            
            
            

            case 2:
                while True:
                    logica.limpiar_terminal()        #menu para cursos
                # Matricular cursos:
                    print("1) Matricular cursos")
                    print("2) Modificar estado de cursos")
                    print("3) Salir")
                    opttt= int(input(" Su opcion es: "))
                    match opttt:
                        case 1:
                            logica.matricular_cursos()       # esta funcion matricula los cursos que escojan y que sean de carrera
                        case 2: 
                            logica.aprobar_reprobar_cursos()  # funcion para poder cambiar el estado del curso
                        case 3: 
                            break
                        case _:
                            print("Opcion invalida")

            case 3:
                # Agregar actividades
                    logica.menu_registro_de_actividades()
            case 4:
                logica.calendario()     #funcion que imprime un horario con varios datos de los cursos y actividades del estudiante
                
            case 5:
                break
            case _:
                print("Opcion invalida")

def menu_prin_administrativo(): #menu del administrador
    while True: 
        logica.limpiar_terminal()
        print("Bienvenido administrador")  
        print("1) Agregar cursos")
        print("2) Agregar carreras")
        print("3) Salir")
        opt= int(input(" Su opcion es: "))
        match opt:
            case 1:
                logica.registros_de_cursos() # esta funcion agrega cursos para matricularlos despues
                
            case 2:
                logica.registros_de_carreras() #agrega carreras
            case 3:
                break
            case _:
                print("Opcion invalida")

menu_interfaz()
