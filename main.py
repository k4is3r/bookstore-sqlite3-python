import SqlPythonManage

def menu():
    print("""
            DB Manager
            Opciones:
            [I]nresar datos a la BD
            [C]onsultar datos a la BD
            [B]orrar dato en DB
            [A]ctualizar dato en DB
            [S]alir 
            """)
    opcion = input('Ingrese su opcion: ')
    if opcion.lower() == 'i':
        SqlPythonManage.insertar()
        menu()
    elif opcion.lower() == 'c':
        print('_____DB_____')
        listaNovelas = SqlPythonManage.consulta()
        for novela in listaNovelas:
            print('************************')
            print('id: {}'.format(novela['id']))
            print('Libro : {}'.format(novela['nombre']))
            print('Autor: {}'.format(novela['autor']))
            print('Año: {}'.format(novela['year']))
        menu()
    elif opcion.lower() == 'b':
        id_db = int(input('Ingrese el ID el registro a borrar: '))
        SqlPythonManage.delete_data_db(id_db)
        menu()
    elif opcion == 'a':
        id_db = int(input('Introduzca el ID para actualizar: '))
        SqlPythonManage.update_data_db(id_db)
        menu()
    elif opcion.lower() == 's':
        print('Hasta luego....')
    else:
        print('*********ERROR**************')
        print('Introduzca una opcion valida')
        print('*****************************')
        menu()


if __name__ == "__main__":
    menu()