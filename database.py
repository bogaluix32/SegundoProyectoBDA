from neo4j import GraphDatabase
import pandas as pd
from io import StringIO
import streamlit as st
#Conexión de Licho
URI = "bolt://localhost:7687"
AUTH = ("neo4j","123456789")

#funcion que define la consulta a ejcutar en neo
def crear_nodo(tx, etiqueta, datos):
    query = (
        f"CREATE (n:`{etiqueta}` {{"
        f"Nombre_del_producto_farmacéutico: '{datos['Nombre del producto farmacéutico']}', "
        f"Tipo_de_fármaco: '{datos['Tipo de fármaco']}', "
        f"Estado: '{datos['Estado']}', "
        f"Precio_venta_con_IVA_Euros: '{datos['Precio venta con IVA_Euros']}', "
        f"Tratamiento_de_larga_duración: '{datos['Tratamiento de larga duración']}', "
        f"Medicamento_huérfano: '{datos['Medicamento huérfano']}', "
        f"Código_de_Medicamento: '{datos['Código de Medicamento']}', "
        f"Nombre_Genérico: '{datos['Nombre Genérico']}', "
        f"Presentación: '{datos['Presentación']}', "
        f"Precio_máximo_de_venta_transacción_final_comercial: '{datos['Precio máximo de venta transacción final comercial']}', "
        f"PRECIO_UNITARIO: '{datos['PRECIO UNITARIO']}'"
        "})"
    )
    tx.run(query)

#función para crear un nodo en la base de datos
def crearNodoMedicamento():
    # Abre una conexión a la base de datos
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        # Abre una sesión de Neo4j
        with driver.session() as session:
            # Lee los datos del archivo_unificado.csv y crea nodos en la base de datos
            with open(r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\\Proyecto Programado 2\\datos\\nodos\\ArchivoNodoMedicamentos.csv', 'r') as file:
                # Procesa el archivo CSV y crea nodos
                for line in file.readlines()[:20]: #leemos los primeros 20 registros
                    datos = line.strip().split(',')  # como los datos se seperan por comas entonces hacemos split
                    etiqueta = "Medicamento"  # definimos la etiqueta del nodo
                    datos_dict = { #cargamos los atributos del nodo mediante un diccionario
                        'Nombre del producto farmacéutico' : datos[0], #datos[x] para acceder a cada dato del los registros, recordemos que el registro es una tupla.
                        'Tipo de fármaco': datos[1],
                        'Estado': datos[2],
                        'Precio venta con IVA_Euros': datos[3],
                        'Tratamiento de larga duración': datos[4],
                        'Medicamento huérfano': datos[5],
                        'Código de Medicamento': datos[6],
                        'Nombre Genérico': datos[7],
                        'Presentación': datos[8],
                        'Precio máximo de venta transacción final comercial': datos[9],
                        'PRECIO UNITARIO': datos[10]
                    }
                    # Llama a la función para crear el nodo
                    session.write_transaction(crear_nodo, etiqueta, datos_dict)

def validarConexionNeo4j():
    try:
        # Intenta abrir una conexión a la base de datos
        with GraphDatabase.driver(URI, auth=AUTH) as driver:
            with driver.session() as session:
                # Realiza una consulta simple para verificar la conexión
                result = session.run("RETURN 1 as result")

                # Comprueba si la consulta fue exitosa
                for record in result:
                    if record["result"] == 1:
                        print("Conexión exitosa a Neo4j")
                        return True

        # Si llegamos a este punto, la conexión no fue exitosa
        print("No se pudo establecer la conexión a Neo4j")
        return False

    except Exception as e:
        print(f"Error de conexión: {str(e)}")
        return False
