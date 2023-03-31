import pandas as pd

df = pd.read_csv(filepath_or_buffer="C://mydataset//tips.csv")
json = df.to_json(path_or_buf="C://mydataset//df.json")
# print(json)