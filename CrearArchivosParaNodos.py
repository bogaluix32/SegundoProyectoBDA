import pandas as pd
from unidecode import unidecode
import csv 
import re



def crearArchivoMedicamentos():

    # Rutas de los archivos limpios CSV
    dfArchivo1 = pd.read_csv(r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio1.csv')
    dfArchivo2 = pd.read_csv(r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio2.csv')
    dfArchivo3 = pd.read_csv(r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio3.csv')
    dfArchivo4 = pd.read_csv(r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio4.csv')
    dfArchivo5 = pd.read_csv(r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio5.csv')

    # Selecciona las columnas requeridas de cada archivo
    columnasRequeridasArchivo1 = dfArchivo1[['Nombre del producto farmacéutico', 'Tipo de fármaco', 'Estado', 'Precio venta con IVA_Euros', 'Tratamiento de larga duración', 'Medicamento huérfano']]
    columnasRequeridasArchivo3 = dfArchivo3[['Código de Medicamento']]
    columnasRequeridasArchivo4 = dfArchivo4[['Nombre Genérico','Presentación','Precio máximo de venta transacción final comercial']]
    columnasRequeridasArchivo5 = dfArchivo5[['PRECIO UNITARIO']]

    # Concatena los DataFrames en uno solo
    archivoResultante = pd.concat([columnasRequeridasArchivo1, columnasRequeridasArchivo3, columnasRequeridasArchivo4, columnasRequeridasArchivo5], axis=1)

    # Guarda el DataFrame resultante en un archivo CSV
    archivoResultante.to_csv(r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\nodos\\ArchivoNodoMedicamentos.csv', index=False)
