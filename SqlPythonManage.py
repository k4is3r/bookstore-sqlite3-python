import sqlite3

def consulta():
    db2 = sqlite3.connect("novelas.db")
    print("Estas en a funcion Consulta")
    db2.row_factory = sqlite3.Row
    consulta = db2.cursor()
    consulta.execute("SELECT * FROM tabla")
    filas = consulta.fetchall()
    lista = []
    for fila in filas:
         s={}
         s['id'] = fila['id']
         s['nombre']=fila['nombre']
         s['autor']=fila['autor']
         s['year']=str(fila['year'])
         lista.append(s)
    consulta.close()
    db2.close()
    return(lista)


def insertar():
    db1 = sqlite3.connect('novelas.db')
    print('Estas en la funcion insertar')
    nombre1= input('Escribe titulo de la novela: ')
    autor1 = input('Escribe el autor de la novela: ')
    year1 = input('Año de la novela: ')
    consulta = db1.cursor()
    sql= """ INSERT INTO tabla(nombre,autor,year) VALUES(?,?,?)"""
    task=(nombre1,autor1,year1)
    consulta.execute(sql,task)
    consulta.close()
    db1.commit()
    db1.close()

def delete_data_db(id_db):
    db1 = sqlite3.connect('novelas.db')
    print('Estas en la funcion delete')
    consulta = db1.cursor()
    sql = """DELETE FROM tabla WHERE id=?"""
    consulta.execute(sql,(id_db,))
    print('Registro eliminado de nuestra DB')
    consulta.close()
    db1.commit()
    db1.close()

def update_data_db(id_db):
    db1 = sqlite3.connect('novelas.db')
    print('Estas en la funcion actualziar')
    consulta = db1.cursor()
    nombre1= input('Titulo actualziar: ')
    autor1 = input('Autor a actualizar: ')
    year1= input('Año actualizar: ')
    sql ="""UPDATE tabla
            SET nombre=?,
                autor=?,
                year=?
            WHERE id=?"""
    task = (nombre1,autor1,year1,id_db)
    consulta.execute(sql,task)
    print('Data atualziado en la DB')
    consulta.close()
    db1.commit()
    db1.close()



if __name__ == '__main__':
    print('say hi coders from slqlite-python DB manage')