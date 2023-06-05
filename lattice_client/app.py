import urllib.request

SITE = 'http://rates.lattice.demo/parking'  # URL of the site to check
SITE_R = 'http://rates.lattice.demo/review'

def lambda_handler(event, context):
    print(event)
    if "parking" in event['path']:
        res = urllib.request.urlopen(urllib.request.Request(url=SITE, method='GET'), timeout=10)
    else:
        res = urllib.request.urlopen(urllib.request.Request(url=SITE_R, method='GET'), timeout=10)
        
    body = res.read()
    print(body.decode("utf-8"))
    return {
        'statusCode': 200,
        'body': body.decode("utf-8")
    }
