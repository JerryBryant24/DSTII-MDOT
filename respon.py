import argparse
import cv2
import numpy as np
import torch
from lib.models.mamba_fetrack import build_mamba_fetrack
from pytorch_grad_cam import GradCAM, \
                            ScoreCAM, \
                            GradCAMPlusPlus, \
                            AblationCAM, \
                            XGradCAM, \
                            EigenCAM, \
                            EigenGradCAM, \
                            LayerCAM, \
                            FullGrad

from pytorch_grad_cam import GuidedBackpropReLUModel
from pytorch_grad_cam.utils.image import show_cam_on_image, \
preprocess_image
from pytorch_grad_cam.ablation_layer import AblationLayerVit

# 加载预训练的 ViT 模型
model = build_mamba_fetrack(params.cfg, training=False)
model.load_state_dict(torch.load(self.params.checkpoint, map_location='cpu')['net'], strict=True)
model.eval()

# 判断是否使用 GPU 加速
use_cuda = torch.cuda.is_available()
if use_cuda:
    model = model.cuda()
def reshape_transform(tensor, height=14, width=14):
    # 去掉类别标记
    result = tensor[:, 1:, :].reshape(tensor.size(0),
    height, width, tensor.size(2))

    # 将通道维度放到第一个位置
    result = result.transpose(2, 3).transpose(1, 2)
    return result

# 创建 GradCAM 对象
cam = GradCAM(model=model,
target_layer=model.blocks[5],
use_cuda=use_cuda,
reshape_transform=reshape_transform)

# 读取输入图像
image_path = "cat.jpg"
rgb_img = cv2.imread(image_path, 1)[:, :, ::-1]
rgb_img = cv2.resize(rgb_img, (224, 224))

# 预处理图像
input_tensor = preprocess_image(rgb_img,
mean=[0.485, 0.456, 0.406],
std=[0.229, 0.224, 0.225])

# 将图像转换为批量形式
input_tensor = input_tensor.unsqueeze(0)
if use_cuda:
    input_tensor = input_tensor.cuda()
# 计算 grad-cam
target_category = None # 可以指定一个类别，或者使用 None 表示最高概率的类别
grayscale_cam = cam(input_tensor=input_tensor,
target_category=target_category)

# 将 grad-cam 的输出叠加到原始图像上
visualization = show_cam_on_image(rgb_img, grayscale_cam)

# 保存可视化结果
cv2.imwrite('cam.jpg', visualization)