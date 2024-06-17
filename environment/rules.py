# --*-- coding:utf-8 --*--
#
# 项目：Reai
# 作者：Reasone
# 日期：2024年06月17日
#


import numpy as np
import personality.recognize as rcg


class World:
    def __init__(self, vertical=32, horizontal=32):
        self.vertical = vertical
        self.horizontal = horizontal
        self.area = self.vertical * self.horizontal
        self.box = np.zeros((self.vertical, self.horizontal))
        self.record = []

    def born(self):
        current = len(self.record)
        order = np.random.randint(10, 15)
        if order > current:
            self.record.extend([rcg.Recognize() for _ in range(order - current)])

    def set_feed(self, vertical, horizontal):
        self.box[vertical][horizontal] = np.random.randint(1, 10)

    def phenomena(self, vertical, horizontal):
        result = self.box[vertical][horizontal]
        self.box[vertical][horizontal] = 0
        return result

    def feedback(self, order):
        current_action = self.record[order].action()
        if current_action is None:
            del self.record[order]
        else:
            self.record[order].feed(self.phenomena(current_action[0], current_action[1]))
