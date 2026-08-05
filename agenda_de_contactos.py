agenda = {}

print("Agenda de Contactos")
print("-------------------")
print("1. Añadir contacto")
print("2. Buscar contacto")
print("3. Editar contacto")
print("4. Eliminar contacto")
print("5. Mostrar contactos")

eleccion = input("Selecciona una opción:")

if eleccion == "1":
    nombre = input("Añade el nombre: ")
    telefono = input("Añade el numero de telefono: ")
    agenda[nombre] = telefono
    print(f"Contacto guardado exitosamente, nombre del contacto : {nombre}, numero de telefono: {telefono} ")
    
elif eleccion == "2":
    busqueda = input("Escriba el nombre del contacto que desea buscar:")
    if busqueda in agenda:
        usuario_buscado = agenda.get(busqueda)
        print(f"El numero de telefono de {busqueda} es {usuario_buscado}")
    else:
        
        print(f"El contacto {busqueda} no existe en la agenda")
    
elif eleccion == "3":
    contacto_a_editar = input("Ingrese el nombre del contacto a editar: ")
    if contacto_a_editar in agenda:
        nuevo_numero = input(f"Ingrese el nuevo numero de {contacto_a_editar}")
        agenda.update({contacto_a_editar: nuevo_numero})
        print(f"Contacto editado correctamente, el nuevo numero es {nuevo_numero}")
    else:
        print(f"{contacto_a_editar} no existe en la agenda")
    
elif eleccion == "4":
    contacto_a_eliminar = input("Ingrese el nombre del contacto a eliminar: ")
    if contacto_a_eliminar in agenda:
        del agenda[contacto_a_eliminar]
        print(f"El contacto {contacto_a_eliminar} ha sido eliminado")
    else:
        print(f"El contacto {contacto_a_eliminar} no existe")
    
elif eleccion == "5":
    print(f"Todos los contactos de la agenda son : {agenda}")
else:
    print("Opcion no valida, seleccione las opciones existentes")