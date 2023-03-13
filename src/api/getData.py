import os
import requests
from os.path import join, dirname
from datetime import datetime


def getData():
    token = os.environ.get('ACCESS_TOKEN')
    after = 'null'
    hasNextPage = True
    data = []
    now = datetime.now()

    while hasNextPage:
        query = """
        {
            search (query: "stars:>100 language:Java", type: REPOSITORY, first: 10, after: %s) {
                pageInfo {
                    startCursor
                    hasNextPage
                    endCursor
                }
                nodes {
                    ... on Repository {
                        nameWithOwner
                        name
                        url
                        createdAt
                        stargazerCount
                    }
                }
            }
        }
        """ % after

        url = 'https://api.github.com/graphql'
        json = {'query': query}
        headers = {'Authorization': 'Bearer %s' % token}

        response = requests.post(url=url, json=json, headers=headers).json()

        hasNextPage = response['data']['search']['pageInfo']['hasNextPage'] if response['data']['search']['pageInfo']['hasNextPage'] else False
        after = '"%s"' % response['data']['search']['pageInfo']['endCursor']

        for repoData in response['data']['search']['nodes']:
            createdAt = datetime.strptime('%s' % repoData['createdAt'], '%Y-%m-%dT%H:%M:%SZ')

            data.append({
                'nameWithOwner': repoData['nameWithOwner'],
                'name': repoData['name'],
                'url': repoData['url'],
                'createdAt': createdAt,
                'stargazerCount': repoData['stargazerCount'],
            })

    return data
