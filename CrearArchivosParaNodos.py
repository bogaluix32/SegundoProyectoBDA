import pandas as pd
from unidecode import unidecode
import csv 
import re

def crearArchivoMedicamentos():

    # Rutas de los archivos limpios CSV
    dfArchivo1 = pd.read_csv(r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio1.csv')    
    dfArchivo3 = pd.read_csv(r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio3.csv')
    dfArchivo4 = pd.read_csv(r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio4.csv')
    dfArchivo5 = pd.read_csv(r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio5.csv')

    eliminarsiglasLabOferente(dfArchivo1)
    eliminarsiglasEspecificasLabOferente(dfArchivo1)
    
    # Aplicar la función a la columna "Principio activo o asociación de principios activos"
    dfArchivo1['Principio activo o asociación de principios activos'] = procesarColumnaPrincipioActivo(dfArchivo1['Principio activo o asociación de principios activos'])

    # Selecciona las columnas requeridas de cada archivo
    columnasRequeridasArchivo1 = dfArchivo1[['Nombre del producto farmacéutico', 'Tipo de fármaco','Nombre del laboratorio ofertante', 'Estado', 'Principio activo o asociación de principios activos', 'Precio venta con IVA_Euros', 'Tratamiento de larga duración', 'Medicamento huérfano']]
    columnasRequeridasArchivo4 = dfArchivo4[['Descripción Principio Activo','Nombre Genérico','Presentación','Precio máximo de venta transacción final comercial']]
    columnasRequeridasArchivo5 = dfArchivo5[['DESCRIPCION','PRECIO UNITARIO']]
    columnasRequeridasArchivo3 = dfArchivo3[['Nombre', 'Código de Medicamento']]

    # Realizar las comparaciones y fusionar los datos
    result = columnasRequeridasArchivo1.merge(columnasRequeridasArchivo4, left_on='Principio activo o asociación de principios activos', right_on='Descripción Principio Activo', how='left')
    result = result.merge(columnasRequeridasArchivo5, left_on='Principio activo o asociación de principios activos', right_on='DESCRIPCION', how='left')
    result = result.merge(columnasRequeridasArchivo3, left_on='Principio activo o asociación de principios activos', right_on='Nombre', how='left')

    # Eliminar registros duplicados
    result = result.drop_duplicates()
    result = result.drop_duplicates(subset=['Nombre del producto farmacéutico'])

    # Convertir la columna 'Código de Medicamento' a valores enteros
    result['Código de Medicamento'] = result['Código de Medicamento'].fillna(0).astype(int)

    # Seleccionar las columnas requeridas en el resultado
    resultado_final = result[['Nombre del producto farmacéutico', 'Tipo de fármaco', 'Nombre del laboratorio ofertante', 'Estado', 'Principio activo o asociación de principios activos', 'Precio venta con IVA_Euros', 'Tratamiento de larga duración', 'Medicamento huérfano', 'Código de Medicamento', 'Nombre Genérico', 'Presentación', 'Precio máximo de venta transacción final comercial', 'PRECIO UNITARIO']]

    # Guardar el resultado en un nuevo archivo CSV
    resultado_final.to_csv(r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\nodos\\ArchivoNodoMedicamentos.csv', index=False)

def crearArchivoPrincipiosActivos():
    # Rutas de los archivos limpios CSV
    dfArchivo4 = pd.read_csv(r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio4.csv')

    # Selecciona las columnas requeridas de cada archivo
    columnasRequeridasArchivo4 = dfArchivo4[['Descripción Principio Activo']]

    # Guarda el DataFrame resultante en un archivo CSV
    columnasRequeridasArchivo4.to_csv(r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\nodos\\ArchivoNodoPrincipiosActivos.csv', index=False)

def crearArchivosLaboratorioOferente():
    #Rutas de los archivos limpios CSV
    dfArchivo1 = pd.read_csv(r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio1.csv')
    eliminarsiglasLabOferente(dfArchivo1)
    eliminarsiglasEspecificasLabOferente(dfArchivo1)
    # Selecciona las columnas requeridas de cada archivo
    columnasRequeridasArchivo1 = dfArchivo1[['Nombre del laboratorio ofertante', 'Principio activo o asociación de principios activos']]

    # Guarda el DataFrame resultante en un archivo CSV
    columnasRequeridasArchivo1.to_csv(r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\nodos\\ArchivoNodoLaboratorioOferente.csv', index=False)

def crearArchivoFabricantes():
    #Rutas de los archivos limpios CSV
    dfArchivo1 = pd.read_csv(r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio1.csv')    
    dfArchivo4 = pd.read_csv(r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio4.csv')

    # Selecciona las columnas requeridas de cada archivo
    columnasRequeridasArchivo1 = dfArchivo1[['Principio activo o asociación de principios activos']]
    columnasRequeridasArchivo4 = dfArchivo4[['Descripción Principio Activo','Fabricante']]

    resultado = columnasRequeridasArchivo1.merge(columnasRequeridasArchivo4, left_on='Principio activo o asociación de principios activos', right_on='Descripción Principio Activo', how='left')

    resultado = resultado.drop_duplicates()
    # Eliminar registros vacíos
    resultado = resultado.dropna()

    resultado = resultado[['Descripción Principio Activo', 'Fabricante']]

    # Guarda el DataFrame resultante en un archivo CSV
    resultado.to_csv(r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\\Proyecto Programado 2\\datos\\nodos\\ArchivoNodoFabricantes.csv', index=False)

def crearArchivoDepartamento():
    #Rutas de los archivos limpios CSV
    dfArchivo1 = pd.read_csv(r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio1.csv')    
    dfArchivo5 = pd.read_csv(r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio5.csv')

    # Selecciona las columnas requeridas de cada archivo
    columnasRequeridasArchivo1 = dfArchivo1[['Principio activo o asociación de principios activos']]
    columnasRequeridasArchivo5 = dfArchivo5[['SERVICIO', 'DESCRIPCION']]

    resultado = columnasRequeridasArchivo1.merge(columnasRequeridasArchivo5, left_on='Principio activo o asociación de principios activos', right_on='DESCRIPCION', how='left')

    resultado = resultado.drop_duplicates()
    # Eliminar registros vacíos
    resultado = resultado.dropna()

    resultado = resultado[['SERVICIO', 'DESCRIPCION']]

    # Guarda el DataFrame resultante en un archivo CSV
    resultado.to_csv(r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\\Proyecto Programado 2\\datos\\nodos\\ArchivoNodoDepartamento.csv', index=False)

def eliminarsiglasLabOferente(dataframe):
    # Modifica el contenido del DataFrame in situ
    for index, row in dataframe.iterrows():
        column = row['Nombre del laboratorio ofertante']
        cleaned_column = column.strip().split(",")[0].strip('\"')
        dataframe.at[index, 'Nombre del laboratorio ofertante'] = cleaned_column

def eliminarsiglasEspecificasLabOferente(dataframe):
    # Define una lista de siglas a eliminar
    siglas_a_eliminar = ['S.A.', 'S.A.E.', 'S.L.']

    # Modifica el contenido del DataFrame in situ
    for index, row in dataframe.iterrows():
        column = row['Nombre del laboratorio ofertante']

        # Utiliza una expresión regular para buscar y reemplazar las siglas
        for sigla in siglas_a_eliminar:
            column = column.replace(sigla, '').strip()

        dataframe.at[index, 'Nombre del laboratorio ofertante'] = column

def procesarColumnaPrincipioActivo(columna):
    # Elimina comillas dobles (")
    columna = columna.str.replace('"', '')
    # Reemplaza comas (,) con guiones (-)
    columna = columna.str.replace(',', '-')
    return columna