# -*- coding: utf-8 -*-

# @Author  : super
# @Time    : 2018/1/29
# @desc    : 推荐算法


def product_set(prefs):
    product = [x for x in prefs]
    return product


def read_pre(prefs_str):
    prefs = dict()
    for line in prefs_str.split('\n'):
        parts = line.rstrip().split()
        if len(parts) == 2:
            userId, itemId = parts
            prefs.setdefault(userId, {})
            prefs[userId].update({itemId: 1})
    return prefs


def jaccard_distance(prefs, user1, user2):
    s1 = set(prefs[user1].keys())
    s2 = set(prefs[user2].keys())
    return 1.0 * len(s1.intersection(s2)) / len(s1.union(s2))


if __name__ == '__main__':
    prefs_str = '''\
    david 百年孤独
    david 霍乱时期的爱情
    andy 霍乱时期的爱情
    jack 浪潮之巅
    jack 失控
    jack 创业维艰
    david 从0到1
    michale 寻路中国:从乡村到工厂的自驾之旅
    michale 背包十年:我的职业是旅行
    ann 活着
    ann 霍乱时期的爱情
    ann 迟到的间隔年
    joel 巨人的陨落:世纪三部曲
    joel 中国历代政治得失
    joel 人类简史:从动物到上帝
    joel 失控
    jim 背包十年:我的职业是旅行
    jim 迟到的间隔年
    ray 霍乱时期的爱情
    ray 迟到的间隔年
    ray 枪炮、病菌与钢铁:人类社会的命运
    '''
    print(prefs_str)
    print(read_pre(prefs_str))
    prefs = read_pre(prefs_str)
    print(product_set(prefs))
