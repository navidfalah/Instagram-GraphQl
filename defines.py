import requests
import json

def getCreds() :
    creds = dict()
    creds['access_token'] = 'EAAbNrriZA4g4BALlOkh6PpMiutkDKsOF1JtzTOButYAbxBMgcqBPd3krDV4kbrNNIuLfarh9oUuZBPhJUI9SEJ3LTwCZC2onX5sPcgkrpkXmZCZBHA2WhzByZBmEsRN7sTsk3n4QJhogUPFeqpkHDYqZAYuZA4NQMPSv4ZC8wdZBI3dJlzhWfk9ieR'
    # 'long lived'
    # 'EAAbNrriZA4g4BAGJBU6Qy0IB8NtyRgsW4MUBWmZABZAeaPmf5G7CdmbYzvh1Rh7s8ogy3ygyCjKqfsKYwO6lBOB9p5ftAZB80BNnHPkBZCCcGIL3tQbFZCZCgZBwNiYSTBuferTG1bS8q5qojqWMwXpvZCzxdvL1luAEEOBAk9ddOhcW5L15cZAOIb'
    # old
    # 'EAAbNrriZA4g4BAC0eOrRHU96q4ZAKgI7QjTHYAzyBeOO8bIZCYgR1OaucMnsBdzpGMAlvjDilNsLblhIecPpzl6CHQYZB66kgyU06vGN2DUj3u5q0oC20OwJNFgFHXxGDmOszZA5QGYJAdYHYaE5mLSuTEfLlH5A9UZAEgveTAPhES1ZAflzZB0y6p4FwXk7cD1YtKFlXu9NZBZCZAjxnINbnrZAIt0XCVhZBvfAZD'
    creds['client_id'] = '1915000165360142'
    creds['client_secret'] = 'd285e2a13c9566ed69f3581fa634f7e1'
    creds['graph_domain'] = 'https://graph.facebook.com/'
    creds['graph_version'] = 'v14.0'
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/'
    creds['debug'] = 'no'
    creds['page_id'] = '101177169410134'
    creds['instagram_account_id'] = '17841455080525749'
    # creds['ig_username'] = 'sarmo_scarf'
    return creds

def makeApiCall(url, endpointParams, debug='no'):
    data = requests.get(url, endpointParams)
    response = dict()
    response['url'] = url
    response['endpoint_params'] = endpointParams
    response['endpoint_params_pretty'] = json.dumps(endpointParams, indent=4)
    response['json_data'] = json.loads(data.content)
    response['json_data_pretty'] = json.dumps(response['json_data'], indent=4)
    return response

