import pandas as pd

xlsx = pd.read_excel("~/Desktop/petplate_food_data.xlsx")
xlsx.to_csv("~/Desktop/petplate_food_data.csv")