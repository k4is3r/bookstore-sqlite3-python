import sqlite3



#Welcom coder
if __name__ == '__main__':
    conexion = sqlite3.connect('novelas.db')
    consulta = conexion.cursor()
    tabla="""CREATE TABLE IF NOT EXISTS tabla(
             id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
             nombre VARCHAR(30) NOT NULL, 
             autor VARCHAR(40) NOT NULL, 
             year INTEGER(9) NOT NULL);"""
    print(tabla)
    if(consulta.execute(tabla)):
        print("La tabla fue creada")
    else:
        print("La tabla no fue creada")
    consulta.close()
    conexion.commit()
    conexion.close()
