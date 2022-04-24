import datetime as dt

lista_estudiantes=[{'clave':1,'Nombre':'Leonardo', 'carrera':'Compuitación'}]
lista_cursos=[{'clave':1,'Nombre':'Introducción a la programación','h_inicio':dt.time(7,55,0),'h_final':dt.time(11,30,0),'dia':'L'}]

lista_actividades=[]





def choque_horario (fi1,ff1,fi2,ff2):
    return ((fi2>=fi1 and fi2<=ff1)or(ff2>=fi1 and ff2<=ff1))


def insertar_actividad (ne,l):
    choque=False
    for e in l:
        if choque_horario(e['h_inicio'],e['h_final'],ne['h_inicio'],ne['h_final']):
            choque=True
            break
    if not choque:
        l.append(ne)
        print ("se agrego la actividad")
    else:
        print ("No se agrega por choque de horarios")


insertar_actividad({'descripcion':'Desarrollo de primer proyecto','h_inicio':dt.time(13,00,0),'h_final':dt.time(14,00,0),'curso':1,'estudiante':1,'tipo':0},lista_actividades)
insertar_actividad({'descripcion':'Desarrollo de primer proyecto','h_inicio':dt.time(14,00,1),'h_final':dt.time(16,00,0),'curso':1,'estudiante':1,'tipo':0},lista_actividades)
insertar_actividad({'descripcion':'Desarrollo de primer proyecto','h_inicio':dt.time(13,30,0),'h_final':dt.time(13,30,0),'curso':1,'estudiante':1,'tipo':0},lista_actividades)

print (choque_horario(ia1,fa1,ia2,fa2))