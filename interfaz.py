from time import sleep
import logicaproyecto as logica



'''                             MENU DEL PROYECTO                                                                              '''
#                               INTERFAZ GRAFICA



def menu_interfaz(): 
    logica.limpiar_terminal
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
                            contra= input("Contraseña: ")
                            logica.us_momentaneo(usuario)
                            if logica.validar_estudiante(usuario,contra):
                                logica.limpiar_terminal()
                                menu_prin_estudiante() 
                            else:
                                print("Usuario o contraseña incorrecta")
                                sleep(2)


                        case 2:
                            logica.registrar_estudiante()

                        case 3:
                            break
                        case _:
                            print("Opcion invalida")
            case 2:
                print("Usuario Administrativo")
                print("1) Iniciar sesion")
                print("2) Registrarse")
                print("3) Salir")
                optt= int(input(" Su opcion es: "))
                match optt:
                    case 1: #iniciar sesion admin*****
                        usuario= input("Usuario: ")
                        contraseña= input("Contraseña: ")
                        if logica.validar_admin(usuario,contraseña):
                            
                            menu_prin_administrativo() 
                                
                        else:
                            print("Usuario o contraseña incorrecta")
                            sleep(2)
                    case 2:
                        logica.registrar_admin()
                    case 3:
                        break
                    case _:
                        print("Opcion invalida")
            
                
            case 3:
                print("\n\t¡Muchas garcias por utilizar nuestro sistema!")
                logica.sleep(3)
                logica.limpiar_terminal()
                break



def menu_prin_estudiante():
    while True: 
    
        print("1) Cambio de carrera")
        print("2) Matricular cursos")
        print("3) Agregar actividades")
        print("4) Salir")
        opt= int(input(" Su opcion es: "))
        match opt: 
            case 1:
                # Cambio de Carrera:
                logica.cambiar_carrera()

            case 2:
                # Matricular cursos:
                logica.matricular_cursos()



            case 3:
                pass  
                # Agregar actividades 


def menu_prin_administrativo():
    while True: 
        print("Nombre: Fernando Chaves Calvo, telefono:83220200")
        print("1) Agregar cursos")
        print("2) Agregar carreras")
        print("3) Salir")
        opt= int(input(" Su opcion es: "))
        match opt:
            case 1:
                logica.registros_de_cursos()
                
            case 2:
                logica.registros_de_carreras()
            case 3:
                break
            case _:
                print("Opcion invalida")

menu_interfaz()
