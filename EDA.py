from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
folder = Path(r"C:\Users\Cyber_AI\.cache\kagglehub\datasets\nathanlauga\nba-games\versions\10")

print(list(folder.glob("*.csv")))  # Check the CSV filenames in the folder
data = pd.read_csv(folder / "games.csv")
print(data.shape)
display(data.head())