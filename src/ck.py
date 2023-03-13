import pandas as pd
import os

csv_path = 'repos.csv'
repos_df = pd.read_csv(csv_path)

if not all(col in repos_df.columns for col in ['CBO', 'DIT', 'LCOM']):
    for index, row in repos_df.iterrows():
        if pd.isnull(row['CBO']) or pd.isnull(row['DIT']) or pd.isnull(row['LCOM']):
            print(f"Processing {row['name']}...")

            os.system(f"git clone {row['url']}")
            repo_path = row['name']

            os.system(f"sudo java -jar ./jar/ck.jar {repo_path} true 0 false ck_output")

            ck_csv_path = os.path.join('ck_output', 'ck.csv')
            ck_df = pd.read_csv(ck_csv_path)

            cbo_mean = ck_df['CBO'].mean()
            dit_mean = ck_df['DIT'].mean()
            lcom_mean = ck_df['LCOM'].mean()

            repos_df.loc[index, 'CBO'] = cbo_mean
            repos_df.loc[index, 'DIT'] = dit_mean
            repos_df.loc[index, 'LCOM'] = lcom_mean
            repos_df.to_csv(csv_path, index=False)

            os.system(f"rm -rf {repo_path}")
            os.system(f"rm -rf ck_output")

else:
    print("Required columns already exist in the CSV file.")