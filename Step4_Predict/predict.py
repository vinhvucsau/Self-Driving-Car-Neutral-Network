import torch
import config
from config import args_setting
from dataset import RoadSequenceDatasetList
from model import generate_model
from torchvision import transforms
from torch.optim import lr_scheduler
from PIL import Image
import numpy as np
import cv2

def output_result(model, test_loader, device):
    model.eval()
    k = 0
    feature_dic=[]
    with torch.no_grad():
        for sample_batched in test_loader:
            k+=1
            #data, target = sample_batched['data'].to(device), sample_batched['label'].type(torch.LongTensor).to(device)
            data = sample_batched['data'].to(device)
            output,feature = model(data) # đối với unet
            #output = model(data) #đối với segnet
            feature_dic.append(feature) # đối với unet
            pred = output.max(1, keepdim=True)[1]
            img = torch.squeeze(pred).cpu().unsqueeze(2).expand(-1,-1,3).numpy()*255
            img = Image.fromarray(img.astype(np.uint8))

            data = torch.squeeze(data).cpu().numpy()
            if args.model == 'SegNet-ConvLSTM' or 'UNet-ConvLSTM':
                data = np.transpose(data[-1], [1, 2, 0]) * 255
            else:
                data = np.transpose(data, [1, 2, 0]) * 255
            data = Image.fromarray(data.astype(np.uint8))
            rows = img.size[0]
            cols = img.size[1]
            for i in range(0, rows):
                for j in range(0, cols):
                    img2 = (img.getpixel((i, j)))
                    if (img2[0] > 200 or img2[1] > 200 or img2[2] > 200):
                        data.putpixel((i, j), (234, 53, 57, 255))
            data = data.convert("RGB")
            data.save(config.save_path + "%s_data.jpg" % k)#red line on the original image
            img.save(config.save_path + "%s_pred.jpg" % k)#prediction result

            return img


def get_parameters(model, layer_name):
    import torch.nn as nn
    modules_skipped = (
        nn.ReLU,
        nn.MaxPool2d,
        nn.Dropout2d,
        nn.UpsamplingBilinear2d
    )
    for name, module in model.named_children():
        if name in layer_name:
            for layer in module.children():
                if isinstance(layer, modules_skipped):
                    continue
                else:
                    for parma in layer.parameters():
                        yield parma


args = args_setting()
torch.manual_seed(args.seed)
use_cuda = args.cuda and torch.cuda.is_available()
#device = torch.device("cuda" if use_cuda else "cpu")
device = torch.device("cuda" if use_cuda else "cpu")
op_tranforms = transforms.Compose([transforms.ToTensor()])  

model = generate_model(args)
class_weight = torch.Tensor(config.class_weight)
criterion = torch.nn.CrossEntropyLoss(weight=class_weight).to(device)

pretrained_dict = torch.load(config.pretrained_path)
model_dict = model.state_dict()
pretrained_dict_1 = {k: v for k, v in pretrained_dict.items() if (k in model_dict)}
model_dict.update(pretrained_dict_1)
model.load_state_dict(model_dict)

def get_output(imgs):



    if args.model == 'SegNet-ConvLSTM' or 'UNet-ConvLSTM':
        test_loader=torch.utils.data.DataLoader(
            RoadSequenceDatasetList(img_list =imgs, transforms=op_tranforms),
            batch_size=args.test_batch_size, shuffle=False, num_workers=1)
    else:
        test_loader = torch.utils.data.DataLoader(
            RoadSequenceDataset(file_path=config.test_path, transforms=op_tranforms),
            batch_size=args.test_batch_size, shuffle=False, num_workers=1)
    
    img_pred = output_result(model, test_loader, device)

    return img_pred

