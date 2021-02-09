#coding=utf8
import requests
url='https://api-cn.faceplusplus.com/facepp/v3/faceset/create'

payload={
    'api_key':'yMR53HaKssmgAtv5-1sxD_rv6taJFpUG',
    'api_secret':'mjI6D-72jCebOq2rs9PPixkMDj-Ia8GW',
    'display_name':'Dorm_1014',
    'outer_id':'dorm',
    'force_merge':1,
    'face_tokens':'b60342dffabe56462936a68fa8839e4d'
}

r=requests.post(url,data=payload)
print(r.text)