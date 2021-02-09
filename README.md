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
    'api_key':'XXX',
    'api_secret':'XXXX',
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
### 说明：    
1.api规定是要post提交，所以这里用了request.post()    
2.apikey/apisecret必填 没有的自行申请见说明7   
3.return_attributes选填 里面有返回的数据 有年龄性别等等    
4.return_landmark选填 是否检测返回人脸关键点0为不返回1为检测83个关键点2为检测106个关键点    
5.传输的内容为请求的URL，图片路径（必填！可以是本地绝对路径，也可以是网络图片分别为image_file、image_url）data数据也就是payload里面的参数：  
6.代码中url中所填写的是Face++中检测人脸所要调用的url：https://api-cn.faceplusplus.com/facepp/v3/detect    
![img1](https://github.com/ChenJian-Jia/Based-on-face-Python-and-OpenCV-are-used-to-realize-face-unlocking/blob/main/img/Face%2B%2B%E7%BD%91%E7%AB%99%E6%93%8D%E4%BD%9C1.png)   
![img2](https://github.com/ChenJian-Jia/Based-on-face-Python-and-OpenCV-are-used-to-realize-face-unlocking/blob/main/img/Face%2B%2B%E7%BD%91%E7%AB%99%E6%93%8D%E4%BD%9C3.png)  
7.apikey和apisecret申请   
![img3](https://github.com/ChenJian-Jia/Based-on-face-Python-and-OpenCV-are-used-to-realize-face-unlocking/blob/main/img/Face%2B%2B%E7%BD%91%E7%AB%99%E6%93%8D%E4%BD%9C4.png)   
8.img=cv2.imread("4.jpg")中的“4.jpg”是你想要上传的面孔上传后json会返回面部指纹（face_token）      

### face_token运行结果  
我使用的是本地素材2，运行结果为：    
![img](https://github.com/ChenJian-Jia/Based-on-face-Python-and-OpenCV-are-used-to-realize-face-unlocking/tree/main/img)   
我们可以看到这个返回的json包里有很多的值，我们这里最重要的就是拿到这张脸的face_toen，然后保存起来，收录到服务端的时候需要。    
注：这里可能有些朋友在网上随便找的照片可能报错，这很可能是图片像素的问题，尽量找高清的，运行后，人脸部分会被绿框标识。   
## 创建人脸集合，并加入face_token   
```
#coding=utf8
import requests
url='https://api-cn.faceplusplus.com/facepp/v3/faceset/create'

payload={
    'api_key':'XXX',
    'api_secret':'XXX',
    'display_name':'Dorm_1014',
    'outer_id':'dorm',
    'force_merge':1,
    'face_tokens':'68e7d175387f7c513aae284b75bfd764'
}

r=requests.post(url,data=payload)
print(r.text)

```
### 说明
9.face_tokens里面填的就是刚才使用本地素材2运行face_token代码所生产的face_token  
10.apikey/apisecret必填 没有的自行申请见说明7
11.面部集合的名字也要记住，待会查询的时候也会用到的。将上一部分获取到的face_token加入到一个新建的人脸集合中。下次人脸对比将直接跟服务端收录的做指纹对比。  
12.这里再简单的点一下payload里面的几个参数：  
display_name：人脸集合的名字  
outer_id：FaceSet全局自定义标识  
force_merge：  
0：不将 face_tokens 加入已存在的 FaceSet 中，直接返回 FACESET_EXIST 错误  
1：将 face_tokens 加入已存在的 FaceSet 中  
face_tokens：传入的人脸标识  
13.因为我们要创建集合可以找到Face++里所需调用的url  
![img](https://github.com/ChenJian-Jia/Based-on-face-Python-and-OpenCV-are-used-to-realize-face-unlocking/blob/main/img/Face%2B%2B%E7%BD%91%E7%AB%99%E6%93%8D%E4%BD%9C5.png)  
创建一个人脸的集合 FaceSet，用于存储人脸标识 face_token。一个 FaceSet 能够存储10000个 face_token。试用API Key可以创建1000个FaceSet，正式API Key可以创建10000个FaceSet。  
此代码中的url为：https://api-cn.faceplusplus.com/facepp/v3/faceset/create    
### creatingCollectionFaces运行结果
![img](https://github.com/ChenJian-Jia/Based-on-face-Python-and-OpenCV-are-used-to-realize-face-unlocking/blob/main/img/creatingCollectionFaces%E8%BF%90%E8%A1%8C%E7%BB%93%E6%9E%9C.png)  
运行完毕后，会返回一个faceset_token，这个地方我们要记录下来，因为我们已经把我们的奥巴马的facetoken上传到服务端的我们创建的集合里了，这个faceset token就是我们的面部集合id 或者说是一个相册都可以。  




