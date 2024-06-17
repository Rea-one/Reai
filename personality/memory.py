# --*-- coding:utf-8 --*--
#
# 项目：Reai
# 作者：Reasone
# 日期：2024年06月17日
#

import numpy as np
import torch
import torch.nn as nn


class Memory:
    def __init__(self):
        self.memory = []

    def remember(self, something):
        self.memory.append(something)
