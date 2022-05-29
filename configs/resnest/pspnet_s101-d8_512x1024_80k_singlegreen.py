_base_ = '../pspnet/pspnet_r50-d8_512x1024_40k_singlegreen.py'
model = dict(
    pretrained='open-mmlab://resnest101',
    backbone=dict(
        type='ResNeSt',
        stem_channels=128,
        radix=2,
        reduction_factor=4,
        avg_down_stride=True))
work_dir = './work_dirs/pspnet_s101_256x512_80k'