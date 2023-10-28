# -*- coding: utf-8 -*-
# config
"""
new Env('xiaoym参数设置');
如需启用此处设置，需将文件重命名为config.py
"""
"""钢镚设置"""
cmzg_config = {
    'printf': 1,  # 实时日志开关,1为开，0为关

    'debug': 1,  # debug模式开关,1为开,0为关

    'max_workers': 5,  # 线程数量设置,设置为5，即最多有5个任务同时进行

    'txbz': 8000,  # 设置提现标准,不低于3000，平台3000起提,设置为8000，即为8毛起提

    'sendable': 1,  # 企业微信推送开关,1为开，0为关开启后必须设置qwbotkey才能运行

    'pushable': 1,  # wxpusher推送开关,1为开，0为关,开启后必须设置pushconfig才能运行

    'delay_time': 30,  # 并发延迟设置,设置为30即每隔30秒新增一个号做任务，直到数量达到max_workers

    'upload': 0,  # 上传检测号信息到服务器设置，1为上传，相应地也可以从云端获取检测号字典；0为不上传， 相应地也不能从云端获取检测号字典
}
"""小阅阅设置"""
xyy_config = {
    'printf': 1,  # 实时日志开关 1为开，0为关

    'debug': 0,  # debug模式开关 1为开，打印调试日志；0为关，不打印

    'max_workers': 5,  # 线程数量设置 设置为5，即最多有5个任务同时进行

    'txbz': 10000,  # 设置提现标准 不低于3000，平台标准为3000 设置为8000，即为8毛起提

    'sendable': 1,  # 企业微信推送开关 1开0关

    'pushable': 1,  # wxpusher推送开关 1开0关

    'delay_time': 20,  # 并发延迟设置 设置为20即每隔20秒新增一个号做任务，直到数量达到max_workers

    'upload': 0,  # 上传检测号信息到服务器设置，1为上传，相应地也可以从云端获取检测号字典；0为不上传， 相应地也不能从云端获取检测号字典
}
"""智慧元宝设置"""
aio_config = {
    'printf': 1,  # 实时日志开关 1为开，0为关

    'debug': 0,  # debug模式开关 1为开，打印调试日志；0为关，不打印

    'max_workers': 5,  # 线程数量设置 设置为5，即最多有5个任务同时进行

    'txbz': 10000,  # 设置提现标准 不低于3000，平台标准为3000 设置为8000，即为8毛起提

    'sendable': 1,  # 企业微信推送开关 1开0关

    'pushable': 1,  # wxpusher推送开关 1开0关

    'delay_time': 20  # 并发延迟设置 设置为20即每隔20秒新增一个号做任务，直到数量达到max_workers
}
"""人人帮设置"""
rrb_config = {
    'printf': 1,  # 实时日志开关 1为开，0为关

    'debug': 0,  # debug模式开关 1为开，打印调试日志；0为关，不打印

    'max_workers': 5,  # 线程数量设置 设置为5，即最多有5个任务同时进行

    'txbz': 10000,  # 设置提现标准 不低于3000，平台标准为3000 设置为8000，即为8毛起提

    'sendable': 1,  # 企业微信推送开关 1开0关

    'pushable': 1,  # wxpusher推送开关 1开0关

    'delay_time': 20  # 并发延迟设置 设置为20即每隔20秒新增一个号做任务，直到数量达到max_workers
}
"""花花设置"""
hh_config = {
    'printf': 1,  # 实时日志开关 1为开，0为关

    'debug': 0,  # debug模式开关 1为开，打印调试日志；0为关，不打印

    'max_workers': 5,  # 线程数量设置 设置为5，即最多有5个任务同时进行

    'txbz': 5000,  # 设置提现标准 不低于3000，平台标准为3000

    'sendable': 1,  # 企业微信推送开关 1开0关

    'pushable': 1,  # wxpusher推送开关 1开0关

    'delay_time': 20  # 并发延迟设置 设置为20即每隔20秒新增一个号做任务，直到数量达到max_workers
}
"""每天赚设置"""
mtz_config = {
    'printf': 1,  # 实时日志开关 1为开，0为关
    'debug': 0,  # debug模式开关
    'txbz': 1000,  # 设置提现标准 不低于1000，平台的提现标准为1000
    'sendable': 1,  # 企业微信推送开关 1为开，0为关 开启后必须设置qwbotkey才能运行
    'pushable': 1,  # wxpusher推送开关 开启后必须设置pushconfig才能运行
    'max_workers': 5,  # 线程数量设置 填入数字，设置同时跑任务的数量
    'delay_time': 20,  # 设置为20即每隔20秒新增一个号做任务，直到数量达到max_workers
    'total_num': 18  # 设置单轮任务最小数量 设置为18即本轮数量小于18不继续阅读
}

"""提现黑名单设置"""
balcklist = []  # 黑名单中的账号不进行自动提现，填入ck中的name
