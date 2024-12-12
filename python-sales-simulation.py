import random
import pandas as pd
from datetime import datetime, timedelta

# Generamos un conjunto de datos simulado (100,000 registros)
def generar_datos_ventas(num_ventas):
    categorias = ['Electronics', 'Clothing', 'Food', 'Toys', 'Books']
    datos = []
    fecha_inicial = datetime(2020, 1, 1)
    
    for i in range(num_ventas):
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
    datos_ventas = generar_datos_ventas(num_ventas)  # Generamos las ventas
    df = pd.DataFrame(datos_ventas, columns=['ID', 'Categoria', 'Monto', 'Fecha'])
    
    # Convertir la columna Fecha a formato de fecha de Pandas
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    
    return df

# Análisis de los datos a gran escala
def analisis_de_ventas(df):
    # Total de ventas por categoría
    total_por_categoria = df.groupby('Categoria')['Monto'].sum()
    print("Total de ventas por categoría (las 5 primeras):\n", total_por_categoria.head())
    
    # Promedio de ventas por día
    ventas_diarias = df.groupby(df['Fecha'].dt.date)['Monto'].sum()
    promedio_diario = ventas_diarias.mean()
    print("\nPromedio de ventas por día:", round(promedio_diario, 2))

    # Total de ventas en todo el periodo
    total_ventas = df['Monto'].sum()
    print("\nTotal de ventas en el periodo:", round(total_ventas, 2))

    # Mostrar estadísticas adicionales como la desviación estándar de las ventas
    print("\nDesviación estándar de las ventas:", round(df['Monto'].std(), 2))

    # Mostrar las primeras filas de los datos procesados
    print("\nPrimeras filas de los datos procesados:")
    print(df.head())

# Función principal
def main():
    num_ventas = 100000  # 100,000 registros de ventas
    print(f"Generando y procesando {num_ventas} registros de ventas...")

    # Procesamos los datos
    df = procesar_datos_ventas(num_ventas)
    
    # Realizamos el análisis
    analisis_de_ventas(df)

if __name__ == "__main__":
    main()
