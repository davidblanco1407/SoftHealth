from simple_colors import *

# Menú 'Paciente'
def menu_paciente():
    z = True
    while z == True:
        # Títulos
        print(green(f'\n{'-'*80}\n{'-'*30} 🏠 Menú principal {'-'*31}\n{'-'*80}','bold'))
        print(black(f'    ¡Hola, bienvenido de nuevo!','italic'))
        # Menú de Opciones
        print(black('Inicio','bold'),'\n1. Info. personal médico\n2. Agendar cita\n3. Tu historia clínica\n4. Cerrar sesión')
        x = int(input('    >>> Para continuar, seleccione una opción: '))
        while x < 1 or x > 4:
            print(red(f'\n{'-'*16} Error, por favor seleccione una opción valida {'-'*17}\n'))
            x = int(input('    >>> Para continuar, seleccione una opción: '))
        match x:
            # Sección 'Info. Personal Médico'
            case 1:
                # Títulos
                print('-'*80)
                print(green(f'{'-'*28} Info. Personal Médico {'-'*29}','bold'))
                print('-'*80)
                # Campos
                print(black('Filtros de Búsqueda','bold'))
                print(black('Para continuar llene los campos con los datos de su médico...','italic'))
                name = input('    >>> Nombre: ')
                area = input('    >>> Área: ')
                print(cyan(f'\n{'-'*25} Los resultados de su búsqueda {'-'*24}'))

            # Sección 'Agendar Cita'
            case 2:
                # Títulos
                print('-'*80)
                print(green(f'{'-'*33} Agendar Cita {'-'*33}','bold'))
                print('-'*80)
                # Opciones
                print(black('Para asignar una cita complete los datos a continuación...','italic'))
                services = input('    >>> Seleccione o especifique un servicio: ')
                day = input('    >>> Seleccione o asigne un dia en formato DD/MM/AAAA: ')
                print(cyan(f'\n{'-'*27} La cita ha sido agendada {'-'*27}'))

            # Sección 'Historial Clínico'
            case 3:
                # Títulos
                print('-'*80)
                print(green(f'{'-'*31} Historia Clínica {'-'*31}','bold'))
                print('-'*80)
                # Opciones
                print(black('\tMenú de Opciones'),'\n\t1. Ver tu historia clínica\n\t2. Solicitar una edición\n\t3. Volver al menú principal')
                i = int(input('    >>> Para continuar, seleccione una opción: '))
                match i:
                    case 1:
                        print(black('\nRecuerde que al ingresar una fecha se genera un documento donde se muestra\nsu historia clínica, a partir de la fecha ingresada hasta la actualidad.','italic'))
                        date = input('    >>> Ingrese una fecha en formato DD/MM/AAAA: ')
                        print(cyan(f'\n{'-'*26} Historial clínico generado {'-'*26}'))
                    case 2:
                        edicion = input('    >>> Ingrese la información que desea solicitar un cambio: ')
                        print(cyan(f'\n{'-'*10} Hemos recibido tu solicitud, pronto recibirás una respuesta {'-'*9}'))
                    case 3:
                        menu_paciente()

            # Cerrar Sesión
            case 4:
                print(red(f'{'-'*80}\n{'-'*22} Se ha cerrado sesión correctamente {'-'*22}\n{'-'*80}\n','bold'))
                z = False

# Menú 'Personal Médico'
def menu_personalMedico():
    z = True
    while z == True:
        # Títulos
        print(green(f'\n{'-'*80}\n{'-'*30} 🏠 Menú principal {'-'*31}\n{'-'*80}','bold'))
        print(black(f'    ¡Hola, bienvenido de nuevo!','italic'))
        # Menú de Opciones
        print(black('Inicio'),'\n1. Info. pacientes\n2. Agendamiento de citas\n3. Historias clínicas\n4. Cerrar sesión')
        x = int(input('    >>> Para continuar, seleccione una opción: '))
        while x < 1 or x > 5:
            print(red(f'\n{'-'*16} Error, por favor seleccione una opción valida {'-'*17}\n'))
            x = int(input('    >>> Para continuar, seleccione una opción: '))
        match x:
            # Sección 'Info. Personal'
            case 1:
                # Títulos
                print('-'*80)
                print(green(f'{'-'*27} Info. Personal Paciente {'-'*28}','bold'))
                print('-'*80)
                # Campos
                print(black('Filtros de Búsqueda','bold'))
                print(black('Para continuar, complete los campos con los datos del paciente...','italic'))
                nro_doc = input('    >>> Número documento del paciente: ')
                print(cyan(f'\n{'-'*25} Los resultados de su búsqueda {'-'*24}'))
            
            # Sección 'Agendamiento de Citas'
            case 2:
                # Títulos
                print('-'*80)
                print(green(f'{'-'*33} Agendar Cita {'-'*33}','bold'))
                print('-'*80)
                # Opciones
                print(black('Para asignar una cita llene los datos a continuación...','italic'))
                nro_doc = input('    >>> Número documento del paciente: ')
                services = input('    >>> Seleccione o especifique un servicio: ')
                day = input('    >>> Seleccione o asigne un dia en formato DD/MM/AAAA: ')
                print(cyan(f'\n{'-'*27} La cita ha sido agendada {'-'*27}'))
            
            # Sección 'Historias Clínicas'
            case 3:
                # Títulos
                print('-'*80)
                print(green(f'{'-'*31} Historia Clínica {'-'*31}','bold'))
                print('-'*80)
                # Opciones
                print(black('Para continuar, complete los campos con los datos del paciente...','italic'))
                nro_doc = input('    >>> Número documento del paciente: ')
                print(black('Recuerde que al ingresar una fecha se genera un documento donde se muestra\nsu historia clínica, a partir de la fecha ingresada hasta la actualidad.','italic'))
                date = input('    >>> Ingrese una fecha en formato DD/MM/AAAA: ')
                print(cyan(f'\n{'-'*26} Historial clínico generado {'-'*26}'))
                print('\n\t1. Si\n\t2. No')
                i = int(input('    >>> ¿Desea editarlo?: '))
                while i < 1 or x > 2:
                    if i == 1:
                        print(magenta('\nEditando...'))
                        break
                    elif i == 2:
                        print(yellow(f'\n{'-'*28} Gracias por confirmar {'-'*29}','italic'))
                        break
                    else:
                        print(red(f'\n{'-'*16} Error, por favor seleccione una opción valida {'-'*17}\n'))
                        i = int(input('    >>> ¿Desea editarlo?: '))
                
            # Cerrar Sesión
            case 4:
                print(red(f'{'-'*80}\n{'-'*22} Se ha cerrado sesión correctamente {'-'*22}\n{'-'*80}\n','bold'))
                z = False

# Menú 'Administrador'
def menu_administrador():
    z = True
    while z == True:
        # Títulos
        print(green(f'\n{'-'*80}\n{'-'*30} 🏠 Menú principal {'-'*31}\n{'-'*80}','bold'))
        print(black(f'    ¡Hola, bienvenido de nuevo!','italic'))
        # Menú de Opciones
        print(black('Inicio','bold'),'\n1. Info. personal\n2. Agendamiento de citas\n3. Historias clínicas\n4. Cerrar sesión')
        x = int(input('    >>> Para continuar, seleccione una opción: '))
        while x < 1 or x > 5:
            print(red(f'\n{'-'*16} Error, por favor seleccione una opción valida {'-'*17}\n'))
            x = int(input('    >>> Para continuar, seleccione una opción: '))
        match x:
            # Sección 'Info. Personal Médico'
            case 1:
                # Títulos
                print('-'*80)
                print(green(f'{'-'*28} Info. Personal Médico {'-'*29}','bold'))
                print('-'*80)
                # Campos
                print(black('    El personal médico que desea buscar, ¿Ya se encuentra registrado en\n    nuestra base de datos?','italic'))
                print('\t1. Si\n\t2. No')
                a = int(input('    >>> Para continuar, seleccione una opción: '))
                while a < 1 or a > 2:
                    print(red(f'\n{'-'*16} Error, por favor seleccione una opción valida {'-'*17}\n'))
                    a = int(input('    >>> Para continuar, seleccione una opción: '))
                if a == 1:
                    print(black('\nFiltros de Búsqueda','bold'))
                    print(black('Para continuar llene los campos con los datos del personal médico...','italic'))
                    name = input('    >>> Nombre: ')
                    area = input('    >>> Área: ')
                    print(cyan(f'\n{'-'*25} Los resultados de su búsqueda {'-'*24}'))
                    print('\n\t1. Si\n\t2. No')
                    i = int(input('    >>> ¿Desea editar uno de los datos?: '))
                    while i < 1 or i > 2:
                        print(red(f'\n{'-'*16} Error, por favor seleccione una opción valida {'-'*17}\n'))
                        i = int(input('    >>> ¿Desea editar uno de los datos?: '))
                    if i == 1:
                        print(magenta('\nEditando...'))
                    elif i == 2:
                        print(yellow(f'\n{'-'*28} Gracias por confirmar {'-'*29}','italic'))
                    else:
                        print(red(f'\n{'-'*16} Error, por favor seleccione una opción valida {'-'*17}\n'))
                        i = int(input('    >>> ¿Desea editarlo?: '))
                elif a == 2:
                    print('\n\t1. Si\n\t2. No')
                    n = int(input('    >>> ¿Desea registrar uno nuevo?: '))
                    while n < 1 or n > 2:
                        print(red(f'\n{'-'*16} Error, por favor seleccione una opción valida {'-'*17}\n'))
                        n = int(input('    >>> ¿Desea registrar uno nuevo?: '))
                    if n == 1:
                        pass
                    elif n == 2:
                        print(yellow(f'\n{'-'*28} Gracias por confirmar {'-'*29}','italic'))
                    else:
                        print(red(f'\n{'-'*16} Error, por favor seleccione una opción valida {'-'*17}\n'))
                        n = int(input('    >>> ¿Desea registrar uno nuevo?: '))
                else:
                    print(red(f'\n{'-'*16} Error, por favor seleccione una opción valida {'-'*17}\n'))
                    a = int(input('    >>> Para continuar, seleccione una opción: '))
                
            # Sección 'Agendamiento de Citas'
            case 2:
                # Títulos
                print('-'*80)
                print(green(f'{'-'*33} Agendar Cita {'-'*33}','bold'))
                print('-'*80)
                # Opciones
                print(black('Para asignar una cita llene los datos a continuación...','italic'))
                nro_doc = input('    >>> Número documento del paciente: ')
                services = input('    >>> Seleccione o especifique un servicio: ')
                day = input('    >>> Seleccione o asigne un dia en formato DD/MM/AAAA: ')
                print(cyan(f'\n{'-'*27} La cita ha sido agendada {'-'*27}'))
                
            # Sección 'Historias Clínicas'
            case 3:
                # Títulos
                print('-'*80)
                print(green(f'{'-'*31} Historia Clínica {'-'*31}','bold'))
                print('-'*80)
                # Opciones
                print(black('Para continuar, complete los campos con los datos del paciente...','italic'))
                nro_doc = input('    >>> Número documento del paciente: ')
                print(black('Recuerde que al ingresar una fecha se genera un documento donde se muestra\nsu historia clínica, a partir de la fecha ingresada hasta la actualidad.','italic'))
                date = input('    >>> Ingrese una fecha en formato DD/MM/AAAA: ')
                print(cyan(f'\n{'-'*26} Historial clínico generado {'-'*26}'))
                print('\n\t1. Si\n\t2. No')
                i = int(input('    >>> ¿Desea editarlo?: '))
                while i < 1 or x > 2:
                    if i == 1:
                        print(magenta('\nEditando...'))
                        break
                    elif i == 2:
                        print(yellow(f'\n{'-'*28} Gracias por confirmar {'-'*29}','italic'))
                        break
                    else:
                        print(red(f'\n{'-'*16} Error, por favor seleccione una opción valida {'-'*17}\n'))
                        i = int(input('    >>> ¿Desea editarlo?: '))
                
            # Cerrar Sesión
            case 4:
                print(red(f'{'-'*80}\n{'-'*22} Se ha cerrado sesión correctamente {'-'*22}\n{'-'*80}\n','bold'))
                z = False