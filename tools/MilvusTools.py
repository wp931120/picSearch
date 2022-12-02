from pymilvus import Milvus
from tools.MinioTools import MinioTools
from tools.ResNetEmbeding import ResNetEmbeding
from pymilvus import DataType


class MilvusTools:

    def __init__(self):
       self.client = Milvus("localhost", "19530")

    def create_collection(self, collection_name):
        fields = {"fields": [{"name": "pic_path",
                            "type": DataType.VARCHAR,
                            "is_primary": True,
                            "params": {"max_length": 200}}
                          ,{
                            "name": "pic_vec",
                            "type": DataType.FLOAT_VECTOR,
                            "params": {"dim": 2048}
                            }]}

        if collection_name not in self.client.list_collections():
            self.client.create_collection(collection_name=collection_name, fields=fields)

        else:
            print("已存在")

    def insert_data(self, collection_name, data):
        entities = [
            {"name": "pic_path", "type": DataType.VARCHAR, "values": data[0]},
            {"name": "pic_vec", "type": DataType.FLOAT_VECTOR, "values": data[1]},
        ]
        self.client.insert(collection_name, entities)
        self.client.flush([collection_name])

    def build_index(self, collection_name, field_name):
        index_param = {
            "metric_type": "L2",
            "index_type": "IVF_FLAT",
            "params": {"nlist": 20}
        }
        self.client.create_index(collection_name, field_name, index_param, timeout=10)
        print("Create index: {}".format(index_param))

    def load(self, collection_name):
        self.client.load_collection(collection_name, timeout=10)
        print("load {} success".format(collection_name))

    def search(self, collection_name, vector_field, search_vectors):
        search_params = {"metric_type": "L2", "params": {"nprobe": 20}}
        results = self.client.search(collection_name, search_vectors, vector_field, param=search_params, limit=9)
        print(
            results
        )
        return results[0].ids


if __name__ == '__main__':
    milvusTool = MilvusTools()
    miniotool = MinioTools()
    pics = miniotool.lists_bucket("picture")
    resnet = ResNetEmbeding("../model/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5")
    paths = []
    embs = []
    for i in pics:
        path = "http://localhost:9000/picture/" + i
        emb = resnet.extract_feature(path)
        paths.append(path)
        embs.append(emb)
    data = [paths, embs]
    print(len(data[1]))
    milvusTool.create_collection("picture")
    milvusTool.insert_data("picture", data)
    milvusTool.build_index("picture", "pic_vec")
    milvusTool.load("picture")
   # print(milvusTool.search("picture", "pic_vec", [data[1][0]]))
