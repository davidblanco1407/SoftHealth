from simple_colors import *

def menu():
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
            print(green('\n    No hay resultados para su búsqueda...\n'))
        
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

menu()