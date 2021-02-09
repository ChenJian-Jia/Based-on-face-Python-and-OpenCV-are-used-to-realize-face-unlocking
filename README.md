# Based-on-face-Python-and-OpenCV-are-used-to-realize-face-unlocking
Based on face++, Python and OpenCV are used to realize face unlocking
## 注：部分内容来自CSDN Python雁横
# 简介
使用python+opencv+face++来实现人脸验证及人脸解锁。代码量同样不多，你可以将这些代码运用在其它一些智能领域，如智能家居，进门的时候判断你是谁，也可以加入机器学习判断来的人是客人还是熟人。在讲之前我们会先适当的拓扑一下关于人脸识别的知识点。OK废话少说下面直接开始开始
## 解锁原理
Face++实现人脸匹配的原理。现在你打开了摄像头，然后恰好你按下了抓取。抓取之后，你的脸部图片会上传到远程服务器，然后服务端会提取你的面部情况生成一个唯一的指纹（标识码），这个指纹在Face++里面叫做face_token这个我们后面会继续讲到，这个指纹就代表你目前的身份。
上传完经过服务端分析收录之后，服务端会通过json发送给你一个数据包，这个数据包里面有你面部全部特征。
当你拿到服务端返回过来的json之后，将face_token提取出来（这很重要，face_token相当于一把钥匙）然后你把拿到的face_token放到python的if里面去判断如果face_token相符就验证成功，如果不相符那么解锁失败。
## face++介绍
Face++是新一代云端视觉服务平台，提供一整套世界领先的人脸检测，人脸识别，面部分析的视觉技术服务。Face++旨在提供简单易用，功能强大，平台通用的视觉服务，让广大的Web及移动开发者可以轻松使用最前沿的计算机视觉技术，从而搭建个性化的视觉应用。 Face++同时提供云端REST API以及本地API（涵盖Android, iOS, Linux, Windows, Mac OS），并且提供定制化及企业级视觉服务。通过Face++，您可以轻松搭建您自己的云端身份认证，用户兴趣挖掘，移动体感交互，社交娱乐分享等多类型应用。
## 环境
操作系统：windows10
Python版本：3.7
Opencv版本：4.4
Face++接口
## 实现方案
1.上传面孔（这个上篇文章我们已经实现摄像头抓取，这篇文章我们不做啰嗦，直接用一张面部图片代替）上传后json会返回面部指纹（face_token）
2.创建人脸集合，并将步骤1返回的face_token加入到集合中去
3.通过python的if判断是否收录当前面孔
## 代码部分
1.获取面孔face_token
```
import cv2
import requests
import json
url='https://api-cn.faceplusplus.com/facepp/v3/detect'
files={'image_file':open('4.jpg','rb')}
payload={
    'api_key':'2ejaeNuWzlBdpSALJTbWNGsTHDjJel9M',
    'api_secret':'E2Vt9E6zz39UNpdm4ngF86Ff1_YX8JV9',
    'return_landmark':0,
    'return_attributes':'gender,age,glass'}

r=requests.post(url,files=files,data=payload)
data=json.loads(r.text)
print(r.text)
print('============')
print(data)

width=data['faces'][0]['face_rectangle']['width']
top=data['faces'][0]['face_rectangle']['top']
height=data['faces'][0]['face_rectangle']['height']
left=data['faces'][0]['face_rectangle']['left']

img=cv2.imread("4.jpg")
vis=img.copy()
cv2.rectangle(vis,(left,top),(left+width,top+height),(0,256,0),2)
cv2.imshow("Image",vis)

```


