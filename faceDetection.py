#coding=utf8
import cv2

import requests
import json
flag = 0
while flag==0:
    capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while True:
        ret, frame = capture.read()
        if ret == True:
            cv2.imshow('My Camera', frame)
        key = cv2.waitKey(10)
        if key == 27:
            flag = 1
            break
        if key == ord('x'):

            filename = "face.jpg"
            cv2.imwrite(filename,frame)
            print('正在进行认证')
            break

    del (capture)
    cv2.destroyWindow("camera")
    if flag==0:
         url = 'https://api-cn.faceplusplus.com/facepp/v3/search'
         payload = {'api_key':'yMR53HaKssmgAtv5-1sxD_rv6taJFpUG',
                    'api_secret':'mjI6D-72jCebOq2rs9PPixkMDj-Ia8GW',
                    'faceset_token':'7f0cc482207099671fc446129b8453ce'}
         files = {'image_file':open('face.jpg','rb')}
         r = requests.post(url, files=files, data=payload)
         data = json.loads(r.text)
         print(data)
         print( r.text)
         # print(data["results"][0]["face_token"]=='dc83bd034ef87241e8fcb99bf088ed5f')
         # if data["results"][0]["face_token"] == "ba24b26bc85ce3048a4e0b6ebee4acb2" and data["results"][0]["confidence"]>=data["thresholds"]["1e-5"]:
         if data["results"][0]["face_token"] == "dc83bd034ef87241e8fcb99bf088ed5f" and data["results"][0]["confidence"]>=data["thresholds"]["1e-5"]:
             name = "奥巴马"
             print('认证成功，奥巴马')
         elif data["results"][0]["face_token"] == "b60342dffabe56462936a68fa8839e4d" and data["results"][0]["confidence"]>=data["thresholds"]["1e-5"]:
             name = "特朗普"
             print('认证成功，特朗普')

