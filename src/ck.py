import pandas as pd
import os
import math

csv_path = './src/data/repos.csv'
repos_df = pd.read_csv(csv_path)

for index, row in repos_df.iterrows():
    if pd.isna(row['CBO']) or pd.isna(row['DIT']) or pd.isna(row['LCOM'] or pd.isna['LOC']):
        print(f"Processing {row['folderName']}...")

        os.system(f"git clone {row['url']}")
        repo_path = row['folderName']

        os.system(f"sudo java -jar ./src/jar/ck.jar {repo_path} true 0 false ck_output")

        ck_csv_path = "./ck_outputclass.csv"

        try:
            ck_df = pd.read_csv(ck_csv_path)

            cbo_mean = ck_df['cbo'].median()
            dit_mean = ck_df['dit'].max()
            lcom_mean = ck_df['lcom'].median()
            loc_sum = ck_df['loc'].sum()

            print(f"CBO: {cbo_mean}")

            repos_df.loc[index, 'LOC'] = '-' if math.isnan(loc_sum) else loc_sum
            repos_df.loc[index, 'CBO'] = '-' if math.isnan(cbo_mean) else cbo_mean
            repos_df.loc[index, 'DIT'] = '-' if math.isnan(dit_mean) else dit_mean
            repos_df.loc[index, 'LCOM'] = '-' if math.isnan(lcom_mean) else lcom_mean
            repos_df.to_csv(csv_path, index=False)
        except pd.errors.EmptyDataError:
            print('Error: The file is empty.')

            repos_df.loc[index, 'CBO'] = '-'
            repos_df.loc[index, 'DIT'] = '-'
            repos_df.loc[index, 'LCOM'] = '-'
            repos_df.loc[index, 'LOC'] = '-'
            repos_df.to_csv(csv_path, index=False)
        finally:
            os.system(f"rm -rf {repo_path}")
            os.system(f"rm -f ck_outputclass.csv")
            os.system(f"rm -f ck_outputmethod.csv")
    else:
        print(f"{row['folderName']} already processed")