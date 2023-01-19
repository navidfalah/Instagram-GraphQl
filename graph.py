
from .defines import makeApiCall

def getAccount(params, username):
    endpointParams = dict()
    endpointParams['fields'] = 'business_discovery.username(' + username + '){name,username,followers_count,follows_count,media_count,profile_picture_url,biography, ig_id, id, website}'
    endpointParams['access_token'] = params['access_token']
    url = params['endpoint_base'] + params['instagram_account_id']
    return makeApiCall(url, endpointParams, params['debug'])

def getMedia(params, username):
    endpointParams = dict()
    endpointParams['fields'] = 'business_discovery.username(' + username + '){media{caption, comments_count, like_count, media_url,permalink,media_product_type, media_type, timestamp, id}}'
    endpointParams['access_token'] = params['access_token']
    url = params['endpoint_base'] + params['instagram_account_id']
    return makeApiCall(url, endpointParams, params['debug'])

