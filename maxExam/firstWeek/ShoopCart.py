# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/9 07:48
# 文件名称: ShoopCart.py


def getGoodsInfo():
    """
    获取商品信息
    :return:
    """
    goods = []
    with open("goods", encoding="utf-8") as f:
        for i in f:
            k, v = i.strip().split("|")
            goods.append({"name":k, "price":v})
        f.close()

    return goods

def showGoods():
    """
    商品信息展示
    :return:
    """
    goods = getGoodsInfo()
    for i in enumerate(goods, 1):
        id, good = i
        print(f"{id} {good['name']} {good['price']}")

if __name__ == '__main__':
    goods = getGoodsInfo()
    print(goods)
    showGoods()