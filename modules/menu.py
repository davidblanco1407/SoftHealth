from simple_colors import *
from .pacienteA import Paciente

def menu_paciente():
    z = True
    while z == True:
        # Títulos
        _ = ('-'*30)
        print('\n')
        print('-'*80)
        print(green(f'----{_} SoftHealth {_}----','bold'))
        print('-'*80)
        print(black(f'      ¡Hola, bienvenido de nuevo!\n','italic'))
        # Menú de Opciones
        print(black('Menú:'),'\n1. Info. personal médico\n2. Agendar cita\n3. Tu historia clínica\n4. Cerrar sesión')
        x = int(input('    >>> Para continuar, seleccione una opción: '))
        while x < 1 or x > 4:
            print(red('    Error505, por favor seleccione un número valido...\n'))
            x = int(input('    >>> Para continuar, seleccione una opción: '))
        match x:
            # Sección 'Info. personal médico'
            case 1:
                # Títulos
                print('-'*80)
                print(green(f'{'-'*28} Info. Personal Médico {'-'*29}','bold'))
                print('-'*80)
                # Campos
                print(black('Filtros de Busqueda','bold'))
                print(black('    Para continuar llene los datos del médico','italic'))
                name = input('\nNombre: ')
                area = input('Área: ')
                Paciente.busquedaMedico(name, area)
            
            case 2:
                # Títulos
                print('-'*80)
                print(green(f'{'-'*28} Agendar Cita {'-'*29}','bold'))
                print('-'*80)
                # Opciones
                services = input("Seleccione o especifique un servicio: ")
                dia = input('Seleccione o asigne un dia: ')
                print(green(f'{'-'*80}\n{'-'*22} La cita ha sido agendada {'-'*22}\n{'-'*80}'))

            case 3:
                # Títulos
                print('-'*80)
                print(green(f'{'-'*28} Historial Clínico {'-'*29}','bold'))
                print('-'*80)
                # Opciones
                print('1. Ver tu historial clinico\n2. Solicitar una edicion\n3. Editar historial\n4.solicitar Actualizacion\n5. Salir')
                i = int(input('    >>> Para continuar, seleccione una opción: '))
                match i:
                    case 1:
                        fecha = input('Ingrese la fecha del historial clínico: ')
                    case 2:
                        edicion = input('Ingrese la información que desea solicitar un cambio: ')

            case 4:
                print(red(f'{'-'*80}\n{'-'*22} Se ha cerrado sesión correctamente {'-'*22}\n{'-'*80}'))
                z = False


def menu_personalMedico():
    # Títulos
    _ = ('-'*30)
    print('\n')
    print('-'*80)
    print(green(f'----{_} SoftHealth {_}----','bold'))
    print('-'*80)
    print(black(f'      ¡Hola, bienvenido de nuevo doctor!\n','italic'))
    # Menú de Opciones
    print(black('Menú:'),'\n1. Info. personal paciente\n2. Agendar cita paciente\n3. info historia clínica paciente\n4. Cerrar sesión')
    x = int(input('    >>> Para continuar, seleccione una opción: '))
    while x < 1 or x > 5:
        print(red('    Error, por favor seleccione un número valido...\n'))
        x = int(input('    >>> Para continuar, seleccione una opción: '))
        
    match x:
        
        # Sección 'Info. personal Paciente'
        case 1:
            # Títulos
            print('-'*80)
            print(green(f'{'-'*28} Info. Personal Paciente {'-'*29}','bold'))
            print('-'*80)
            # Campos
            print(black('Filtros de Busqueda','bold'))
            print(black('    Para continuar llene los datos del paciente','italic'))
            name = input('\nNombre: ')
            area = input('Área: ')
            print(green('\n    No hay resultados para su búsqueda...\n'))
        
        
        case 2:
            # Títulos
            print('-'*80)
            print(green(f'{'-'*28} Agendar cita paciente {'-'*29}','bold'))
            print('-'*80)
            # Opciones
            ver = input("Agende una cita para el paciente: ")
            print(green(f'{'-'*80}\n{'-'*22} Dejaste De Agendar una cita para el paciente {'-'*22}\n{'-'*80}'))
            # Títulos
            print('-'*80)
        
        
        
        case 3:
            # Títulos
            print('-'*80)
            print(green(f'{'-'*28} Ver Historia Clinica Del Paciente {'-'*29}','bold'))
            print('-'*80)
            # Opciones
            ver = input("Seleccione que historia clinica quiere ver: ")
            print(green(f'{'-'*80}\n{'-'*22} Dejaste De Ver Historia Clinica Del Paciente {'-'*22}\n{'-'*80}'))
            # Títulos
            print('-'*80)
            
            
        case 4:
            print(green(f'{'-'*28} Editar Historia Clinica Del Paciente {'-'*29}','bold'))
            print('-'*80)
            # Opciones
            editar = input("Edite La Historia Clinica Del Paciente: ")
            print(green(f'{'-'*80}\n{'-'*22} Dejaste De Ver Historia Clinica Del Paciente {'-'*22}\n{'-'*80}'))
            
            
            
        # actualizar. 'Info historial paciente'
        case 5:
            # Títulos
            print('-'*80)
            print(green(f'{'-'*28} Actualizar Historia Clinica Del Paciente {'-'*29}','bold'))
            print('-'*80)
            # Opciones
            actualizar = input("actualice la historia clinica del paciente: ")
            print(green(f'{'-'*80}\n{'-'*22} Historia clinica paciente actualizada {'-'*22}\n{'-'*80}'))

def menuAdministrador():
    # Títulos
    _ = ('-'*30)
    print('\n')
    print('-'*80)
    print(green(f'----{_} SoftHealth {_}----','bold'))
    print('-'*80)
    print(black(f'      ¡Hola, bienvenido de nuevo administrador !\n','italic'))
    # Menú de Opciones
    print(black('Menú:'),'\n1. Info. personal médico\n2. agregar personal medico\n3. Administrar citas\n4.  consultar historia clínica\n5. editar historia clinica paciente\n6. actualizar historia clinica paciente\n7. Cerrar sesión')
    x = int(input('    >>> Para continuar, seleccione una opción: '))
    while x < 1 or x > 7:
        print(red('    Error505, por favor seleccione un número valido...\n'))
        x = int(input('    >>> Para continuar, seleccione una opción: '))
        
    match x:
        
        # Sección 'Info. personal Medico'
        case 1:
            # Títulos
            print('-'*80)
            print(green(f'{'-'*28} Info. Personal Medico {'-'*29}','bold'))
            print('-'*80)
            # Campos
            print(black('Filtros de Busqueda','bold'))
            print(black('    Para continuar llene los datos del medico','italic'))
            name = input('\nNombre: ')
            area = input('Área: ')
            print(green('\n    No hay resultados para su búsqueda...\n'))
        
        
        
        # Sección 'agregar personal medico'
        
        case 2:
            # Títulos
            print('-'*80)
            print(green(f'{'-'*28} Agregar Personal Medico {'-'*29}','bold'))
            print('-'*80)
            # Opciones
            agregar = input("agrege el nuevo personal medico : ")
            print(green(f'{'-'*80}\n{'-'*22} saliste de agregar personal medico {'-'*22}\n{'-'*80}'))
            
        # 'administrar citas'
        case 3:
            # Títulos
            print('-'*80)
            print(green(f'{'-'*28}  Administrar citas {'-'*29}','bold'))
            print('-'*80)
            # Opciones
            consultar_citas = input("Administre las citas del Paciente : ")
            print(green(f'{'-'*80}\n{'-'*22} saliste de administrar  citas paciente {'-'*22}\n{'-'*80}'))
            
        # consultar. 'Historia clinica paciente'
        case 4:
            # Títulos
            print('-'*80)
            print(green(f'{'-'*28} Consultar Historia Clinica Del Paciente  {'-'*29}','bold'))
            print('-'*80)
            # Opciones
            consultar_historia = input("consulte la historia clinica del paciente : ")
            print(green(f'{'-'*80}\n{'-'*22} saliste de consultar historia clinica del paciente {'-'*22}\n{'-'*80}'))
            
        # editar. 'historia clinica paciente'
        case 5:
            # Títulos
            print('-'*80)
            print(green(f'{'-'*28} Editar Historia Clinica Del Paciente  {'-'*29}','bold'))
            print('-'*80)
            # Opciones
            editar_historia = input("edite la historia clinica del paciente : ")
            print(green(f'{'-'*80}\n{'-'*22} saliste de editar historia clinica del paciente {'-'*22}\n{'-'*80}'))
            
        # actualizar. 'Actualizar Historia clinica paciente'
        case 6:
            # Títulos
            print('-'*80)
            print(green(f'{'-'*28} Actualizar Historia Clinica Del Paciente  {'-'*29}','bold'))
            print('-'*80)
            # Opciones
# 'cerrar sesion' :r_historia_paciente = input("actualice la historia clinica del pacSe ha cerrado sesión correctamente     print(green(f'{'-'*80}\n{'-'*22} saliste de actualizar historia clinica del paciente {'-'*22}\n{'-'*80}'))
            
        # 'cerrar sesion' :
        case 7:
                print(red(f'{'-'*80}\n{'-'*22} has salido del menu administ {'-'*22}\n{'-'*80}'))
                z = False