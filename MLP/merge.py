import pandas as pd


df1 = pd.read_csv("actual_results_unscaled.csv")
df2 = pd.read_csv("predicted_results_unscaled.csv")


merged_df = pd.concat([df1, df2], axis=1)

merged_df.to_csv('arrays.csv', index=False)
