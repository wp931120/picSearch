# picSearch
seach engine for picture search by picture

### 项目介绍博客地址
https://zhuanlan.zhihu.com/p/591672698

### 项目使用步骤
+ 1.进入milvus 文件夹执行命令

docker-compose up -d 

docker run --name attu -p 8000:3000 -d -e MILVUS_URL={your machine IP} zilliz/attu:latest

+ 2. 访问 localhost:9000 minio 服务，并手动将ILSVRC2012_img_val目录下的图片上传到minio

+ 3.执行tools/MilvusTools.py 的主函数,想milvus服务插入并加载图片向量

+ 4.执行SearchServer.py 启动以图搜图服务
### 项目效果
![image](https://user-images.githubusercontent.com/28627216/207487045-98ec7b9b-a437-44ee-bc9e-915840089e33.png)
