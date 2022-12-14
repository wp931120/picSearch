# picSearch
seach engine for picture search by picture

### 技术选型

图片数据存储工具：minio 一个轻量化的oss的分布式对象存储引擎

图片向量数据存储和检索工具：milvus 向量存储和检索引擎，内置了faiss，HNSW,annoy等多种ann向量检索算法。

图片向量化：resnet 算法进行图片向量抽取

前后端demo工具：gradio一个轻便的机器学习模型的demo部署包

上述工具的使用使得此以图搜图服务非常接近企业级别的可用程度，只需将前后端工具升级替换一下，就可以上线提供服务了。

### 项目介绍博客地址
https://zhuanlan.zhihu.com/p/591672698

### 项目使用步骤
+ 1.进入milvus 文件夹执行命令

docker-compose up -d 

docker run --name attu -p 8000:3000 -d -e MILVUS_URL={your machine IP} zilliz/attu:latest

+ 2.访问 localhost:9000 minio 服务，并手动将ILSVRC2012_img_val目录下的图片上传到minio

+ 3.执行tools/MilvusTools.py 的主函数,想milvus服务插入并加载图片向量

+ 4.执行SearchServer.py 启动以图搜图服务
### 项目效果
![image](https://user-images.githubusercontent.com/28627216/207487045-98ec7b9b-a437-44ee-bc9e-915840089e33.png)
