from AdministradorA import Administrador
from EntidadA import Entidad
from PersonalA import Personal
from pacienteA import Paciente
from menu import menu  
objAdministrador=Administrador('','','','','','','','','','','')
objEntidad=Entidad('','','','','','','','','','','')
objPersonal=Personal('','','','','','','','','','','')
objPaciente=Paciente('','','','','','','','','','','')
def base():
    print('\n')
    print('≛'*50,'\n')
    print('☲'*12,'Bienvenido a SoftHealth','☲'*12)
    if primeraVez() == True:
        if tipoPersona()== 1:
            objPaciente.registrarPaciente()
        elif tipoPersona()== 2:
            seParteDeNosotros()
        else:
            objPersonal.registrarPersonal()

    else:
        iniciarSesion()

def primeraVez():
    opcion=0
    while opcion<1 or opcion>2:
        opcion=int(input(('¿Es primera vez en SoftHealth?\n\t1. Sí.\n\t2. No.\nDigite su respuesta: ')))
    if opcion==1:
        return True
    else:
        return False
def tipoPersona():
    opcion=0
    while opcion<1 or opcion>3:
        opcion=int(input(('¿Quien intenta entrar en SoftHealth?\n\t1. Usuario/Paciente.\n\t2. Administrador.\n\t3. Personal Medico\nDigite su respuesta: ')))
    if opcion==1:
        return 1
    elif opcion==2:
        return 2
    else:
        return 3
def seParteDeNosotros():
    opcion=0
    valAdmin=0
    valEntidad=0
    valPersonal=0
    print('\nCompleta los tres registros para continuar.','☲'*20,'\n   1. Sobre Usted.\n   2. Sobre la IPS/EPS.\n  3. Sobre el personal.\n 4. ¡Listo para trabajar!  ')
    while opcion<1 or opcion>4:
        opcion=int(input(('Opcion: ')))
    print('☲'*100)
    if opcion==1:
        objAdministrador.registrarAdmin()
        valAdmin+=1
        seParteDeNosotros()
    elif opcion==2:
        objEntidad.registrarEntidad()
        valEntidad+=1
        seParteDeNosotros()
    elif opcion==3:
        objPersonal.registrarPersonal()
        valPersonal+=1
        seParteDeNosotros()
    else:
        if valAdmin==1 and valEntidad==1 and valPersonal==1:
            print('Todos los datos han sido registrados correctamente.')
            print('Inicie sesión en su cuenta.')
            base()
        else:
            print('Por favor, complete todos los pasos para continuar.')
            seParteDeNosotros()
            
def iniciarSesion():
    print('Inicie sesión en su cuenta.','☲'*20)
    if tipoPersona()==1:
        if objPaciente.iniciarSesion() == True:
            menu()
        else: 
            q=input('\t1. Reintentar.\n\t2. Inicio.\nOpcion: ')
            if q=='1':
                iniciarSesion()
            else:
                base()
    elif tipoPersona()==2:
        if objAdministrador.iniciarSesion() == True:
            menu()
        else: 
            q=input('\t1. Reintentar.\n\t2. Inicio.\nOpcion: ')
            if q=='1':
                iniciarSesion()
            else:
                base()    
    else:
        if objPersonal.iniciarSesion() == True:
            menu()
        else: 
            q=input('\t1. Reintentar.\n\t2. Inicio.\nOpcion: ')
            if q=='1':
                iniciarSesion()
            else:
                base()    
base()
