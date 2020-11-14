#!/bin/python3
import pandas as pd

df = pd.read_csv("tmp", delimiter="\t")
print("done")
# new_df = df1.join(df2, how="outter", lsuffix="_df1", rsuffix="_df2")
# new_df = pd.concat([df1, df2, df3, df4], axis=1, join='inner')
df.to_csv('output.csv', encoding='utf-8', index=False)
