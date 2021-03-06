# import torch
# from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F

# x = torch.rand(5)
# print(x)
#
# x = Variable(x,requires_grad = True)
# y = x *2
#
# grads = torch.FloatTensor([1,2,3,4,5])
# y.backward(grads)
# print(x.grad)

class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()

        self.conv1 = nn.Conv2d(1,6,5)
        self.conv2 = nn.Conv2d(6,16,5)

        self.fc1 = nn.Linear(16*5*5,120)
        self.fc2 = nn.Linear(120,84)
        self.fc3 = nn.Linear(84,10)

    def forward(self, x):

        x = F.max_pool2d(F.relu(self.conv1(x)),(2,2))
        x = F.max_pool2d(F.relu(self.conv2(x)),2)
        x = x.view(-1,self.num_flat_feature(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)

        return x

    def num_flat_feature(self,x):
        size = x.size()[1:]
        num_feature = 1

        for s in size:
            num_feature *= s
        return num_feature


net = Net()

print(net)

