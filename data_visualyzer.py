import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import process_data
import load_data
from io import BytesIO

def visualyze_total_amount_by_cat(df):
    # Crear el gráfico de pastel
    plt.figure(figsize=(8, 8))  # Establecer el tamaño del gráfico

    # Generar gráfico de pastel
    plt.pie(df, labels=df.index, autopct='%1.1f%%', startangle=90)

    # Añadir título al gráfico
    plt.title('Gastos Anuales por Categoría de Producto')

    # Asegurarse de que el gráfico sea un círculo
    plt.axis('equal')  

    # Guardar el gráfico en un objeto BytesIO
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    return img

def visualyze_total_amount_by_month(df):
    df["Year-Month"] = df["Year-Month"].astype(str)
    plt.figure(figsize=(10,6))
    
    plt.plot(df["Year-Month"], df["Total Amount"], marker='o', linestyle='-', color='b')
    plt.title('Subidas y Bajadas de Total Amount por Mes')
    plt.xlabel('Fecha (Mes)')
    plt.ylabel('Total Amount')

    # Rotar las etiquetas del eje X para mayor legibilidad
    plt.xticks(df["Year-Month"], rotation=45)

    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return img

def percent_amount_by_month(df):
    # Crear el gráfico de barras
    plt.figure(figsize=(12, 6))  # Establecer el tamaño del gráfico
    bars = plt.bar(df["Month"].astype(str), df["Porcentaje"], color='skyblue')

    # Añadir título y etiquetas de los ejes
    plt.title('Categoría de Producto con Mayor Porcentaje de Ventas por Mes')
    plt.xlabel('Mes')
    plt.ylabel('Porcentaje de Ventas')

    # Mostrar las etiquetas de categoría y porcentaje sobre las barras
    for index, bar in enumerate(bars):
        yval = bar.get_height()
        category = df["Product Category"].iloc[index]
        plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{category}\n{yval:.2f}%", 
                ha='center', va='bottom', fontsize=10)

    # Rotar las etiquetas del eje X para mejor legibilidad
    plt.xticks(rotation=45)

    # Ajustar el gráfico para que no se corten las etiquetas
    plt.tight_layout()

    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return img
    

