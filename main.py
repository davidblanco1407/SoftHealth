from simple_colors import *
from modules.AdministradorA import Administrador
from modules.EntidadA import Entidad
from modules.PersonalA import PersonalHospital
from modules.pacienteA import Paciente
from modules.menu import menu_paciente, menu_personalMedico, menuAdministrador

valAdmin = False
valEntidad = False
valPersonal = False
objAdministrador=Administrador('','','','','','','','','','','')
objEntidad=Entidad('','','','','')
objPersonal=PersonalHospital('','','','','','','','','','','','')
objPaciente=Paciente('','','','','','','','','','','')

def base():
    print('\n')
    print('-'*80)
    print(green(f'{'-'*27} Bienvenido a SoftHealth {'-'*28}','bold'))
    print('-'*80)
    if primeraVez() == True:
        x=tipoPersona()
        if x== 1:
            objPaciente.registrarPaciente()
            print(green('-'*80))
            print(green(f'{'-'*30} Usuario registrado {'-'*30}','bold'))
            print(green('-'*80))
            base()
        elif x== 2:
            seParteDeNosotros()
        else:
            objPersonal.registrarPersonal()
            print(green('-'*80))
            print(green(f'{'-'*29} Personal registrado {'-'*30}','bold'))
            print(green('-'*80))
    else:
        iniciarSesion()

def primeraVez():
    opcion=0
    while opcion<1 or opcion>2:
        print(black('¿Es primera vez en SoftHealth?\n\t1. Sí.\n\t2. No.'))
        opcion=int(input(('    >>> Digite su respuesta: ')))
    if opcion==1:
        return True
    else:
        return False

def tipoPersona():
    print('-'*80)
    opcion=0
    while opcion<1 or opcion>3:
        print(black('¿Quien intenta entrar en SoftHealth?\n\t1. Usuario/Paciente.\n\t2. Administrador.\n\t3. Personal Medico'))
        opcion=int(input(('    >>> Seleccione una opción: ')))
    return opcion

def seParteDeNosotros():
    global valAdmin, valEntidad, valPersonal
    opcion=0
    print('-'*80)
    print(green(f'{'-'*18} Completa los tres registros para continuar {'-'*18}'))
    print('-'*80)
    print(black('        1. Sobre Usted.\n        2. Sobre la IPS/EPS.\n        3. Sobre el personal.\n        4. ¡Listo para trabajar!'))
    while opcion<1 or opcion>4:
        opcion=int(input(('    >>> Seleccione una opción: ')))
    if opcion==1:
        objAdministrador.registrarAdmin()
        valAdmin = True
        seParteDeNosotros()
    elif opcion==2:
        objEntidad.registrarEntidad()
        valEntidad = True
        seParteDeNosotros()
    elif opcion==3:
        objPersonal.registrarPersonal()
        valPersonal = True
        seParteDeNosotros()
    else:
        if valAdmin==True and valEntidad==True and valPersonal==True:
            print(green('\nTodos los datos han sido registrados correctamente','bold'))
            input(black('Inicie sesión en su cuenta, para continuar presione "enter" ','italic'))
            base()
        else:
            print(red(f'\n{'-'*14} Por favor, complete todos los pasos para continuar {'-'*14}\n'))
            seParteDeNosotros()
            
def iniciarSesion():
    print('-'*80)
    print(green(f'{'-'*25} Iniciar sesión en su cuenta {'-'*26}','bold'))
    x = tipoPersona()
    if x == 1:
        if objPaciente.iniciarSesion() == True:
            menu_paciente()
        else: 
            print(red('-'*80))
            print(red(f'{'-'*17} Correo electrónico y/o contraseña incorrectos {'-'*16}'))
            print(red('-'*80))
            print(black('\t1. Reintentar.\n\t2. Inicio.'))
            q=input('    >>> Seleccione una opción: ')
            if q=='1':
                iniciarSesion()
            else:
                base()
    elif x == 2:
        if objAdministrador.iniciarSesion() == True:
            menuAdministrador()
        else:
            print(red('-'*80))
            print(red(f'{'-'*17} Correo electrónico y/o contraseña incorrectos {'-'*16}'))
            print(red('-'*80))
            print(black('\t1. Reintentar.\n\t2. Inicio.'))
            q=input('    >>> Seleccione una opción: ')
            if q=='1':
                iniciarSesion()
            else:
                base()
    else:
        if objPersonal.iniciarSesion() == True:
            menu_personalMedico()
        else:
            print(red('-'*80))
            print(red(f'{'-'*17} Correo electrónico y/o contraseña incorrectos {'-'*16}'))
            print(red('-'*80))
            print(black('\t1. Reintentar.\n\t2. Inicio.'))
            q=input('    >>> Seleccione una opción: ')
            if q=='1':
                iniciarSesion()
            else:
                base()
base()