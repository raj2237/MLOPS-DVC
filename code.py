import pandas as pd
import os 

data = {
    'Name':['Alice','Bob','Charlie'],
    'Age': [25,30,25],
    'City': ['New york' ,'Los Angeles', 'Chicago'],
}
df = pd.DataFrame(data)

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)
file_path = os.path.join(data_dir, 'sample_data.csv')
df.to_csv(file_path, index = False)
print(f"CSV file saveed to {file_path}")
