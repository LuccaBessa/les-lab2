import csv
import os

headers = [
    'nameWithOwner',
    'folderName',
    'url',
    'createdAt',
    'stargazerCount',
    'releases',
    'LOC',
    'CBO',
    'DIT',
    'LCOM',
]


def generateCSV(json, filename):
    print("Generating " + filename + " CSV...")
    with open(filename + '.csv', 'x') as f:
        writer = csv.writer(f)

        writer.writerow(headers)

        for repo in json:
            writer.writerow([
                repo['nameWithOwner'],
                repo['name'],
                repo['url'],
                repo['createdAt'],
                repo['stargazerCount'],
                repo['releases'],
                None,
                None,
                None,
                None,
            ])
