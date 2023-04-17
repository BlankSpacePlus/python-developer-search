import os
import torch

# 是否有可用的gpu
print(torch.cuda.is_available())
# 有几个可用的gpu
print(torch.cuda.device_count())
# 可用gpu编号
print(torch.cuda.current_device())
# 可用gpu内存大小，可用gpu的名字
print(torch.cuda.get_device_capability(device=None), torch.cuda.get_device_name(device=None))
# 声明gpu
os.environ["CUDA_VISIBLE_DEVICES"] = "3"
# 调用哪个gpu
dev = torch.device('cuda:3')
a = torch.rand(100, 100).to(dev)
