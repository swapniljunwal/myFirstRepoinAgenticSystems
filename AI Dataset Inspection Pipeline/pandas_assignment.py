import pandas as pd


data = pd.read_csv("AI Dataset Inspection Pipeline\employee.csv")

print(data)

head = data.head(5)
print(head)
tail = data.tail(5)
print(head)

data.info()

des = data.describe()

print(des)

se = data.loc[:,"Name"]

print(se)

new_data = data[["Name","Department","Age"]]

print(new_data)

si = data.iloc[0:6]
print(si)
se = data.loc[data["PerformanceScore"]> 80]
print(se)