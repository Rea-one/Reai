# --*-- coding:utf-8 --*--
#
# 项目：Reai
# 作者：Reasone
# 日期：2024年06月17日
#


import numpy as np
import torch
import torch.nn as nn

import personality.reflection as rfc
import personality.memory as mmr


class Recognize:
    def __init__(self):
        self.me = self
        self.satisfaction = 0
        self.memory = mmr.Memory()

        self.current = torch.tensor([np.random.randint(0, 15), np.random.randint(0, 15)],
                                    dtype=torch.float32)
        self.energy = 64
        self.feedback = rfc.Reflection(2, 10, 2)

    def action(self):
        if self.energy > 0:
            self.current = torch.tensor([np.abs(int(elem)) for elem in self.feedback(self.current)],
                                        dtype=torch.float32)
            self.energy -= 1
            # 在返回前将current转换为整数
            return self.current.type(torch.int16)
        else:
            return None

    def feed(self, energy):
        self.energy += energy
        self.satisfaction += self.energy * energy
