import pandas as pd

df = pd.read_csv("Car_sales.csv")

# print(df.info())
# ИНОФРМАЦИЯ
# -------------------
# print(df.describe())
# ДЕТАЛЬНАЯ ИНФОРМАЦИЯ 
# ----------------------
print(df.head(10).T)
# ДЛЯ УДОБНОГО ПРОСМОТРА МЕНЯЕТ СТРОКИ И СТОЛБЦЫ
# ----------------------
# print(df.isnull().sum())
# ТУТ МЫ ВИДИМ ЧТО ЕСТЬ ПРОПУЩЕННЫЕ ДАННЫЕ



