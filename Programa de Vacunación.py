##Programa de Vacunación

#########################################
def programaVacuna():
  estado = None
  pacientesVacunados = 0
  sumEdad = 0
  citas = 0
  promEdad = 0
  while estado != "PARAR":
    pacienteapto = True
    razon = "\nNo se puede vacunar porque:"
###########################################
    print("¿Presenta Cedula o Tarjeta de identidad?\nIngrese: SI o NO")
    n = input()
    if n == "NO":
      pacienteapto = False
      razon = razon + "\nFalta cédula o Tarjeta de identidad."
###########################################
    print("¿Se ha vacunado recientemente en un plazo de 21 días?\nIngrese: SI o NO")
    n = input()
    if n == "SI":
      pacienteapto = False
      razon = razon + "\nRecibió la vacuna dentro de los 21 días."
###############################################
    print("¿Recibió una vacuna contra otra enfermedad en un plazo de 1 mes?\nIngrese: SI o NO")
    n = input()
    if n == "SI":
      pacienteapto = False
      razon = razon + "\nRecibió una vacuna contra otra enfermedad en un plazo de 1 mes."
################################################
    print("¿Tuvo recientemente Covid-19 o algún sintoma relacionado?\nIngrese: SI o NO")
    n = input()
    if n == "SI":
      pacienteapto = False
      razon = razon + "\nTuvo Covid-19 o sintomas asociados."
#################################################
    if pacienteapto == True:
      print("\nPaciente apto para vacuna Covid19, por favor, siga a la mesa de inscripción.\n")
    else:
      print(razon)
    
    if pacienteapto == True:
      ########################
      print("Ingrese nombre del paciente")
      Nombre = input()
      print("Ingrese apellido del paciente")
      Apellido = input()
      #########################
      print("Seleccione el sexo del paciente:\n1: Masculino\n2: Femenino")
      Dato = int(input())
      if Dato == 1:
        Sexo = "Masculino"
      elif Dato == 2:
        Sexo = "Femenino"
      ########################
      print("Ingrese edad del paciente")
      Edad = int(input())
      sumEdad += Edad
      ########################
      print("Ingrese barrio del paciente")
      Barrio = input()
      #########################
      print("Dosis a recibir:\n1.Primera\n2.Segunda")
      Dato2 = int(input())
      if Dato2 == 1:
        Dosis = "Primera"
      elif Dato2 == 2:
        Dosis = "Segunda"
      ###########################
      print("Ingrese EPS del paciente")
      EPS = input()
      ###########################
      print("¿El paciente tiene cita para el día de hoy?\nIngrese: SI o NO")
      res = input()
      if res == "NO":
        citas +=1
        print("El paciente",Nombre, Apellido,"tiene cita asignada para el dia de mañana.")
      else:
        pacientesVacunados +=1

    print("¿Desea agregar un nuevo registro?\nPara cerrar el sistema ingresar el comando PARAR\nPara Seguir agregando registror pulsar Enter.")
    estado = str(input())
  if pacientesVacunados > 0:
    promEdad = sumEdad/pacientesVacunados
    registros = citas + pacientesVacunados
    print("\nResultados del día de de hoy","\nPacientes registrados: ",registros,"\nPacientes Vacunados: ",pacientesVacunados, "\nPromedio de la edad de los pacientes: ", promEdad, "\nCitas asignadas el día de hoy: ", citas)
  else:
    registros = citas + pacientesVacunados
    print("\nResultados del día de de hoy","\nPacientes registrados: ",registros,"\nPacientes Vacunados: ",pacientesVacunados, "\nPromedio de la edad de los pacientes: ", promEdad, "\nCitas asignadas el día de hoy: ", citas)
programaVacuna()
