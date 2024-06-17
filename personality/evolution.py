# --*-- coding:utf-8 --*--
#
# 项目：Reai
# 作者：Reasone
# 日期：2024年06月17日
#

import numpy as np
import torch
import torch.nn as nn


def evolution(self, world, mutation_rate=12):
    learn(self, world)
    mutation(self.feedback, mutation_rate)


def learn(self, world):
    count = 10
    length = len(world.record)
    if length > 0:
        for idx in range(count):
            others = world.record[np.random.randint(0, len(world.record))]
            if others != self:
                difference = compare(self, others)
                if difference == 1:
                    pass
                elif difference == -1:
                    temp = np.random.randint(1, 3)
                    for order in range(temp):
                        if np.random.randint(0, 2) == 1:
                            self.feedback.net[0] = others.feedback.net[0]
                        if np.random.randint(0, 2) == 1:
                            self.feedback.net[3] = others.feedback.net[3]
                        self.feedback.net[np.random.randint(1, 3)] \
                            = others.feedback.net[np.random.randint(1, 3)]
                count += 1


def mutation(model, mutation_rate):
    for param in model.parameters():
        if np.random.random() < mutation_rate:
            param.data = param.data + np.random.normal(0, 0.1, param.shape)


def compare(self, others):
    if self.satisfaction > others.satisfaction:
        return 1
    elif self.satisfaction < others.satisfaction:
        return -1
    else:
        return 0
