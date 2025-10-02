import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# loading the CSV
df = pd.read_csv("AI Energy Score Leaderboard Data.csv")

# cleaning the data

# drop rows where model class is missing
df = df.dropna(subset=["Model Class (Only for Text Generation)"])

# ensure GPU Energy column is numeric
df["GPU Energy (Wh) per 1k tasks"] = (
    df["GPU Energy (Wh) per 1k tasks"]
    .astype(str)             # convert to string in case of mixed types
    .str.replace(",", "")    # remove commas if they exist
    .str.strip()             # remove spaces
)

df["GPU Energy (Wh) per 1k tasks"] = pd.to_numeric(
    df["GPU Energy (Wh) per 1k tasks"], errors="coerce"
)



# average GPU energy per model class
class_energy = (
    df.groupby("Model Class (Only for Text Generation)")["GPU Energy (Wh) per 1k tasks"]
    .mean()
    .reset_index()
    .sort_values(by="GPU Energy (Wh) per 1k tasks", ascending=False)
)

# printing results in terminal
print(class_energy)

# barplot of averages
plt.figure(figsize=(12, 6))
sns.barplot(
    data=class_energy,
    x="Model Class (Only for Text Generation)",
    y="GPU Energy (Wh) per 1k tasks",
    palette="viridis"
)
plt.xticks(rotation=45, ha="right")
plt.title("Average GPU Energy per Model Class")
plt.tight_layout()
plt.show()

#boxplot to see distribution instead of just averages
plt.figure(figsize=(12, 6))
sns.boxplot(
    data=df,
    x="Model Class (Only for Text Generation)",
    y="GPU Energy (Wh) per 1k tasks",
    palette="coolwarm"
)
plt.xticks(rotation=45, ha="right")
plt.title("Distribution of GPU Energy by Model Class")
plt.tight_layout()
plt.show()

