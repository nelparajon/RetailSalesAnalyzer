import pandas as pd
import numpy as np
import load_data

def process_data(data):
    data = data.dropna()
    data = data.drop_duplicates()
    return data

def data_info(data):
    data = load_data.load_data()
    print(data.info())
    print(data.describe())
    print(data.head())

def data_shape(data):
    data = load_data.load_data()
    print(data.shape)

def data_columns(data):
    data = load_data.load_data()
    print(data.columns)

def data_dtypes(data):
    data = load_data.load_data()
    print(data.dtypes)

def total_amount_by_gender(data):
    #filtramos por mes y genero para saber que meses compran mas mujeres y que mes compran mas hombres en porcentaje
    #primero convertimos el tipo de "Date" a un tipo válido, ya que ahora mismo está en object
    data["Date"] = pd.to_datetime(data["Date"], errors='coerce')
    #creamos una nueva columna que sea año-mes YYYY-MM
    data["Year-Month"] = data["Date"].dt.to_period("M")
    #calculamos el total amount para cada genero por mes
    amount_by_gender_month = data.groupby(["Year-Month", "Gender"])["Total Amount"].sum().reset_index()
    #calculamos el total amount mensual
    total_by_month = data.groupby("Year-Month")["Total Amount"].sum().reset_index()
    total_by_month = total_by_month.rename(columns={"Total Amount": "Total Monthly Amount"})
    #combinamos ambos df
    merge_df = pd.merge(amount_by_gender_month, total_by_month, on="Year-Month")
    #calculamos el porcentaje de comprar al mes por genero y lo mostramos en columna
    merge_df["Porcentaje"] = (merge_df["Total Amount"] / merge_df["Total Monthly Amount"]) * 100
    print(merge_df)
    return merge_df

def total_amount_by_category(data):
    #filtramos el total por category para conocer en que se gasta mas al año
    amount_by_category = data.groupby(["Product Category"])["Total Amount"].sum()
    print(amount_by_category)
    return amount_by_category

def total_amount_by_days(data):
    #filtramos el total por dias
    amount_by_date = data.groupby("Date")["Total Amount"].sum().reset_index()
    print(amount_by_date)
    return amount_by_date

def total_amount_by_month(data):
    # Convertimos el tipo de dato de Date a datetime
    data["Date"] = pd.to_datetime(data["Date"], errors='coerce')
    
    # Creamos una nueva columna que sea año-mes YYYY-MM
    data["Year-Month"] = data["Date"].dt.to_period("M")
    
    # Calculamos y filtramos el total amount por mes
    amount_by_month = data.groupby("Year-Month")["Total Amount"].sum().reset_index()
    
    print(amount_by_month)
    return amount_by_month

def porcentaje_compras_cat_month(data):
    # Asegúrate de que la columna "Date" esté en formato datetime y crear la columna "Month"
    data["Date"] = pd.to_datetime(data["Date"], errors='coerce')
    data["Month"] = data["Date"].dt.to_period("M")

    # Agrupar y calcular el total por cada categoría y el total mensual
    amount_by_cat_month = data.groupby(["Month", "Product Category"])["Total Amount"].sum().reset_index()

    # Calcular el total mensual
    amount_by_month = data.groupby("Month")["Total Amount"].sum().reset_index()

    # Combinar ambos DataFrames
    merge_df = pd.merge(amount_by_cat_month, amount_by_month, on="Month", suffixes=('_Cat', '_Total'))

    # Calcular el porcentaje por categoría y mes
    merge_df["Porcentaje"] = (merge_df["Total Amount_Cat"] / merge_df["Total Amount_Total"]) * 100

    # Filtrar las filas con el porcentaje máximo por cada mes
    max_porcentaje_idx = merge_df.groupby("Month")["Porcentaje"].idxmax()
    categorias_max_vendidas = merge_df.loc[max_porcentaje_idx]

    # Preparar los datos para el gráfico
    resultado = categorias_max_vendidas[["Month", "Product Category", "Porcentaje"]]
    print(resultado)
    return resultado

def get_season(date):
    if pd.isna(date):
        return None
    month = date.month
    day = date.day

    if (month == 3 and day >= 21) or (3 < month < 6) or (month == 6 and day < 21):
        return 'Primavera'
    elif (month == 6 and day >= 21) or (6 < month < 9) or (month == 9 and day < 23):
        return 'Verano'
    elif (month == 9 and day >= 23) or (9 < month < 12) or (month == 12 and day < 21):
        return 'Otoño'
    else:
        return 'Invierno'

def total_amount_by_season(data):
    # Convertimos el tipo de dato de Date a datetime
    data["Date"] = pd.to_datetime(data["Date"], errors='coerce')
    data["Month"] = data["Date"].dt.to_period("M")

    data["Season"] = data["Date"].apply(get_season)

    # Calculamos el total amount por estación
    amount_by_season = data.groupby("Season")["Total Amount"].sum().reset_index()
    amount_by_season["Percentage"] = (amount_by_season["Total Amount"] / amount_by_season["Total Amount"].sum()) * 100

    print(amount_by_season)
    return amount_by_season

def mean_amount_by_month(data):
    #transaction mean by month
    data["Date"] = pd.to_datetime(data["Date"], errors='coerce')
    data["Month"] = data["Date"].dt.to_period("M")
    amount_by_cat_month = data.groupby(["Month"])["Total Amount"].mean().reset_index()
    amount_by_cat_month = amount_by_cat_month.rename(columns={"Total Amount": "Mean Amount"})
    print(amount_by_cat_month)

def transactions_count_by_month(data):
    #transaction count by month
    data["Date"] = pd.to_datetime(data["Date"], errors='coerce')
    data["Month"] = data["Date"].dt.to_period("M")
    count_transactions_by_month = data.groupby("Month")["Total Amount"].count().reset_index()
    count_transactions_by_month = count_transactions_by_month.rename(columns={"Total Amount": "Transaction Count"})
    print(count_transactions_by_month)
    return count_transactions_by_month
