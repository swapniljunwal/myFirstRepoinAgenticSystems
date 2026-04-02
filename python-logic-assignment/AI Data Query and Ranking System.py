import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Score": [85, 72, 90, 65, 78],
    "Passed": [True, True, True, False, True],
    "Category": ["A", "B", "A", "C", "B"]
}

df = pd.DataFrame(data)

single_col = df["Name"]
multi_col = df[["Name","Passed"]]

top_3 = df.iloc[0:3]
a_student = df.loc[0:2:2,["Name","Category"]]

highest_s = df[df["Score"] > 85]
highest_SCORE = df[(df["Score"] > 85) & (df["Passed"] == True)]

sort_Score = df.sort_values("Score" , ascending= False)

f_s = df[df["Score"] > 75].sort_values("Score", ascending = True)

print(f_s)

