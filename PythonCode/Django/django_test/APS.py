# -*- coding: utf-8 -*-

from datetime import datetime
# import os
from apscheduler.schedulers.blocking import BlockingScheduler


def tick():
    """要执行的定时任务"""
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    # 创建scheduler对象
    scheduler = BlockingScheduler()
    # 添加任务：
    # interval:表示时间间隔
    # seconds:以秒为时间单位间隔
    scheduler.add_job(tick, 'interval', seconds=3)
    # 添加任务：
    # cron:表示定时的时间
    # hour:每天几点
    # minute:小时对应的分钟
    # 每天特定时间（9:23）执行一次
    scheduler.add_job(tick, 'cron', hour=19, minute=23)
    # print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
    