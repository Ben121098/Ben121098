import pandas as pd
import numpy as np
import pdb

file_name = "Auswertung"
df = pd.read_excel(r"{}.xlsx".format(file_name),sheet_name="Tabelle1")
df_mittel = df[df["w [%]"].isna()==False]
df_mittel = df_mittel.copy()
df_columns = list(df_mittel.columns)
for invalid_column_name in ["Nr"]:
    df_columns.remove(invalid_column_name)

df_mittel = df_mittel[df_columns]
    
for i in df_mittel.index:
    for column_name in df_mittel.columns[2:]:
        sample_values = [df[column_name].iloc[ind] for ind in range(i,i+3)]
        breakpoint()
        if not any(np.isnan(k) for k in sample_values):
            df_mittel[column_name].iloc[i] = sum(sample_values)/3
    

# print(df_mittel)

df_mittel.to_excel("{}_python.xlsx".format(file_name))