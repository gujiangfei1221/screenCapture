# screenCapture
## 介绍
- 这个工具是一个自动抓图截屏工具，使用场景为：编写操作手册或者制作文档时，只需要打开工具，然后执行一遍操作，工具会自动进行截图并保存，后续只需要根据截图播放就可以回放你的操作，方便编写文档


## 使用
- screencapture.py使用了pyhook库对鼠标和键盘事件进行监听，使用了pil库进行截图
- histsimilar.py使用了pil库进行图片相似度的分析
- dist文件夹是已经打包好的exe文件，先运行screencapture.exe，后运行histsimilar.exe

## todo
- 制作一个GUI界面
- 解决退出程序时候的报错
- 把图片转化成pdf

# 更新日志
- V1.1 新增image2pdf.py，实现图片打包pdf的功能；将dist的exe更新成最新

## 感谢
图片相似度的代码参考自：http://www.webtag123.com/python/44300.html

