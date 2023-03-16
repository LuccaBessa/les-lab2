import pandas as pd
import os

csv_path = './src/data/repos.csv'
repos_df = pd.read_csv(csv_path)

for index, row in repos_df.iterrows():
    if pd.isna(row['CBO']) or pd.isna(row['DIT']) or pd.isna(row['LCOM']):
        print(f"Processing {row['folderName']}...")

        os.system(f"git clone {row['url']}")
        repo_path = row['folderName']

        os.system(f"sudo java -jar ./jar/ck.jar {repo_path} true 0 false ck_output")

        ck_csv_path = "./ck_outputclass.csv"
        ck_df = pd.read_csv(ck_csv_path)

        cbo_mean = ck_df['CBO'].median()
        dit_mean = ck_df['DIT'].max()
        lcom_mean = ck_df['LCOM'].median()

        repos_df.loc[index, 'CBO'] = cbo_mean
        repos_df.loc[index, 'DIT'] = dit_mean
        repos_df.loc[index, 'LCOM'] = lcom_mean
        repos_df.to_csv(csv_path, index=False)

        os.system(f"rm -rf {repo_path}")
        os.system(f"rm ck_outputclass.csv")
        os.system(f"rm ck_outputmethod.csv")
    else:
        print(f"{row['folderName']} already processed")
