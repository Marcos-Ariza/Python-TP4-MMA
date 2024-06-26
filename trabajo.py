class Jugador1:
  def __init__(self, nombre, equipo, edad, goles, posicion, numero, pais, partidos, reconocimientos):
      self.nombre = nombre
      self.equipo = equipo
      self.edad = edad
      self.goles = goles
      self.posicion = posicion
      self.numero = numero
      self.pais = pais
      self.partidos = partidos
      self.reconocimientos = reconocimientos

jugadores = []


jugadorEJ = Jugador1("Lionel Messi", "inter di miami fulbo clu", 36, 700, "Delantero", 30, "Argentina", 300, ["Balón de Oro", "Bota de Oro"])
jugadores.append(jugadorEJ)

while True:
  print("Qué acción desea realizar:")
  print("1 - Crear un nuevo jugador de fútbol.")
  print("2 - Mostrar la información de un jugador existente.")
  print("3 - Actualizar la información de un jugador existente.")
  print("4 - Calcular el promedio de goles por partido de un jugador.")
  print("5 - Verificar si un jugador es un goleador.")
  print("6 - Agregar un premio o reconocimiento a un jugador.")
  print("7 - Eliminar un premio o reconocimiento de un jugador.")
  print("0 - Salir del programa.")

  cod = int(input("Escriba el número por favor: "))

  if cod == 1:
      nombre = input("Nombre del jugador: ")
      equipo = input("Equipo del jugador: ")
      edad = int(input("Edad del jugador: "))
      goles = int(input("Cantidad de goles del jugador: "))
      posicion = input("Posición del jugador: ")
      numero = int(input("Número de camiseta del jugador: "))
      pais = input("País del jugador: ")
      partidos = int(input("Cantidad de partidos jugados por el jugador: "))
      reconocimientos = input("Reconocimientos del jugador (separados por comas): ").split(", ")
      jugador_nuevo = Jugador1(nombre, equipo, edad, goles, posicion, numero, pais, partidos, reconocimientos)
      jugadores.append(jugador_nuevo)
      print("¡Jugador creado con éxito!")

  elif cod == 2:
    if not jugadores:
      print("No hay jugadores registrados.")
    else:
      print("Jugadores existentes:")
      for jugador in jugadores:
          print(jugador.nombre)
      nombre_buscar = input("Ingrese el nombre del jugador: ")
      encontrado = False
      for jugador in jugadores:
          if jugador.nombre == nombre_buscar:
              print("Información del jugador:")
              print("Nombre:", jugador.nombre)
              print("Equipo:", jugador.equipo)
              print("Edad:", jugador.edad)
              print("Goles:", jugador.goles)
              print("Posición:", jugador.posicion)
              print("Número:", jugador.numero)
              print("País:", jugador.pais)
              print("Partidos:", jugador.partidos)
              print("Reconocimientos:", jugador.reconocimientos)
              encontrado = True
              break
      if not encontrado:
          print("No se encontró ningún jugador con ese nombre.")

  elif cod == 3:

    print("Jugadores existentes:")
    for jugador in jugadores:
        print(jugador.nombre)
    nombre_jugador = input("Ingrese el nombre del jugador que desea actualizar: ")
    for jugador in jugadores:
        if jugador.nombre == nombre_jugador:
            print("Ingrese los nuevos datos del jugador:")
            jugador.nombre = input("Nombre: ")
            jugador.equipo = input("Equipo: ")
            jugador.edad = int(input("Edad: "))
            jugador.goles = int(input("Goles: "))
            jugador.posicion = input("Posición: ")
            jugador.numero = int(input("Número: "))
            jugador.pais = input("País: ")
            jugador.partidos = int(input("Partidos: "))
            jugador.reconocimientos = input("Reconocimientos (separados por coma): ").split(", ")
            print("¡Datos actualizados con éxito!")
            break
    else:
        print("El jugador no se encuentra en la lista.")

  elif cod == 4:
    nombre_buscar = input("Ingrese el nombre del jugador: ")
    encontrado = False
    for jugador in jugadores:
      if jugador.nombre == nombre_buscar:
          if jugador.partidos > 0:
              promedio_goles = jugador.goles / jugador.partidos
              print(f"El promedio de goles por partido de {jugador.nombre} es: {promedio_goles:.2f}")
          else:
              print("El jugador no ha jugado ningún partido, por lo tanto, no se puede calcular el promedio de goles.")
          encontrado = True
          break
    if not encontrado:
      print("No se encontró ningún jugador con ese nombre.")


  elif cod == 5:
      nombre_buscar = input("Ingrese el nombre del jugador: ")
      encontrado = False
      for jugador in jugadores:
          if jugador.nombre == nombre_buscar:
              if jugador.goles > 50:
                  print("El jugador es un goleador.")
              else:
                  print("El jugador no es considerado un goleador.")
              encontrado = True
              break
      if not encontrado:
          print("No se encontró ningún jugador con ese nombre.")

  elif cod == 6:
      nombre_jugador = input("Ingrese el nombre del jugador al que desea agregar un premio o reconocimiento: ")
      for jugador in jugadores:
          if jugador.nombre == nombre_jugador:
              nuevo_reconocimiento = input("Ingrese el nuevo premio o reconocimiento: ")
              jugador.reconocimientos.append(nuevo_reconocimiento)
              print("¡Premio o reconocimiento agregado con éxito!")
              break
      else:
          print("El jugador no se encuentra en la lista.")

  elif cod == 7:
      nombre_jugador = input("Ingrese el nombre del jugador al que desea eliminar un premio o reconocimiento: ")
      for jugador in jugadores:
          if jugador.nombre == nombre_jugador:
              if jugador.reconocimientos:
                  print("Reconocimientos actuales del jugador:", jugador.reconocimientos)
                  reconocimiento_eliminar = input("Ingrese el premio o reconocimiento que desea eliminar: ")
                  if reconocimiento_eliminar in jugador.reconocimientos:
                      jugador.reconocimientos.remove(reconocimiento_eliminar)
                      print("¡Premio o reconocimiento eliminado con éxito!")
                  else:
                      print("El premio o reconocimiento especificado no está presente en la lista.")
              else:
                  print("El jugador no tiene ningún premio o reconocimiento registrado.")
              break
      else:
          print("El jugador no se encuentra en la lista.")


  elif cod == 0:
      print("Saliendo del programa...")
      break

  else:
      print("Opción no válida. Por favor, seleccione una opción válida.")

##############
