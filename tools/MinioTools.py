import minio


class MinioTools:
    def __init__(self):
        self.client =minio.Minio(endpoint='localhost:9000',
                                 access_key='minioadmin',
                                 secret_key='minioadmin',
                                 secure=False
                                 )

    def lists_bucket(self, bucket):
        print(self.client.list_buckets())
        data = self.client.list_objects(bucket, recursive=True)
        objs = []
        if self.client.bucket_exists(bucket):
            for obj in data:
                objs.append(obj.object_name)
        return objs


if __name__ == '__main__':
    miniotool = MinioTools()
    miniotool.lists_bucket("picture")
