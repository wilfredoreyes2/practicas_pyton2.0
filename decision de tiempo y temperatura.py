decision =0;    
while decision !=3:
    decision = int(input('Elige el tipo de operación: 1 = conversión de temperatura, 2 = conversión de tiempo, salir = 3: '))

    if decision == 1:
        degreesF = float(input('Ingresa la temperatura en grados Fahrenheit: '))
        # Realiza la conversión
        degreesC = 5/9 * (degreesF - 32)
        # Reporta el resultado
        print(degreesF, 'grados Fahrenheit =', degreesC, 'grados Celsius')

    elif decision == 2:
        seconds = int(input("Por favor, ingresa la cantidad de segundos: "))
        # Primero, calcula la cantidad de horas en el número de segundos dado
        # Nota: división entera con posible truncamiento
        hours = seconds // 3600  # 3600 segundos = 1 hora
        # Calcula los segundos restantes después de tener en cuenta las horas
        seconds = seconds % 3600
        # Luego, calcula la cantidad de minutos en los segundos restantes
        minutes = seconds // 60   # 60 segundos = 1 minuto
        # Calcula los segundos restantes después de tener en cuenta los minutos
        seconds = seconds % 60
        # Reporta los resultados
        print(hours, "hr,", minutes, "min,", seconds, "seg")

    else:
        print('Opción no válida. Por favor, selecciona 1 o 2 para la conversión de temperatura o tiempo.')

