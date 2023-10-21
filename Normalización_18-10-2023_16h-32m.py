import csv  # Importa la biblioteca csv para trabajar con archivos CSV
import re  # Importa la biblioteca re para trabajar con expresiones regulares

def limpiarNombre(input_file):
    # Crea una lista para almacenar las filas limpias
    filas_limpias = []

    # Abre el archivo de entrada en modo lectura ('r') y crea un lector CSV
    with open(input_file, 'r', newline='', encoding='utf-8') as csv_in:
        reader = csv.reader(csv_in)

        # Recorre cada fila en el archivo CSV
        for row in reader:
            if row:
                # Busca la primera ocurrencia de un dígito en el primer elemento de la fila
                match = re.search(r'\d', row[0])

                if match:
                    numero_index = match.start()  # Obtiene el índice del primer dígito encontrado
                    row[0] = row[0][:numero_index]  # Elimina todo después del primer dígito
                filas_limpias.append(row)  # Agrega la fila modificada a la lista filas_limpias

    # Abre el archivo original en modo escritura ('w') para sobrescribirlo
    with open(input_file, 'w', newline='', encoding='utf-8') as csv_out:
        writer = csv.writer(csv_out)  # Crea un escritor CSV

        # Escribe las filas limpias en el archivo original
        writer.writerows(filas_limpias)

# Uso de la función
archivo_entrada = "C:\\Users\\Luis Antonio Jimenez\\OneDrive - Estudiantes ITCR\\TEC\\ATI\\Semestre 6\\Bases de Datos Avanzadas\\Proyecto Programado 2\\datos\\limpios\\Limpio1.1_Nombre_de_productos_genéricos_y_Farmaceutica.csv"

# Llama a la función limpiarNombre con el archivo de entrada especificado
limpiarNombre(archivo_entrada)
