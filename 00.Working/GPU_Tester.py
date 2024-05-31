import torch

# GPU 사용 가능 -> True, GPU 사용 불가 -> False
print(torch.zeros(1).cuda())