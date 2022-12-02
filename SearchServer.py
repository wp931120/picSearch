import gradio as gr
from tools.MilvusTools import MilvusTools
from tools.ResNetEmbeding import ResNetEmbeding

milvusTool = MilvusTools()
resnet = ResNetEmbeding("./model/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5")

def seach(path):
    emb = resnet.extract_feature(path.file, distant=False)
    res = milvusTool.search("picture", "pic_vec", [emb])
    return res


if __name__ == '__main__':

    demo = gr.Interface(title="以图搜图",
                        css="",
                        fn=seach,
                        inputs=[gr.outputs.Image(type="file", label="图片")],
                        outputs=[gr.outputs.Image(type="file", label="图片") for _ in range(4)])

    demo.launch(inline=True, height=100)
