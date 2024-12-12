import random
import pandas as pd
from datetime import datetime, timedelta
from time import sleep
from tqdm import tqdm  # Barra de progreso

# Generamos un conjunto de datos simulado (1,000,000 registros)
def generar_datos_ventas(num_ventas):
    categorias = ['Electronics', 'Clothing', 'Food', 'Toys', 'Books', 'Health', 'Home']  # Añadimos 2 productos más
    datos = []
    fecha_inicial = datetime(2020, 1, 1)

    # Usamos tqdm para mostrar una barra de progreso durante la generación de datos
    for i in tqdm(range(num_ventas), desc="Generando datos de ventas", ncols=100, 
                  bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed} < {remaining}, {rate_fmt}]"):
        # Generar datos aleatorios
        id_transaccion = i + 1
        categoria = random.choice(categorias)
        monto_venta = round(random.uniform(5, 1000), 2)
        fecha_venta = fecha_inicial + timedelta(days=random.randint(0, 365))

        # Almacenamos los datos generados
        datos.append([id_transaccion, categoria, monto_venta, fecha_venta])

    return datos

# Convertimos los datos a un DataFrame de Pandas
def procesar_datos_ventas(num_ventas):
    print("\033[1;32mCargando, espere...\033[0m")  # Mensaje con color verde
    sleep(1)  # Pausa para simular tiempo de procesamiento
    
    print("\033[1;33mGenerando los datos de ventas...\033[0m")
    datos_ventas = generar_datos_ventas(num_ventas)  # Generamos las ventas
    
    # Creación del DataFrame
    print("\033[1;36mProcesando los datos en un DataFrame...\033[0m")
    df = pd.DataFrame(datos_ventas, columns=['ID', 'Categoria', 'Monto', 'Fecha'])
    
    # Convertir la columna Fecha a formato de fecha de Pandas
    print("\033[1;34mConvirtiendo las fechas a formato estándar...\033[0m")
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    
    return df

# Análisis de los datos a gran escala
def analisis_de_ventas(df):
    print("\n\033[1;37m---- Análisis de ventas ----\033[0m\n")

    # Total de ventas por categoría
    print("\033[1;34mCalculando el total de ventas por categoría...\033[0m")
    total_por_categoria = df.groupby('Categoria')['Monto'].sum()
    print("\033[1;34mTotal de ventas por categoría (las 5 primeras):\033[0m\n", total_por_categoria.head())
    
    # Promedio de ventas por día
    print("\n\033[1;33mCalculando el promedio de ventas por día...\033[0m")
    ventas_diarias = df.groupby(df['Fecha'].dt.date)['Monto'].sum()
    promedio_diario = ventas_diarias.mean()
    print("\033[1;33mPromedio de ventas por día:\033[0m", round(promedio_diario, 2))

    # Total de ventas en todo el periodo
    print("\n\033[1;35mCalculando el total de ventas en el periodo...\033[0m")
    total_ventas = df['Monto'].sum()
    print("\033[1;35mTotal de ventas en el periodo:\033[0m", round(total_ventas, 2))

    # Mostrar estadísticas adicionales como la desviación estándar de las ventas
    print("\n\033[1;36mCalculando la desviación estándar de las ventas...\033[0m")
    print("\033[1;36mDesviación estándar de las ventas:\033[0m", round(df['Monto'].std(), 2))

    # Resumen rápido de las primeras filas
    print("\n\033[1;32mResumen de los primeros registros procesados:\033[0m")
    print(df.head())

    # Resumen rápido de las estadísticas
    print("\n\033[1;35mEstadísticas rápidas:\033[0m")
    print(df.describe())

# Función principal
def main():
    num_ventas = 1000000  # 1,000,000 registros de ventas
    print(f"\033[1;32mGenerando y procesando {num_ventas} registros de ventas...\033[0m\n")

    # Procesamos los datos
    df = procesar_datos_ventas(num_ventas)
    
    # Realizamos el análisis
    analisis_de_ventas(df)

if __name__ == "__main__":
    main()
