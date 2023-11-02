# Importar las librerías necesarias
import streamlit as st
import pandas as pd
import database as db
import Normalizacion_19_10_15h_55m as normalizacion
import CrearArchivosParaNodos

columnasArchivo1 = ["Aportación del beneficiario", "Nombre de la agrupación homogénea del producto sanitario", "Diagnóstico hospitalario", "Especial control médico"]
columnasArchivo4 = ["ATC", "Forma Farmacéutica", "detalles del producto", "Tamaño de Caja o presentación"]
columnasArchivo5 = ["MES","FECHA","TIPO","UNIDAD","PIEZAS SOLICITADAS","PIEZAS SURTIDAS"]

# Función para cargar y procesar archivos CSV
def cargar_archivos_csv():
    # Permitir al usuario cargar archivos CSV
    uploaded_files = st.file_uploader("Subir archivos", type=["csv"], accept_multiple_files=True)

    # Botón para iniciar el procesamiento de nodos
    if st.button("Cargar Nodos"):
        uploaded_files = True
        if uploaded_files:
            """
            # Leer los archivos CSV
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
            """
            #Creamos los archivos que necesitamos para los nodos
            #CrearArchivosParaNodos.crearArchivoMedicamentos()
            #print("Archivo para el nodo medicamentos creado con éxito")
            #CrearArchivosParaNodos.crearArchivoPrincipiosActivos()
            #print("Archivo para el nodo principios activos creado con éxito")
            #CrearArchivosParaNodos.crearArchivosLaboratorioOferente()
            #print("Archivo para el nodo laboratorio oferente creado con éxito")
            #CrearArchivosParaNodos.crearArchivoFabricantes()
            #print("Archivo para el nodo fabricantes creado con éxito")
            #CrearArchivosParaNodos.crearArchivoDepartamento()
            #print("Archivo para el nodo departamento creado con éxito")

            # Llama a la función para validar la conexión
            #if db.validarConexionNeo4j():
                # Realiza otras operaciones si la conexión es exitosa
                #print("La conexión es válida, puedes realizar otras operaciones en Neo4j.")
            #else:
                # Maneja el caso en el que la conexión no sea válida
                #print("No se pudo validar la conexión a Neo4j.")

            """
            #Creamos los nodos medicamentos en neo4j
            db.crearNodoMedicamento()
            print("Nodos Medicamentos creados con éxito")
            #Creamos los nodos principios activos en neo4j
            db.crearNodoPrincipioActivo()
            print("Nodos Principios Activos creados con éxito")
            #Creamos los nodos categoria medicamento en neo4j
            db.crearNodoCategoriaMedicamentos()
            print("Nodos Categoría Medicamentos creados con éxito")
            #Creamos los nodos laboratorio oferente en neo4j
            db.crearNodoLaboratorioOferente()
            print("Nodos Laboratorio Oferente creados con éxito")
            #Creamos los nodos Departamento en neo4j
            db.crearNodoDepartamento()
            print("Nodos Departamento creados con éxito")
            #Creamos los nodos Fabricante en neo4j
            db.crearNodoFabricante()
            print("Nodos Fabricante creados con éxito")
            print("Nodos creados con éxito")
            """
            #Creamos las relaciones entre los nodos
            #db.crearRelacionMedicamentoDepartamento()
            #db.crearRelacionLaboratorioFabricante()
            #db.crearRelacionMedicamentoLaboratorio()
            #db.crearRelacionMedicamentoPrincipioActivo()
            #db.crearRelacionMedicamentoCategoriaMedicamento()

            # Ejemplo de uso Consulta 3
            print("--- Consulta 3 ---")
            p = "CLARITROMICINA"
            medicamentos = db.buscar_medicamentos_por_principio_activo(p)

            # Imprime los medicamentos encontrados
            for medicamento in medicamentos:
                print(medicamento)
            
            # Ejemplo de uso Consulta 5
            print("--- Consulta 5 ---")
            x = "ACICLOVIR"
            resultados = db.consultar_info_principio_activo(x)

            # Imprime los resultados
            for resultado in resultados:
                print("Laboratorio:", resultado["Laboratorio"])
                print("Presentación:", resultado["Presentación"])
                print("Categorías:", resultado["Categorias"])
            """
            print("--- Consulta 1 ---")
            x = "ANTIBIOTICOS"
            codigo = db.axuliar_BuscarCategoria(x)
            print(codigo)
            principioActivo = db.axuliar_BuscarMedicamentoUsandoCodigo(codigo)
            print(principioActivo)
            detalleMedicamento = db.reporteMedicamentosPotencialmenteAdquiridos(principioActivo)
            for i in detalleMedicamento:
                print("Nombre Medicamento:", i["nombre"])
                print("Principio Activo:", i["principio"])
                print("Fabricante:", i["laboratorio"])
                print("Es de Marca:", i["marcaOGenerico"])
            """
            print("--- Consulta 2 ---")
            x = "INSPRA"
            principio = db.axuliarObtenerPrincipioActivoUsandoNombreProducto(x)
            print(principio)
            proveedores = db.obtenerProveedoresParaMedicamento(principio)
            for proveedor in proveedores:
                print(proveedor)
            
            print("--- Consulta 4 ---")
            resultados = db.auxiliarObtenerTop5MedicamentosMasUsadosPorDepartamento()
            # Ahora puedes trabajar con los resultados
            print("---TOP 5---")
            for resultado in resultados:
                medicamento = resultado["medicamento"]
                departamento = resultado["departamento"]
                cantidad_solicitudes = resultado["cantidad_solicitudes"]

                nombre_medicamento = medicamento["Nombre_del_producto_farmacéutico"]
                nombre_departamento = departamento["Nombre"]

                print(f"Medicamento: {nombre_medicamento}, Departamento: {nombre_departamento}, Solicitudes: {cantidad_solicitudes}")

                principio_activo = medicamento["Principio_activo_o_asociacion_de_principios_activos"]

                detalles_medicamentos = db.obtenerDetalleTop5MedicamentosMasUsadosPorDepartamento(principio_activo)

                print("---Detalles---")
                for detalle in detalles_medicamentos:
                    print(f"Fabricante: {detalle['Fabricante']}")
                    print(f"Precio con IVA: {detalle['PrecioConIVA']}")
                    print(f"Precio Máximo: {detalle['precioMaximo']}")
            
            print("--- Consulta 8 ---")
            resultados = db.top10PrincipiosActivosProducidosPorMasFabricantes()
            print("---TOP 10---")
            for resultado in resultados:
                principioActivo, numFabricantes = resultado
                print(f"Principio Activo: {principioActivo}, Número de Fabricantes: {numFabricantes}")

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
    elif choice == "Consultas":
        # Si el usuario elige "Consultas," mostrar ComboBox y cuadro de texto
        st.subheader("Consultas")
        consulta_elegida = st.selectbox("Selecciona una consulta", ["Consulta 1", "Consulta 2", "Consulta 3", "Consulta 4", "Consulta 5", "Consulta 6", "Consulta 7", "Consulta 8", "Consulta 9"])

        #//////////////////////////////////////////////////////////////////// C O N S U L T A S //////////////////////////////////////////
    
    
    
    #///////////////////////////////////Consulta 1////////////////////////////////////////////////////////////////////////////////////////
              
        # Realizar acciones basadas en la consulta seleccionada
        if consulta_elegida:
                if consulta_elegida == "Consulta 1":
                    st.subheader("Consulta 1 - Reporte de medicamentos que potencialmente podría adquirir la CCSS")
                        # Agregar una entrada de texto 
                    categoria = st.text_input("Ingresa la categoria del medicamento:")   
                    codigo = db.axuliar_BuscarCategoria(categoria)
                    principioActivo = db.axuliar_BuscarMedicamentoUsandoCodigo(codigo)
                    detalleMedicamento = db.reporteMedicamentosPotencialmenteAdquiridos(principioActivo)
                        
                    if detalleMedicamento:
                        st.text("Medicamentos potencialmente adquiridos por la caja:")
                        for i in detalleMedicamento:
                            for i in detalleMedicamento:
                                st.write("Nombre Medicamento:", i["nombre"])
                                st.write("Principio Activo:", i["principio"])
                                st.write("Fabricante:", i["laboratorio"])
                                st.write("Es de Marca:", i["marcaOGenerico"])
                    else:
                        st.text("No se encontraron medicamentos potencialmente adquiridos por la caja.")

    #///////////////////////////////////Consulta 2////////////////////////////////////////////////////////////////////////////////////////
    
                elif consulta_elegida == "Consulta 2":
                    st.subheader("Consulta 2 - Posibles proveedores de medicamentos")
                        # Agregar una entrada de 
                    nombre_medicamento = st.text_input("Ingresa el nombre del medicamento:")
                    
                    #if nombre_medicamento:
                    # Llamar a la función para buscar buscar lo solicitado
                    # proveedores_encontrados = buscar_proveedor(nombre_medicamento)
                    
                   # if proveedores_encontrados:
                   #     st.text("Proveedores encontrados:")
                   #     for proveedor in proveedores_encontrados:
                   #         st.text(proveedor)
                   #     else:
                   #      st.text("No se encontraron proveedores para el medicamento ingresado.")
 
     #///////////////////////////////////Consulta 3////////////////////////////////////////////////////////////////////////////////////////
              
                elif consulta_elegida == "Consulta 3":
                    st.subheader("Consulta 3 - Medicamentos Bioequivalentes")
                        # Agregar una entrada de texto 
                    principio_activo = st.text_input("Ingresa el principio activo:")
                    
                    #if principio_activo:
                    # Llamar a la función para buscar buscar lo solicitado
                    # medicamentos_encontrados = buscar_medicamentos_por_principio_activo(principio_activo)
                    
                    #if medicamentos_encontrados:
                    #    st.text("Medicamentos bioequivalentes encontrados:")
                    #    for medicamento in medicamentos_encontrados:
                    #        st.text(medicamento)
                    #    else:
                    #     st.text("No se encontraron medicamentos para el principio activo ingresado.")
        #///////////////////////////////////Consulta 4////////////////////////////////////////////////////////////////////////////////////////
                
                elif consulta_elegida == "Consulta 4":
                    st.subheader("Consulta 4 - Top 5 de medicamentos o suministros solicitados por cada departamento del hospital")
                        # Agregar una entrada de texto 
                    departamento = st.text_input("Ingresa el departamento:")
                    
                    #if departamento:
                    # Llamar a la función para buscar buscar lo solicitado
                    # Top5_medicamentos = buscar_Top5_medicamentos_por_departamento(departamento)
                    
                    #if Top5_medicamentos:
                    #    st.text("Top 5 de los Medicamentos solicitados por la caja:")
                    #    for medicamento in Top5_medicamentos:
                    #        st.text(medicamento)
                    #    else:
                    #     st.text("No se encontraron medicamentos.")

        #///////////////////////////////////Consulta 5////////////////////////////////////////////////////////////////////////////////////////
                elif consulta_elegida == "Consulta 5":
                    st.subheader("Consulta 5 -  Fabricantes y ofertantes que trabajan con el producto, así como la presentación de los productos ofrecidos para ese principio activo y las categorías a las que pertenece según el catálogo de la CCSS")
                        # Agregar una entrada de texto 
                    principio_activo_consulta5 = st.text_input("Ingresa el principio activo:")
                    
                    #if principio_activo_consulta5:
                    # Llamar a la función para buscar lo solicitado
                    # Ofertantes_y_fabricantes = buscar_fabricantes_ofertantes(principio_activo_consulta5)
                    
                    #if Ofertantes_y_fabricantes:
                    #    st.text("Fabricantes y ofertantes encontrados:")
                    #    for ofertante_fabricante in Ofertantes_y_fabricantes:
                    #        st.text(ofertante_fabricante)
                    #    else:
                    #     st.text("No se encontro información.")

        #///////////////////////////////////Consulta 6////////////////////////////////////////////////////////////////////////////////////////
              
                elif consulta_elegida == "Consulta 6":
                    st.subheader("Consulta 6 - Top 10 de principios activos que han sido suspendidos para uso comercial")
                   #LLAMAR A LA FUNCION Top10_principiosActivos
                   # st.text(Top10_principiosActivos)   

         #///////////////////////////////////Consulta 7////////////////////////////////////////////////////////////////////////////////////////
              
                elif consulta_elegida == "Consulta 7":
                    st.subheader("Consulta 7 - Lista de los medicamentos para tratamientos de larga duración que se encuentren disponibles en la CCSS y los posibles reemplazos para él")
                   #LLAMAR A LA FUNCION tratamientos_larga_duracion
                   # st.text(tratamientos_larga_duracion)

        #///////////////////////////////////Consulta 8////////////////////////////////////////////////////////////////////////////////////////
              
                elif consulta_elegida == "Consulta 8":
                    st.subheader("Consulta 8 - Top 10 de principios activos que son producidos por más fabricantes")
                   #LLAMAR A LA FUNCION Top10_principiosActivos_producidos_por_fabricantes                   
                    #st.text(Top10_principiosActivos_producidos_por_fabricantes)   

        #///////////////////////////////////Consulta 9////////////////////////////////////////////////////////////////////////////////////////
               
                elif consulta_elegida == "Consulta 9":
                    st.subheader("Consulta 9 -  Productos de un fabricante que actualmente no están en la CCSS.")
                        # Agregar una entrada de texto 
                    fabricante = st.text_input("Ingresa el nombre del fabricante:")
                    
                    #if fabricante:
                    # Llamar a la función para buscar lo solicitado
                    # productos_no_enCCSS = buscar_proctos_NO_enCCSS_por_fabriacante(fabricante)
                    
                    #if productos_no_enCCSS:
                    #    st.text("Productos encontrados:")
                    #    for productos in productos_no_enCCSS:
                    #        st.text(productos)
                    #    else:
                    #     st.text("No se encontraron productos.")
                    
main()  # Llamar a la función main() para iniciar la aplicación