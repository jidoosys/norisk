#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import random
from datetime import datetime

while True:
    # 
    # このBOTは、甘い言葉に誘われコードの中身も確認しないでBOTを使用し損失を出してしまう人を救う、実験プロジェクトです。
    # 社会実験として公開してみました。
    # より多くのトレーダーさんにオススメされることで輝きます。
    # 
    # シェアお願いします（ネタバレ厳禁）
    # 
    print( datetime.now().strftime("%Y/%m/%d %H:%M:%S") + ' リスク判定中...')
    time.sleep(1)
    print( datetime.now().strftime("%Y/%m/%d %H:%M:%S") + ' リスクレシオ = ' + str(random.randrange(-9,10) /10))
    print( datetime.now().strftime("%Y/%m/%d %H:%M:%S") + ' リスクがあるためスルーします' )
    time.sleep(4)
