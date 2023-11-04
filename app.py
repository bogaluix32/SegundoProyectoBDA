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
            """
            print("--- Consulta 3 ---")
            p = "CLARITROMICINA"
            medicamentos = db.buscar_medicamentos_por_principio_activo(p)

            # Imprime los medicamentos encontrados
            for medicamento in medicamentos:
                print(medicamento)
            """
            # Ejemplo de uso Consulta 5
            """
            print("--- Consulta 5 ---")
            x = "ACICLOVIR"
            resultados = db.consultar_info_principio_activo(x)

            # Imprime los resultados
            for resultado in resultados:
                print("Laboratorio:", resultado["Laboratorio"])
                print("Presentación:", resultado["Presentación"])
                print("Categorías:", resultado["Categorias"])
            """    
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
            """
            print("--- Consulta 2 ---")
            x = "INSPRA"
            principio = db.axuliarObtenerPrincipioActivoUsandoNombreProducto(x)
            print(principio)
            proveedores = db.obtenerProveedoresParaMedicamento(principio)
            for proveedor in proveedores:
                print(proveedor)
            """
            """
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
            """
            """
            print("--- Consulta 8 ---")
            resultados = db.top10PrincipiosActivosProducidosPorMasFabricantes()
            print("---TOP 10---")
            for resultado in resultados:
                principioActivo, numFabricantes = resultado
                print(f"Principio Activo: {principioActivo}, Número de Fabricantes: {numFabricantes}")
            """

        else:
            st.warning("Por favor, suba los archivos CSV primero.")  # Mensaje de advertencia si no se cargaron archivos
    elif st.button("Limpiar Base de Datos"):
        db.clean_database()
        st.success("Base de datos limpiada con éxito.")

# Función principal de la aplicación
def main():
    # Configurar el título de la página
    st.title("Proyecto 2 Bases de datos Avanzadas")
    
    # Crear el menú principal con dos opciones: "Subir Datos" y "Consultas"
    menu = ["Subir Datos", "Consultas", "CRUD Medicamento", "CRUD Laboratorio", "CRUD Fabricante", "CRUD Principio Activo", "CRUD Departamento", "CRUD Categoria Medicamento"]
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

                    principio = db.axuliarObtenerPrincipioActivoUsandoNombreProducto(nombre_medicamento)
                    proveedores = db.obtenerProveedoresParaMedicamento(principio) 
                    if proveedores:
                        st.text("Proveedores:")
                        for proveedor in proveedores:
                            st.write(proveedor)
                    else:
                        st.text("No se encontraron resultados.")
     #///////////////////////////////////Consulta 3////////////////////////////////////////////////////////////////////////////////////////
              
                elif consulta_elegida == "Consulta 3":
                    st.subheader("Consulta 3 - Medicamentos Bioequivalentes")
                        # Agregar una entrada de texto 
                    principio_activo = st.text_input("Ingresa el principio activo para buscar el medicamento:")

                    medicamentos = db.buscar_medicamentos_por_principio_activo(principio_activo)
                    if medicamentos:
                        st.text("Lista de medicamentos bioequivalentes")
                        for medicamento in medicamentos:
                            st.write(medicamento)
                    else:
                        st.text("No se encontraron resultados.")
                    
        #///////////////////////////////////Consulta 4////////////////////////////////////////////////////////////////////////////////////////
                
                elif consulta_elegida == "Consulta 4":
                    st.subheader("Consulta 4 - Top 5 de medicamentos o suministros solicitados por cada departamento del hospital")
                    resultados = db.auxiliarObtenerTop5MedicamentosMasUsadosPorDepartamento()
                    if resultados:
                        st.text("TOP 5:")
                        for resultado in resultados:
                            medicamento = resultado["medicamento"]
                            departamento = resultado["departamento"]
                            cantidad_solicitudes = resultado["cantidad_solicitudes"]
                            nombre_medicamento = medicamento["Nombre_del_producto_farmacéutico"]
                            nombre_departamento = departamento["Nombre"]

                            st.write(f"Medicamento: {nombre_medicamento}, Departamento: {nombre_departamento}, Solicitudes: {cantidad_solicitudes}")
                            
                            principio_activo = medicamento["Principio_activo_o_asociacion_de_principios_activos"]

                            detalles_medicamentos = db.obtenerDetalleTop5MedicamentosMasUsadosPorDepartamento(principio_activo)

                            if detalles_medicamentos:
                                st.text(f"Detalles para el medicamento: {nombre_medicamento}")
                                for detalle in detalles_medicamentos:
                                    st.write(f"Fabricante: {detalle['Fabricante']}")
                                    st.write(f"Precio con IVA: {detalle['PrecioConIVA']}")
                                    st.write(f"Precio Máximo: {detalle['precioMaximo']}")
                            else:
                                st.text(f"No se encontraron detalles para el medicamento {nombre_medicamento}")
                    else:
                        st.text("No se encontraron resultados.")
                    

        #///////////////////////////////////Consulta 5////////////////////////////////////////////////////////////////////////////////////////
                elif consulta_elegida == "Consulta 5":
                    st.subheader("Consulta 5 -  Fabricantes y ofertantes que trabajan con el producto, así como la presentación de los productos ofrecidos para ese principio activo y las categorías a las que pertenece según el catálogo de la CCSS")
                        # Agregar una entrada de texto 
                    pricipioActivo = st.text_input("Ingresa el principio activo:")

                    resultados = db.consultar_info_principio_activo(pricipioActivo)
                    
                    if resultados:
                        for resultado in resultados:
                            st.text("Laboratorio:", resultado["Laboratorio"])
                            st.text("Presentación:", resultado["Presentación"])
                            st.text("Categorías:", resultado["Categorias"])
                    else:
                        st.text("No se encontraron resultados.")

        #///////////////////////////////////Consulta 6////////////////////////////////////////////////////////////////////////////////////////
              
                elif consulta_elegida == "Consulta 6":
                    st.subheader("Consulta 6 - Top 10 de principios activos que han sido suspendidos para uso comercial")
                   
                    resultados = db.consultaNumeroSeis()

                    if resultados:
                        st.text("Medicamentos Huérfanos:")
                        for resultado in resultados:
                            principio_activo = resultado[0]
                            nombre_medicamento = resultado[1]

                            st.write(f"Principio Activo: {principio_activo}")
                            st.write(f"Medicamento: {nombre_medicamento}")
                    else:
                        st.text("No se encontraron medicamentos huérfanos.")
         #///////////////////////////////////Consulta 7////////////////////////////////////////////////////////////////////////////////////////
              
                elif consulta_elegida == "Consulta 7":
                    st.subheader("Consulta 7 - Lista de los medicamentos para tratamientos de larga duración que se encuentren disponibles en la CCSS y los posibles reemplazos para él")
                    resultados = db.consultaNumeroSiete()

                    if resultados:
                        st.text(
                            "Medicamentos medicamentos para tratamientos de larga duración:")
                        for resultado in resultados:
                            Medicamento = resultado[0]
                            Tipo_de_padecimientos = resultado[1]

                            st.write(f"Principio Activo: {Medicamento}")
                            st.write(f"Medicamento: {Tipo_de_padecimientos}")
                    else:
                        st.text("No se encontraron medicamentos huérfanos.")

        #///////////////////////////////////Consulta 8////////////////////////////////////////////////////////////////////////////////////////
              
                elif consulta_elegida == "Consulta 8":
                    st.subheader("Consulta 8 - Top 10 de principios activos que son producidos por más fabricantes")
                   
                    result = db.top10PrincipiosActivosProducidosPorMasFabricantes()
                    if result:
                        for resultado in result:
                            principioActivo, numFabricantes = resultado
                            st.text(f"Principio Activo: {principioActivo}, Número de Fabricantes: {numFabricantes}")
                    else:
                        st.text("No se encontraron resultados.")


        #///////////////////////////////////Consulta 9////////////////////////////////////////////////////////////////////////////////////////
               
                elif consulta_elegida == "Consulta 9":
                    st.subheader("Consulta 9 -  Productos de un fabricante que actualmente no están en la CCSS.")
                    
                    fabricante = st.text_input(
                    "Ingresa el nombre del Fabricante:")

                    resultados = db.buscar_medicamentos_por_laboratorioConsulta9(fabricante)

                    if resultados:
                        st.text("Medicamentos")
                        for resultado in resultados:
                            st.write(resultado)
                    else:
                        st.text("No se encontraron resultados.")


    elif choice == "CRUD Medicamento":
        st.subheader("Opciones de CRUD Medicamento")
        accion = st.selectbox("Selecciona un opción", ["Insertar Medicamento", "Modificar Medicamento", "Consultar Medicamento", "Eliminar Medicamento"])

        if accion:
                if accion == "Insertar Medicamento":
                    st.subheader("Insertar Medicamento")

                    nombre_producto = st.text_input("Nombre del Producto Farmacéutico: ")
                    presentacion = st.text_input("Presentación: ")
                    nombre_generico = st.text_input("Nombre Genérico: ")
                    precio_maximo = st.text_input("Precio Máximo de Venta: ")
                    codigo_medicamento = st.text_input("Código de Medicamento: ")
                    medicamento_huerfano = st.selectbox("Medicamento Huérfano", ["Sí", "No"])
                    estado = st.selectbox("Estado", ["ALTA", "BAJA"])
                    tipo_farmaco = st.text_input("Tipo de Fármaco: ")
                    nombre_laboratorio = st.text_input("Nombre del Laboratorio Ofertante: ")
                    precio_venta = st.text_input("Precio de Venta con IVA en Euros: ")
                    principio_activo = st.text_input("Principio Activo o Asociación de Principios Activos: ")
                    tratamiento_largo = st.selectbox("Tratamiento de Larga Duración", ["Sí", "No"])
                    precio_unitario = st.text_input("Precio de unitario: ")

                    medicamento_data = {
                        "Nombre_del_producto_farmacéutico": nombre_producto,
                        "Presentacion": presentacion,
                        "Nombre_Generico": nombre_generico,
                        "Precio_maximo_de_venta_transaccion_final_comercial": precio_maximo,
                        "Codigo_de_Medicamento": codigo_medicamento,
                        "Medicamento_huerfano": medicamento_huerfano,
                        "Estado": estado,
                        "Tipo_de_fármaco": tipo_farmaco,
                        "Nombre_del_laboratorio_ofertante": nombre_laboratorio,
                        "Precio_venta_con_IVA_Euros": precio_venta,
                        "Principio_activo_o_asociacion_de_principios_activos": principio_activo,
                        "Tratamiento_de_larga_duracion": tratamiento_largo,
                        "PRECIO_UNITARIO": precio_unitario
                    }

                    if st.button("Crear nodo de medicamento"):
                        result = db.create_medicamento(medicamento_data)  # Asegúrate de que medicamento_data esté definido
                        st.success("Nodo de medicamento creado con éxito. Resultado: " + str(result))

                elif accion == "Modificar Medicamento":
                    st.subheader("Modificar Medicamento")
                    pass

                elif accion == "Consultar Medicamento":
                    st.subheader("Consultar Medicamento")
                    nombre_producto = st.text_input("Nombre del Producto Farmacéutico: ")
                    if st.button("Consultar nodo de medicamento"):
                        medicamento = db.read_medicamento(nombre_producto)  # Asegúrate de que nombre_del_producto_farmacéutico esté definido
                        if medicamento:
                            st.write("Nodo de medicamento leído:", medicamento)
                        else:
                            st.warning("El medicamento no se encontró en la base de datos.")

                elif accion == "Eliminar Medicamento":
                    st.subheader("Eliminar Medicamento")
                    nombre_producto = st.text_input("Nombre del Producto Farmacéutico: ")
                    if st.button("Eliminar nodo de medicamento"):
                        db.delete_medicamento(nombre_producto)  # Asegúrate de que nombre_del_producto_farmacéutico esté definido
                        st.success("Nodo de medicamento eliminado con éxito.")

                else:
                    st.warning("Por favor, seleccione una opción.")
        
    elif choice == "CRUD Laboratorio":
        st.subheader("Opciones de CRUD Laboratorio")
        accion = st.selectbox("Selecciona un opción", ["Insertar Laboratorio", "Modificar Laboratorio", "Consultar Laboratorio", "Eliminar Laboratorio"])

        if accion:
                if accion == "Insertar Laboratorio":
                    st.subheader("Insertar Laboratorio")
                    pass

                elif accion == "Modificar Laboratorio":
                    st.subheader("Modificar Laboratorio")
                    pass

                elif accion == "Consultar Laboratorio":
                    st.subheader("Consultar Laboratorio")
                    pass

                elif accion == "Eliminar Laboratorio":
                    st.subheader("Eliminar Laboratorio")
                    pass

                else:
                    st.warning("Por favor, seleccione una opción.")
    
    elif choice == "CRUD Fabricante":
        st.subheader("Opciones de CRUD Fabricante")
        accion = st.selectbox("Selecciona un opción", ["Insertar Fabricante", "Modificar Fabricante", "Consultar Fabricante", "Eliminar Fabricante"])

        if accion:
                if accion == "Insertar Fabricante":
                    st.subheader("Insertar Fabricante")
                    pass

                elif accion == "Modificar Fabricante":
                    st.subheader("Modificar Fabricante")
                    pass

                elif accion == "Consultar Fabricante":
                    st.subheader("Consultar Fabricante")
                    pass

                elif accion == "Eliminar Fabricante":
                    st.subheader("Eliminar Fabricante")
                    pass

                else:
                    st.warning("Por favor, seleccione una opción.")
    
    elif choice == "CRUD Principio Activo":
        st.subheader("Opciones de CRUD Principio Activo")
        accion = st.selectbox("Selecciona un opción", ["Insertar Principio Activo", "Modificar Principio Activo", "Consultar Principio Activo", "Eliminar Principio Activo"])

        if accion:
                if accion == "Insertar Principio Activo":
                    st.subheader("Insertar Principio Activo")
                    pass

                elif accion == "Modificar Principio Activo":
                    st.subheader("Modificar Principio Activo")
                    pass

                elif accion == "Consultar Principio Activo":
                    st.subheader("Consultar Principio Activo")
                    pass

                elif accion == "Eliminar Principio Activo":
                    st.subheader("Eliminar Principio Activo")
                    pass

                else:
                    st.warning("Por favor, seleccione una opción.")
    
    elif choice == "CRUD Departamento":
        st.subheader("Opciones de CRUD Departamento")
        accion = st.selectbox("Selecciona un opción", ["Insertar Departamento", "Modificar Departamento", "Consultar Departamento", "Eliminar Departamento"])

        if accion:
                if accion == "Insertar Departamento":
                    st.subheader("Insertar Departamento")
                    pass

                elif accion == "Modificar Departamento":
                    st.subheader("Modificar Departamento")
                    pass

                elif accion == "Consultar Departamento":
                    st.subheader("Consultar Departamento")
                    pass

                elif accion == "Eliminar Departamento":
                    st.subheader("Eliminar Departamento")
                    pass

                else:
                    st.warning("Por favor, seleccione una opción.")
    
    elif choice == "CRUD Categoria Medicamento":
        st.subheader("Opciones de CRUD Categoria Medicamento")
        accion = st.selectbox("Selecciona un opción", ["Insertar Categoria Medicamento", "Modificar Categoria Medicamento", "Consultar Categoria Medicamento", "Eliminar Categoria Medicamento"])

        if accion:
                if accion == "Insertar Categoria Medicamento":
                    st.subheader("Insertar Categoria Medicamento")
                    pass

                elif accion == "Modificar Categoria Medicamento":
                    st.subheader("Modificar Categoria Medicamento")
                    pass

                elif accion == "Consultar Categoria Medicamento":
                    st.subheader("Consultar Categoria Medicamento")
                    pass

                elif accion == "Eliminar Categoria Medicamento":
                    st.subheader("Eliminar Categoria Medicamento")
                    pass
        else:
            st.warning("Por favor, seleccione una opción.") 
                    
                    
main()  # Llamar a la función main() para iniciar la aplicación