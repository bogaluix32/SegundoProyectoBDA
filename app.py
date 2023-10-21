# Importar las librerías necesarias
import streamlit as st
import pandas as pd
import database
import Normalizacion_19_10_15h_55m as normalizacion

columnasArchivo1 = ["Aportación del beneficiario", "Nombre de la agrupación homogénea del producto sanitario", "Diagnóstico hospitalario", "Especial control médico"]
columnasArchivo4 = ["ATC", "Forma Farmacéutica", "detalles del producto", "Tamaño de Caja o presentación"]
columnasArchivo5 = ["MES","FECHA","TIPO","UNIDAD","PIEZAS SOLICITADAS","PIEZAS SURTIDAS"]



# Función para cargar y procesar archivos CSV
def cargar_archivos_csv():
    # Permitir al usuario cargar archivos CSV
    uploaded_files = st.file_uploader("Subir archivos", type=["csv"], accept_multiple_files=True)

    # Botón para iniciar el procesamiento de nodos
    if st.button("Cargar Nodos"):
        if uploaded_files:

            primerArchivo = pd.read_csv(uploaded_files[0], low_memory=False)
            segundoArchivo = pd.read_csv(uploaded_files[1], low_memory=False)
            tercerArchivo = pd.read_csv(uploaded_files[2], low_memory=False)
            cuartoArchivo = pd.read_csv(uploaded_files[3], low_memory=False)
            quintoArchivo = pd.read_csv(uploaded_files[4], low_memory=False)
            # Llamar a la función para realizar la eliminación de columnas en los archivos
            nuevoArchivo1 = normalizacion.eliminacionColumnas(primerArchivo, columnasArchivo1)
            nuevoArchivo4 = normalizacion.eliminacionColumnas(cuartoArchivo, columnasArchivo4)
            nuevoArchivo5 = normalizacion.eliminacionColumnas(quintoArchivo, columnasArchivo5)

            #Leer los archivos faltantes 
            nuevoArchivo2 = segundoArchivo
            nuevoArchivo3 = tercerArchivo

            #--Guardar el archivo 1
            nuevoArchivo1 = normalizacion.normalizarArchivo1(nuevoArchivo1)
            nombre_archivo_limpio = r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio1.csv'
            nuevoArchivo1.to_csv(nombre_archivo_limpio, index=False)
            print("Normalizacion de archivo 1")

            #--Guardar el archivo 2--
            nuevoArchivo2 = normalizacion.normalizarArchivo2(nuevoArchivo2)
            nombre_archivo_limpio2 = r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio2.csv'
            nuevoArchivo2.to_csv(nombre_archivo_limpio2, index=False)
            print("Normalizacion de archivo 2")

            #--Guardar el archivo 3
            nuevoArchivo3 = normalizacion.normalizarArchivo3(nuevoArchivo3)
            nombre_archivo_limpio3 = r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio3.csv'
            nuevoArchivo3.to_csv(nombre_archivo_limpio3, index=False)
            print("Normalizacion de archivo 3")

            #--Guardar el archivo 4
            nuevoArchivo4 = normalizacion.normalizarArchivo4(nuevoArchivo4)
            nombre_archivo_limpio4 = r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio4.csv'
            nuevoArchivo4.to_csv(nombre_archivo_limpio4, index=False)
            print("Normalizacion de archivo 4")

            #Guardar el archivo 5
            nuevoArchivo5 = normalizacion.normalizarArchivo5(nuevoArchivo5)
            nombre_archivo_limpio5 = r'C:\\Users\\Luis Antonio Jimenez\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\Proyecto Programado 2\\datos\\limpios\\ArchivoLimpio5.csv'
            nuevoArchivo5.to_csv(nombre_archivo_limpio5, index=False)
            print("Normalizacion de archivo 5")

            # Aquí podrías realizar más operaciones con el DataFrame df si lo deseas
        else:
            st.warning("Por favor, suba los archivos CSV primero.")  # Mensaje de advertencia si no se cargaron archivos

# Función principal de la aplicación
def main():
    # Configurar el título de la página
    st.title("Proyecto 2 Bases de datos Avanzadas")
    
    # Crear el menú principal con dos opciones: "Subir Datos" y "Consultas"
    menu = ["Subir Datos", "Consultas"]
    choice = st.sidebar.selectbox("Menú", menu)  # Permite al usuario seleccionar una opción del menú en el sidebar

    # Lógica condicional basada en la opción seleccionada
    if choice == "Subir Datos":
        # Si el usuario elige "Subir Datos," mostrar esta sección
        st.subheader("Sección para Subir Datos")
        cargar_archivos_csv()


main()  # Llamar a la función main() para iniciar la aplicación