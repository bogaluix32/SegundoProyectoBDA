import pandas as pd
from unidecode import unidecode
import csv 
import re


# Rutas de los archivos originales CSV
#archivo1 = r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\originales\\1.1_Nombre_de_productos_genéricos_y_Farmaceutica.csv'
#archivo2 = r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\originales\\2._Catálogo_de_Categorías_de_Medicamentos_CCSS.csv'
#archivo3 = r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\originales\\3._muestra_Medicamentos_CCSS_clasificados.csv'
#archivo4 = r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\originales\\4._Principios_Activos_y_Presentación.csv'
#archivo5 = r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\originales\\6-Medicamentos_adquiridos_por_hospital.csv'


#Eliminacion de columnas innecesarias para cada archivo (Archivo 1, Archivo 4 y Archivo 5)
#Listas de columnas a eliminar
#columnasArchivo1 = ["Aportación del beneficiario", "Nombre de la agrupación homogénea del producto sanitario", "Diagnóstico hospitalario", "Especial control médico"]
#columnasArchivo4 = ["ATC", "Forma Farmacéutica", "detalles del producto", "Tamaño de Caja o presentación"]
#columnasArchivo5 = ["MES","FECHA","TIPO","UNIDAD","PIEZAS SOLICITADAS","PIEZAS SURTIDAS"]

def eliminacionColumnas(archivo, columnas_a_eliminar):
    # Cargar el archivo CSV
    # Eliminar las columnas especificadas
    nuevoArchivo = archivo.drop(columns=columnas_a_eliminar, errors="ignore")
    return nuevoArchivo

# Llamar a la función para realizar la eliminación de columnas en los archivos
#nuevoArchivo1 = eliminacionColumnas(archivo1, columnasArchivo1)
#nuevoArchivo4 = eliminacionColumnas(archivo4, columnasArchivo4)
#nuevoArchivo5 = eliminacionColumnas(archivo5, columnasArchivo5)

#Leer los archivos faltantes 
#nuevoArchivo2 = pd.read_csv(archivo2)
#nuevoArchivo3 = pd.read_csv(archivo3)

#Ahora los 5 archivos ya estan asignados con las variables de nuevoArchivo# y listos para normalizar




#------Funciones Mixtas------#

#Funcion quitar tildes y cambiar mayusculas, recibe un objeto de tipo nuevoArchivo
def sinTildesMayuscula(dataframe):
    # Función para quitar tildes y convertir a mayúsculas
    def normalizar_texto(texto):
        if isinstance(texto, str):
            # Quitar tildes y convertir a mayúsculas
            texto_normalizado = unidecode(texto).upper()
            return texto_normalizado
        return texto

    # Aplicar la función a todas las celdas del DataFrame
    dataframe = dataframe.applymap(normalizar_texto)

    return dataframe
#Fin

#Funcion para eliminar todo despues del primer numero
def limpiarNombre(nuevoArchivo):
    # Crea una lista para almacenar las filas limpias
    filas_limpias = []

    for row in nuevoArchivo.iterrows():
        row = row[1].values.tolist()  # Convertir la fila a una lista
        if row:
            # Busca la primera ocurrencia de un dígito en el primer elemento de la fila
            match = re.search(r'\d', row[0])

            if match:
                numero_index = match.start()  # Obtiene el índice del primer dígito encontrado
                row[0] = row[0][:numero_index]  # Elimina todo después del primer dígito

                # Ahora, elimina todos los espacios vacíos al final del texto
                row[0] = row[0].rstrip()
            filas_limpias.append(row)  # Agrega la fila modificada a la lista filas_limpias

    return pd.DataFrame(filas_limpias, columns=nuevoArchivo.columns)
#Fin



#------Funciones Especificas------#


#---Archivo 1--
# Función 1.1 para eliminar datos duplicados
def eliminarProductoDuplicados(dataframe):
    # Eliminar datos duplicados en la columna "Descripción Principio Activo"
    dataframe.drop_duplicates(subset=["Nombre del producto farmacéutico"], keep="first", inplace=True)
    return dataframe
#Fin




#---Archivo 2---
# Función 2.1 para reemplazar "/" "y" "e" por comas en la columna DESCRIPCIÓN
def normalizarCatalogoDeMedicamentos(nuevoArchivo2):
    # Reemplazar "/" y "y" y "e" por comas en la columna DESCRIPCIÓN
    nuevoArchivo2['DESCRIPCIÓN'] = nuevoArchivo2['DESCRIPCIÓN'].str.replace(
        '/', ',').str.replace('y', ',').str.replace(' e ', ',')
    
    return nuevoArchivo2
#Fin

# Función 2.2 dividir las categorias manteniendo el numero de grupo
def dividirCategorias(nuevoArchivo2):
    #llamar a la primera funcion 
    nuevoArchivo2 = normalizarCatalogoDeMedicamentos(nuevoArchivo2)

    # Dividir las descripciones por comas y convertir en filas separadas
    nuevoArchivo2['DESCRIPCIÓN'] = nuevoArchivo2['DESCRIPCIÓN'].str.split(',')
    nuevoArchivo2 = nuevoArchivo2.explode('DESCRIPCIÓN')

    #Funcion auxiliar1 necesaria para quitar comas repetidas
    def filtro_descripcion(descripcion):
        return (descripcion is not None) and (not any(c.isdigit() for c in descripcion)) and (descripcion.strip() != '')

    # Aplicar Funcion auxiliar1 
    nuevoArchivo2 = nuevoArchivo2[nuevoArchivo2['DESCRIPCIÓN'].apply(filtro_descripcion)]

    #Funcion auxiliar2 necesaria para quitar espacios iniciales
    def eliminar_espacios(descripcion):
        return descripcion.lstrip() if isinstance(descripcion, str) else descripcion

    # Aplicar Funcion auxiliar2
    nuevoArchivo2['DESCRIPCIÓN'] = nuevoArchivo2['DESCRIPCIÓN'].apply(eliminar_espacios)

    return nuevoArchivo2
#Fin


# Función 2.3 para eliminar datos duplicados
def eliminarDescripcionDuplicados(dataframe):
    # Eliminar datos duplicados en la columna "Descripción Principio Activo"
    dataframe.drop_duplicates(subset=["DESCRIPCIÓN"], keep="first", inplace=True)
    return dataframe
#Fin


#---Archivo 3---
# Función 3.1 para eliminar todo Despues Del Guion
def eliminarDespuesDelGuion(dataframe):
    # Verificar si la segunda columna existe en el DataFrame
    if len(dataframe.columns) < 2:
        raise ValueError("El DataFrame no tiene una segunda columna.")

    # Obtener el nombre de la segunda columna
    columna_nombre = dataframe.columns[1]

    # Aplicar la función de eliminación del guion a la segunda columna
    dataframe[columna_nombre] = dataframe[columna_nombre].str.split('-').str[0]

    return dataframe
#Fin


# Función 3.2 para eliminar datos duplicados
def eliminarNomnbresDuplicados(dataframe):
    # Eliminar datos duplicados en la columna "Descripción Principio Activo"
    dataframe.drop_duplicates(subset=["Nombre"], keep="first", inplace=True)
    return dataframe
#Fin



#---Archivo 4---
# Función 4.1 para eliminar datos duplicados
def eliminarPrincipiosDuplicados(dataframe):
    # Eliminar datos duplicados en la columna "Descripción Principio Activo"
    dataframe.drop_duplicates(subset=["Descripción Principio Activo"], keep="first", inplace=True)
    return dataframe
#Fin


#---Archivo 5---
# Función 5.1 para eliminar datos duplicados
def limpiarDescripcion(dataframe):
    # Limpiar la columna "DESCRIPCION"
    dataframe["DESCRIPCION"] = dataframe["DESCRIPCION"].str.split(',').str[0]
    dataframe["DESCRIPCION"] = dataframe["DESCRIPCION"].str.split().str[0]
    return dataframe
#Fin



#Normalizacion de todos los archivos

#Archivo1
def normalizarArchivo1(nuevoArchivo1):
    nuevoArchivo11 = limpiarNombre(nuevoArchivo1)
    nuevoArchivo11 = sinTildesMayuscula(nuevoArchivo11)
    nuevoArchivo11 = eliminarProductoDuplicados(nuevoArchivo11)
    nuevoArchivo11 = eliminarProductoDuplicados(nuevoArchivo11)
    #eliminar los registros duplicados. 
    #mayusculas y tildes
    return nuevoArchivo11

#Archivo2
def normalizarArchivo2(nuevoArchivo2):
    nuevoArchivo2 = dividirCategorias(nuevoArchivo2)
    nuevoArchivo2 = sinTildesMayuscula(nuevoArchivo2)
    nuevoArchivo2 = eliminarDescripcionDuplicados(nuevoArchivo2) ###############
    return nuevoArchivo2

#Archivo3
def normalizarArchivo3(nuevoArchivo3):
    nuevoArchivo33 = limpiarNombre(nuevoArchivo3)
    nuevoArchivo33 = eliminarDespuesDelGuion(nuevoArchivo33)
    nuevoArchivo33 = eliminarNomnbresDuplicados(nuevoArchivo33) ###############
    nuevoArchivo33 = sinTildesMayuscula(nuevoArchivo33)
    return nuevoArchivo33

#Archivo4
def normalizarArchivo4(nuevoArchivo4):
    nuevoArchivo44 = limpiarNombre(nuevoArchivo4)
    nuevoArchivo44 = eliminarPrincipiosDuplicados(nuevoArchivo44)
    nuevoArchivo44 = sinTildesMayuscula(nuevoArchivo44)
    return nuevoArchivo44

#Archivo5
def normalizarArchivo5(nuevoArchivo5):
    nuevoArchivo55 = limpiarDescripcion(nuevoArchivo5)
    nuevoArchivo55 = sinTildesMayuscula(nuevoArchivo55)
    return nuevoArchivo55

""" 
def main():
    #--Normalizar archivo 1
    nuevoArchivo1 = normalizarArchivo1(nuevoArchivo1)
    #--Guardar el archivo 1
    nombre_archivo_limpio = r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio1.csv'
    nuevoArchivo1.to_csv(nombre_archivo_limpio, index=False)
    print("Normalizacion de archivo 1")


    #--Normalizar archivo 2--
    nuevoArchivo2 = normalizarArchivo2(nuevoArchivo2)
    #--Guardar el archivo 2--
    nombre_archivo_limpio2 = r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio2.csv'
    nuevoArchivo2.to_csv(nombre_archivo_limpio2, index=False)
    print("Normalizacion de archivo 2")


    #Normalizar archivo 3
    nuevoArchivo3 = normalizarArchivo3(nuevoArchivo3)
    #--Guardar el archivo 3
    nombre_archivo_limpio3 = r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio3.csv'
    nuevoArchivo3.to_csv(nombre_archivo_limpio3, index=False)
    print("Normalizacion de archivo 3")


    #--Normalizar archivo 4
    nuevoArchivo4 = normalizarArchivo4(nuevoArchivo4)
    #--Guardar el archivo 4
    nombre_archivo_limpio4 = r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio4.csv'
    nuevoArchivo4.to_csv(nombre_archivo_limpio4, index=False)
    print("Normalizacion de archivo 4")


    #Normalizar archivo 5
    nuevoArchivo5 = normalizarArchivo5(nuevoArchivo5)
    #Guardar el archivo 5
    nombre_archivo_limpio5 = r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio5.csv'
    nuevoArchivo5.to_csv(nombre_archivo_limpio5, index=False)
    print("Normalizacion de archivo 5")

main()"""