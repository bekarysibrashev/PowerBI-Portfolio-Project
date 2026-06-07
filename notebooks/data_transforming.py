import pandas as pd
import numpy as np
df = pd.read_csv("Car_sales.csv")

# print(df.isna().sum())

#Меняем название на правильное
df = df.rename(columns={"__year_resale_value": "Year_resale_value"})
df = df.rename(columns={"Sales_in_thousands": "Sales"})
df = df.rename(columns={"Price_in_thousands": "Price"})


#Удаляем Пустые даные
df = df.dropna(subset=['Year_resale_value', 'Engine_size', 'Horsepower', 'Wheelbase', 
                     'Width', 'Length', 'Curb_weight', 'Fuel_capacity', 'Fuel_efficiency', 'Power_perf_factor', 'Price'])


#Меняем тип данных
df["Latest_Launch"] = pd.to_datetime(df["Latest_Launch"], format='%m/%d/%Y')
df["Sales"] = df["Sales"] * 1000
df["Price"] = df["Price"] * 1000
df["Year_resale_value"] = df["Year_resale_value"] * 1000
df["Sales"] = df["Sales"].astype(int)
df["Price"] = df["Price"].astype(int)
df["Year_resale_value"] = df["Year_resale_value"].astype(int)

print('\n')
print(df.head(10))

print('\n')
print('\n')
print(df.describe())

print('\n')
print('\n')
print(df.isna().sum().sum() == 0)
print(df.duplicated().sum() == 0)

print('\n')
print('\n')
print(df.dtypes)

# df.to_csv("clean_dataset.csv", index=False)
df.to_excel("data/clean_dataset.xlsx", index=False)