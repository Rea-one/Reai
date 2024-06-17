# --*-- coding:utf-8 --*--
#
# 项目：Reai
# 作者：Reasone
# 日期：2024年06月17日
#


import torch.nn as nn


class Reflection(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(Reflection, self).__init__()
        self.net = [nn.Linear(input_size, hidden_size),
                    nn.Linear(hidden_size, hidden_size),
                    nn.Linear(hidden_size, hidden_size),
                    nn.Linear(hidden_size, output_size)]
        self.relu = nn.ReLU()

    def forward(self, x):
        for elem in self.net:
            x = self.relu(elem(x))
        return x

