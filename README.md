# Based-on-face-Python-and-OpenCV-are-used-to-realize-face-unlocking
Based on face++, Python and OpenCV are used to realize face unlocking
## 注：部分内容来自CSDN Python雁横
# 简介
使用python+opencv+face++来实现人脸验证及人脸解锁。代码量同样不多，你可以将这些代码运用在其它一些智能领域，如智能家居，进门的时候判断你是谁，也可以加入机器学习判断来的人是客人还是熟人。在讲之前我们会先适当的拓扑一下关于人脸识别的知识点。OK废话少说下面直接开始开始
## 解锁原理
Face++实现人脸匹配的原理。现在你打开了摄像头，然后恰好你按下了抓取。抓取之后，你的脸部图片会上传到远程服务器，然后服务端会提取你的面部情况生成一个唯一的指纹（标识码），这个指纹在Face++里面叫做face_token这个我们后面会继续讲到，这个指纹就代表你目前的身份。
## face++介绍
Face++是新一代云端视觉服务平台，提供一整套世界领先的人脸检测，人脸识别，面部分析的视觉技术服务。Face++旨在提供简单易用，功能强大，平台通用的视觉服务，让广大的Web及移动开发者可以轻松使用最前沿的计算机视觉技术，从而搭建个性化的视觉应用。 Face++同时提供云端REST API以及本地API（涵盖Android, iOS, Linux, Windows, Mac OS），并且提供定制化及企业级视觉服务。通过Face++，您可以轻松搭建您自己的云端身份认证，用户兴趣挖掘，移动体感交互，社交娱乐分享等多类型应用。
