import pandas as pd
import os

csv_path = './data/repos.csv'
repos_df = pd.read_csv(csv_path)


for index, row in repos_df.iterrows():
    if pd.isnull(row['CBO']) or pd.isnull(row['DIT']) or pd.isnull(row['LCOM']):
        print(row)
        print(f"Processing {row['nameWithOwner']}...")

        os.system(f"sudo git clone {row['url']}")
        print(row)
        repo_path = row['folderName']

        os.system(f"sudo java -jar ./jar/ck.jar {repo_path} true 0 false ck_output")

        ck_csv_path = os.path.join('ck_outputclass.csv')
        ck_df = pd.read_csv(ck_csv_path)

        cbo_mean = ck_df['cbo'].mean()
        dit_mean = ck_df['dit'].mean()
        lcom_mean = ck_df['lcom'].mean()

        repos_df.loc[index, 'CBO'] = cbo_mean
        repos_df.loc[index, 'DIT'] = dit_mean
        repos_df.loc[index, 'LCOM'] = lcom_mean
        repos_df.to_csv(csv_path, index=False)

        os.system(f"rm -rf {repo_path}")
        os.system(f"rm -rf ck_output")
    
    break