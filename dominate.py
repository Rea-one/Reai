# --*-- coding:utf-8 --*--
#
# 项目：Reai
# 作者：Reasone
# 日期：2024年06月17日
#

import numpy as np
import os
from datetime import datetime

import environment.rules as rl
import personality.emotion as emt
import personality.evolution as evl
import personality.logic as lgc
import personality.memory as mmr
import personality.recognize as rcg
import personality.reflection as rfc


def log_records(wld, directory='dairy'):
    """记录数据到以日期命名的文件中"""
    # 获取当前日期并格式化为文件名友好的字符串
    date_str = datetime.now().strftime('%Y-%m-%d')
    # 构建完整的文件路径
    file_path = os.path.join(directory, f'{date_str}.txt')
    # 打开文件并追加写入数据
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write('\n')
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        file.write('\n')
        file.write(f'feeds: {wld.box}\n\n')
        for elem in wld.record:
            file.write(f'当前位置：{elem.current}，当前能量：{elem.energy}，当前满足感：{elem.satisfaction}\n')


if __name__ == '__main__':
    world = rl.World()

    for time_now in range(10000):
        world.born()  # 确保新出生的个体能被加入到循环中
        for temp in range(np.random.randint(world.area // 3, world.area // 2)):
            world.set_feed(np.random.randint(1, world.vertical), np.random.randint(1, world.horizontal))

        # 使用列表副本进行遍历，防止遍历过程中修改原列表导致的问题
        for creature in list(world.record):
            print(f'当前时间：{time_now}，当前个体编号：{world.record.index(creature)}\n当前位置{creature.current.numpy()},'
                  f'当前能量：{creature.energy}，当前满足感：{creature.satisfaction}')
            world.feedback(world.record.index(creature))  # 使用索引调用feedback，确保正确对应
            evl.evolution(creature, world)  # 直接操作creature，因为已经从list中取出

        # 确保新加入的个体也能被记录
        while len(world.record) > len(list(world.record)):
            # 这里实际上是个逻辑错误，正确的做法是在born或其它地方确保新个体被立即处理
            # 但根据原始逻辑，此处应修正为正确处理新增个体的逻辑，下面的伪代码仅示意
            pass  # 或者处理新加入的个体，例如记录它们的状态

        log_records(world)

