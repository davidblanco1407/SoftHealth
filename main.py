from simple_colors import *
from modules.AdministradorA import Administrador
from modules.EntidadA import Entidad
from modules.PersonalA import PersonalHospital
from modules.pacienteA import Paciente
from modules.menu import menu_paciente, menu_personalMedico, menu_administrador

valAdmin = False
valEntidad = False
valPersonal = False
objAdministrador=Administrador('','','','','','','','','','','')
objEntidad=Entidad('','','','','')
objPersonal=PersonalHospital('','','','','','','','','','','','')
objPaciente=Paciente('','','','','','','','','','','')

def base():
    print(green(f'\n{'-'*80}\n{'-'*27} Bienvenido a SoftHealth {'-'*28}\n{'-'*80}','bold'))
    if primeraVez() == True:
        x = tipoPersona()
        if x == 1:
            objPaciente.registrarPaciente()
            print(green(f'\n{'-'*30} Usuario registrado {'-'*30}'))
            base()
        elif x == 2:
            seParteDeNosotros()
    else:
        iniciarSesion()

def primeraVez():
<<<<<<< HEAD
    opcion=0
    while opcion<1 or opcion>2:
        print(black('¿Es primera vez en SoftHealth?\n\t1. Sí.\n\t2. No.'))
        opcion=int(input(('    >>> Digite su respuesta: ')))
    if opcion==1:
=======
    opcion = 0
    print(black('¿Es su primera vez en SoftHealth?','italic'))
    print(black('\t1. Sí.\n\t2. No.'))
    opcion = int(input('    >>> Seleccione una opción: '))
    while opcion < 1 or opcion > 2:
        print(red(f'\n{'-'*16} Error, por favor seleccione una opción valida {'-'*17}\n'))
        opcion = int(input('    >>> Seleccione una opción: '))
    if opcion == 1:
>>>>>>> santiago
        return True
    else:
        return False

def tipoPersona():
    print('-'*80)
    print(black('¿Quién intenta entrar en SoftHealth?','italic'))
    print(black('\t1. Usuario/Paciente.\n\t2. Administrador.'))
    opcion=int(input(('    >>> Seleccione una opción: ')))
    while opcion < 1 or opcion > 2:
        print(red(f'\n{'-'*16} Error, por favor seleccione una opción valida {'-'*17}\n'))
        opcion = int(input('    >>> Seleccione una opción: '))
    return opcion

def seParteDeNosotros():
    global valAdmin, valEntidad, valPersonal
    opcion = 0
    print('-'*80)
    print(green(f'{'-'*28} Registro Administrador {'-'*28}','bold'))
    print('-'*80)
    print(black('Para continuar complete los tres registros...','italic'))
    print(black('\t1. Sobre usted.\n\t2. Sobre la IPS/EPS.\n\t3. Sobre el personal.\n\t4. ¡Listo para trabajar!'))
    while opcion < 1 or opcion > 4:
        opcion = int(input(('    >>> Seleccione una opción: ')))
    if opcion == 1:
        objAdministrador.registrarAdmin()
        valAdmin = True
        print(blue(f'\n{'-'*13} Sección completa, continue con el siguiente registro {'-'*13}\n'))
        seParteDeNosotros()
    elif opcion == 2:
        objEntidad.registrarEntidad()
        valEntidad = True
        print(blue(f'\n{'-'*13} Sección completa, continue con el siguiente registro {'-'*13}\n'))
        seParteDeNosotros()
    elif opcion == 3:
        objPersonal.registrarPersonal()
        valPersonal = True
        print(blue(f'\n{'-'*13} Sección completa, continue con el siguiente registro {'-'*13}\n'))
        seParteDeNosotros()
    else:
        if valAdmin==True and valEntidad==True and valPersonal==True:
            print(green('\nTodos los datos han sido registrados correctamente.........','bold'))
            input(blue('Inicie sesión en su cuenta, para continuar presione "enter" ','bold'))
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
            print('-'*80)
            print(blue(f'Iniciando sesión............................','bold'))
            input(green(f'Ha ingresado correctamente, presione "enter" ','bold'))
            menu_paciente()
        else: 
            print(red(f'\n{'-'*17} Correo electrónico y/o contraseña incorrectos {'-'*16}\n'))
            print(black('\t1. Reintentar.\n\t2. Inicio.'))
            q = int(input('    >>> Seleccione una opción: '))
            if q == 1:
                iniciarSesion()
            else:
                base()
    elif x == 2:
        if objAdministrador.iniciarSesion() == True:
            print('-'*80)
            print(blue(f'Iniciando sesión............................','bold'))
            input(green(f'Ha ingresado correctamente, presione "enter" ','bold'))
            menu_administrador()
        else:
            print(red(f'\n{'-'*17} Correo electrónico y/o contraseña incorrectos {'-'*16}\n'))
            print(black('\t1. Reintentar.\n\t2. Inicio.'))
            q = int(input('    >>> Seleccione una opción: '))
            if q == 1:
                iniciarSesion()
            else:
                base()
    else:
        if objPersonal.iniciarSesion() == True:
            print('-'*80)
            print(blue(f'Iniciando sesión............................','bold'))
            input(green(f'Ha ingresado correctamente, presione "enter" ','bold'))
            menu_personalMedico()
        else:
            print(red(f'\n{'-'*17} Correo electrónico y/o contraseña incorrectos {'-'*16}\n'))
            print(black('\t1. Reintentar.\n\t2. Inicio.'))
            q = int(input('    >>> Seleccione una opción: '))
            if q == 1:
                iniciarSesion()
            else:
                base()
base()