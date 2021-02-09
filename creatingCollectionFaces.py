#coding=utf8
import requests
url='https://api-cn.faceplusplus.com/facepp/v3/faceset/create'

payload={
    'api_key':'XXX',
    'api_secret':'XXX',
    'display_name':'Dorm_1014',
    'outer_id':'dorm',
    'force_merge':1,
    'face_tokens':'b60342dffabe56462936a68fa8839e4d'
}

r=requests.post(url,data=payload)
print(r.text)