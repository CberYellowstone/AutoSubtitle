# -*- coding: utf-8 -*-
import itertools
import os
import sys
import time

import cv2
import numpy as np

opening_old = ['1000011010001100010000000000000000000000000000000000000000000000','1100100000010000110010111001011101100100001000000001001011000001','1100100000010000110010111001011001100100001000000001001011000001']
opening_new = ['1110010111001100000100010111000010010000000100000001001100000110','1101010010110011010000111001000101100000000100000011100010000001']
opening_newnew1 = [
    "1000111010010001100100001100101011000011011000010011001010000110",
    "1011100111011000101101000001011000010010001010001000110100100010",
]
opening_newnew2 = [
    "1010101010101100010101010011010100110101100100001010100010001000",
    "1010100111011000111000001000011100000111001000001000110000000010",
]

openings = [opening_old, opening_new, opening_newnew1, opening_newnew2]

subtitle_head = """
[Script Info]
; Script generated by Aegisub 3.2.2
; http://www.aegisub.org/
Title: Default Aegisub file
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: None
PlayResX: 1920
PlayResY: 1080

[Aegisub Project Garbage]
Audio File: $$FILE$$
Video File: $$FILE$$

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: 未定义#正文#1,Resource Han Rounded CN,107,&H00FFFFFF,&H00FFFFFF,&H00000000,&H910E0807,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 路人男#正文#1,Resource Han Rounded CN,107,&H00FCA439,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 死亡flag#正文#1,Resource Han Rounded CN,107,&H0042FFF8,&H00FFFFFF,&H00000000,&H17FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 生存flag#正文#1,Resource Han Rounded CN,107,&H00BAFF48,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 恋爱flag#正文#1,Resource Han Rounded CN,107,&H00F4A9FF,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 失恋flag#正文#1,Resource Han Rounded CN,107,&H00FFED7D,&H00FFFFFF,&H00000000,&H17FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 毁灭flag#正文#1,Resource Han Rounded CN,107,&H00BDC805,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 路人妹#正文#1,Resource Han Rounded CN,107,&H00BF7DF7,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 娜娜#正文#1,Resource Han Rounded CN,107,&H004F83FA,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 小美#正文#1,Resource Han Rounded CN,107,&H0091E1FB,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 死神No.13#正文#1,Resource Han Rounded CN,107,&H0089FE97,&H00FFFFFF,&H00000000,&H17FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 死神No.1#正文#1,Resource Han Rounded CN,107,&H008428CA,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 贪婪#正文#1,Resource Han Rounded CN,107,&H00D866AD,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 愤怒#正文#1,Resource Han Rounded CN,107,&H005D54EE,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 嫉妒#正文#1,Resource Han Rounded CN,107,&H00C07DF8,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 神#正文#1,Resource Han Rounded CN,107,&H00D2FEFF,&H00FFFFFF,&H00000000,&H17FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 洋红色#正文#1,Resource Han Rounded CN,107,&H00A643F6,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 东云色#正文#1,Resource Han Rounded CN,107,&H009196F8,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 淡紫色#正文#1,Resource Han Rounded CN,107,&H00D97092,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 深红色#正文#1,Resource Han Rounded CN,107,&H00251AF0,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 土黄色#正文#1,Resource Han Rounded CN,107,&H0039B0EB,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 玫瑰色#正文#1,Resource Han Rounded CN,107,&H007848FE,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 酒红色#正文#1,Resource Han Rounded CN,107,&H008A25E1,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 橙色#正文#1,Resource Han Rounded CN,107,&H005183FC,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 蓝色#正文#1,Resource Han Rounded CN,107,&H00F7797C,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 绿色#正文#1,Resource Han Rounded CN,107,&H0090DB83,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 转场#1,TsangerYuYangT W02,100,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,8,0,2,10,10,350,1
Style: 旁白#1,Source Han Serif CN Heavy,110,&H00FFFFFF,&H00FFFFFF,&H00000000,&H910E0807,0,0,0,0,100,100,2,0,1,9,0,2,135,135,160,1
Style: 开场白,Source Han Sans CN,120,&H00FFFFFF,&H00FFFFFF,&H00000000,&H910E0807,-1,0,0,0,100,100,2,0,1,7,4,2,135,135,50,1
Style: 转场#2,TsangerYuYangT W02,100,&H00FFFFFF,&H000000FF,&H00FFFFFF,&H00000000,-1,0,0,0,100,100,0,0,1,12,4,2,10,10,350,1
Style: 旁白#2,Source Han Serif CN Heavy,110,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H290E0807,0,0,0,0,100,100,2,0,1,13,4,2,135,135,160,1
Style: 白边框#正文#2,Resource Han Rounded CN,107,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H17000000,-1,0,0,0,100,100,2,0,1,11,4,2,135,135,160,1
Style: 译注,Source Han Sans CN,80,&H00FFFFFF,&H00FFFFFF,&H00000000,&H910E0807,-1,0,0,0,100,100,2,0,1,5,2,7,50,0,50,1
Style: フェン#正文#1,Resource Han Rounded CN,107,&H001854F0,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 样式1,Source Han Sans CN,72,&H00000000,&H00FFFFFF,&H00FFFFFF,&H910E0807,-1,0,0,0,100,100,2,0,1,6,0,8,50,0,50,1


[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

def phash(img):
    #加载并调整图片为32x32灰度图片
    img = cv2.resize(img, (8, 8), interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img.astype(np.float32)
    #离散余弦变换
    img = cv2.dct(img)
    hash_str = ''
    img = img[0:8, 0:8]
    avg = sum(img[i, j] for i, j in itertools.product(range(8), range(8)))
    avg = avg/64
    #获得hsah
    for i, j in itertools.product(range(8), range(8)):
        hash_str = f'{hash_str}1' if img[i, j] > avg else f'{hash_str}0'
    return hash_str

def get_color_rate(frame,lower,upper):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    ratio_green = cv2.countNonZero(mask)/(frame.size/3)
    colorPercent = (ratio_green * 100)
    return np.round(colorPercent, 2)

def hamming_distance(str1, str2):
    #计算汉明距离
    if len(str1) != len(str2):
        return 0
    return sum(str1[i] != str2[i] for i in range(len(str1)))

def isset(v): 
    try:
        type(eval(v))
    except NameError:
        return  0
    return  1 


def frames_to_timecode(framerate,frames):
    # 视频 通过视频帧转换成时间|framerate: 视频帧率|frames: 当前视频帧数|return:时间（00:00:01.001）
    return '{0:02d}:{1:02d}:{2:02d}.{3:02d}'.format(int(frames / (3600 * framerate)),
                                                    int(frames / (60 * framerate) % 60),
                                                    int(frames / framerate % 60),
                                                    int(frames / framerate % 1 * 100))

def get_people(img):
    mobuo_rate = get_color_rate(img,np.array([100,185,225]),np.array([110,225,255]))
    flag_rate = get_color_rate(img,np.array([27,155,240]),np.array([37,215,255]))
    renai_rate = get_color_rate(img,np.array([150,70,225]),np.array([160,90,255]))
    seizon_rate = get_color_rate(img,np.array([75,150,230]),np.array([80,190,255]))
    mobumi_rate = get_color_rate(img,np.array([20,90,245]),np.array([25,120,255]))
    purple_rate = get_color_rate(img,np.array([125,105,190]),np.array([135,135,220]))
    kaqi_rate = get_color_rate(img,np.array([15,95,225]),np.array([25,130,255]))
    kaqi_rate = 0 #这个奇葩颜色貌似不常见，禁用算了
    dongyun_rate = get_color_rate(img,np.array([0,83,225]),np.array([10,125,255]))
    yanghong_rate = get_color_rate(img,np.array([162,140,215]),np.array([170,180,255]))
    yanghong2_rate = get_color_rate(img,np.array([160,200,205]),np.array([165,220,230]))
    siturenn_rate = get_color_rate(img,np.array([90,75,205]),np.array([95,145,255]))
    darkgreen_rate = get_color_rate(img,np.array([70,210,120]),np.array([75,255,155]))
    rose_rate = get_color_rate(img,np.array([160,210,195]),np.array([165,250,240]))
    kami_rate = get_color_rate(img,np.array([25,110,245]),np.array([35,130,255]))
    darkred_rate = get_color_rate(img,np.array([175,240,210]),np.array([180,255,225]))
    narrator_rate = get_color_rate(img,np.array([0,0,225]),np.array([175,5,255]))
    rate_list = [mobuo_rate,flag_rate,renai_rate,seizon_rate,mobumi_rate,purple_rate,kaqi_rate,dongyun_rate,yanghong_rate,yanghong2_rate,siturenn_rate,darkgreen_rate,rose_rate,kami_rate,darkred_rate]
    people_list = ["mobuo","flag","renai","seizon","mobumi","purple","kaqi","dongyun","yanghong","yanghong","siturenn","darkgreen","rose","kami","darkred"]
    max_rate = max(rate_list)
    if(max_rate < 0.2):
        if(len([x for x in rate_list if x > 4]) > 1):
            return "undefined"
        elif(narrator_rate > 25):
            return "narrator"
        else:
            return "undefined"
    return people_list[rate_list.index(max_rate)]

def people2style(people):
    style_dict = {
        "mobuo": "路人男#正文#1",
        "flag": "死亡flag#正文#1",
        "seizon": "生存flag#正文#1",
        "renai": "恋爱flag#正文#1",
        "Opening": "开场白",
        "trans": "转场#1",
        "mobumi": "路人妹#正文#1",
        "purple": "淡紫色#正文#1",
        "kaqi": "土黄色#正文#1",
        "dongyun": "东云色#正文#1",
        "yanghong": "洋红色#正文#1",
        "undefined": "未定义#正文#1",
        "narrator": "旁白#1",
        "siturenn": "失恋flag#正文#1",
        "darkgreen": "绿色#正文#1",
        "rose": "玫瑰色#正文#1",
        "kami": "神#正文#1",
        "darkred": "深红色#正文#1",
    }
    return style_dict[people]

def add_sub(subtext,begintime,endingtime,subpeople):
    global sub_num
    global subtitle
    style = people2style(subpeople)
    subtitle = (
        f'{subtitle}Dialogue: 1,{begintime},{endingtime},{style},{subpeople}'
        + ",0,0,0,,"
        + subtext
        + str(sub_num)
        + "\n"
    )

    sub_num += 1


def add_op(frame_rate, begin_frame_num, opType):
    match opType:
        case 0:
            add_sub(
                "没有任何优点的路人男",
                frames_to_timecode(frame_rate, begin_frame_num),
                frames_to_timecode(frame_rate, begin_frame_num + (1.87 * frame_rate)),
                "Opening",
            )
            add_sub(
                "在路人男面前出现的女孩，她的真实身份是...?",
                frames_to_timecode(frame_rate, begin_frame_num + (1.87 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (4.57 * frame_rate)),
                "Opening",
            )
            add_sub(
                "死亡flag?",
                frames_to_timecode(frame_rate, begin_frame_num + (4.57 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (5.77 * frame_rate)),
                "Opening",
            )
            add_sub(
                "路人男能成功回避死亡flag吗!?",
                frames_to_timecode(frame_rate, begin_frame_num + (5.77 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (8.47 * frame_rate)),
                "Opening",
            )
            add_sub(
                "全力回避flag酱!",
                frames_to_timecode(frame_rate, begin_frame_num + (8.47 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (10.84 * frame_rate)),
                "Opening",
            )
        case 1:
            add_sub(
                "立起来了!",
                frames_to_timecode(frame_rate, begin_frame_num + (2.63 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (3.59 * frame_rate)),
                "Opening",
            )
            add_sub(
                "全力回避flag酱!",
                frames_to_timecode(frame_rate, begin_frame_num + (4.9 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (6.61 * frame_rate)),
                "Opening",
            )
        case 2:
            add_sub(
                "flag回收",
                frames_to_timecode(frame_rate, begin_frame_num + (0.44 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (2.19 * frame_rate)),
                "narrator",
            )
            add_sub(
                "是引导灵魂走向正确的命运的",
                frames_to_timecode(frame_rate, begin_frame_num + (2.19 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (4.86 * frame_rate)),
                "narrator",
            )
            add_sub(
                "天界之使命",
                frames_to_timecode(frame_rate, begin_frame_num + (4.86 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (6.73 * frame_rate)),
                "narrator",
            )
            add_sub(
                "而威胁flag回收的存在——",
                frames_to_timecode(frame_rate, begin_frame_num + (6.73 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (9.27 * frame_rate)),
                "narrator",
            )
            add_sub(
                "恶魔，从地狱出现了",
                frames_to_timecode(frame_rate, begin_frame_num + (9.27 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (11.90 * frame_rate)),
                "narrator",
            )
            add_sub(
                "没能被回收flag的灵魂",
                frames_to_timecode(frame_rate, begin_frame_num + (11.90 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (14.19 * frame_rate)),
                "narrator",
            )
            add_sub(
                "会因为走向错误的命运而堕入地狱",
                frames_to_timecode(frame_rate, begin_frame_num + (14.19 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (17.69 * frame_rate)),
                "narrator",
            )
            add_sub(
                "为了阻止试图扩大地狱势力的恶魔",
                frames_to_timecode(frame_rate, begin_frame_num + (17.69 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (20.82 * frame_rate)),
                "narrator",
            )
            add_sub(
                "flag们今天也要战斗!",
                frames_to_timecode(frame_rate, begin_frame_num + (20.82 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (22.73 * frame_rate)),
                "narrator",
            )
            add_sub(
                "绝对回收Death Flag决不放弃",
                frames_to_timecode(frame_rate, begin_frame_num + (24.52 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (28.36 * frame_rate)),
                "Opening",
            )
            add_sub(
                "干劲满满!",
                frames_to_timecode(frame_rate, begin_frame_num + (28.36 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (30.36 * frame_rate)),
                "Opening",
            )
            add_sub(
                "却总是失败的死神啊!",
                frames_to_timecode(frame_rate, begin_frame_num + (30.36 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (32.94 * frame_rate)),
                "Opening",
            )
            add_sub(
                "但是下次一定会成功回收!",
                frames_to_timecode(frame_rate, begin_frame_num + (32.94 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (35.77 * frame_rate)),
                "Opening",
            )
            add_sub(
                "绝对回收! 绝对回收! 绝对回收!",
                frames_to_timecode(frame_rate, begin_frame_num + (35.77 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (38.02 * frame_rate)),
                "Opening",
            )
            add_sub(
                "Flag绝对回收! 绝对回收!",
                frames_to_timecode(frame_rate, begin_frame_num + (38.02 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (39.98 * frame_rate)),
                "Opening",
            )
            add_sub(
                "DeDeDe Death Flag",
                frames_to_timecode(frame_rate, begin_frame_num + (39.98 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (41.02 * frame_rate)),
                "Opening",
            )
            add_sub(
                "绝对回收! 绝对回收! 绝对回收!",
                frames_to_timecode(frame_rate, begin_frame_num + (41.02 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (43.07 * frame_rate)),
                "Opening",
            )
            add_sub(
                "Flag绝对回收! 绝对回收! Death Flag",
                frames_to_timecode(frame_rate, begin_frame_num + (43.07 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (46.19 * frame_rate)),
                "Opening",
            )
        case 3:
            add_sub(
                "绝对回收Death Flag决不放弃",
                frames_to_timecode(frame_rate, begin_frame_num + (1.73 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (5.57 * frame_rate)),
                "Opening",
            )
            add_sub(
                "干劲满满!",
                frames_to_timecode(frame_rate, begin_frame_num + (5.57 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (7.57 * frame_rate)),
                "Opening",
            )
            add_sub(
                "却总是失败的死神啊!",
                frames_to_timecode(frame_rate, begin_frame_num + (7.57 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (10.15 * frame_rate)),
                "Opening",
            )
            add_sub(
                "但是下次一定会成功回收!",
                frames_to_timecode(frame_rate, begin_frame_num + (10.15 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (12.98 * frame_rate)),
                "Opening",
            )
            add_sub(
                "绝对回收! 绝对回收! 绝对回收!",
                frames_to_timecode(frame_rate, begin_frame_num + (12.98 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (15.23 * frame_rate)),
                "Opening",
            )
            add_sub(
                "Flag绝对回收! 绝对回收!",
                frames_to_timecode(frame_rate, begin_frame_num + (15.23 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (17.19 * frame_rate)),
                "Opening",
            )
            add_sub(
                "DeDeDe Death Flag",
                frames_to_timecode(frame_rate, begin_frame_num + (17.19 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (18.23 * frame_rate)),
                "Opening",
            )
            add_sub(
                "绝对回收! 绝对回收! 绝对回收!",
                frames_to_timecode(frame_rate, begin_frame_num + (18.23 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (20.28 * frame_rate)),
                "Opening",
            )
            add_sub(
                "Flag绝对回收! 绝对回收! Death Flag",
                frames_to_timecode(frame_rate, begin_frame_num + (20.28 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (23.40 * frame_rate)),
                "Opening",
            )


# 视频帧总数
current_frame_num = begin_frame_num = last_frame_num = 0
last_pic_hash = ''
op = trans = False
op_match_times = op_bg_num = 0
sub_num = 1
Err = False


def autosub(videopath, subpath, opType):
    start = time.time()
    global op_match_times
    global op
    global trans
    global last_pic_hash
    global current_frame_num
    global begin_frame_num
    global last_frame_num
    global subtitle
    global sub_num
    global current_pic
    global pic_current_hash
    global hamdistant
    global people_pic
    global people_hash
    global people
    global Err
    opening = openings[opType]
    subtitle = subtitle_head.replace("$$FILE$$",os.path.abspath(videopath))
    source_video = cv2.VideoCapture(videopath)
    global op_bg_num
    isOpened = bool(source_video.isOpened())
    if isOpened:
        frame_rate = round(source_video.get(5),2)
        while True:
            ret, frame = source_video.read()
            # print(current_frame_num)
            if ret == False:
                break

            assert 0 not in frame[950:1045, 810:910].shape, "视频分辨率应为1920*1080"
            pic_current_hash = phash(frame[950:1045, 810:910])
            hmdistant = hamming_distance(last_pic_hash,pic_current_hash)

            switch_hash = phash(frame[940:1060, 360:1540])

            # match_op_hash = phash(frame)
            # if current_frame_num == 137:
            #     print(match_op_hash)
            #     print(hamming_distance(match_op_hash, opening[0]))
            #     cv2.imshow("frame", frame)
            #     while True:
            #         if cv2.waitKey(1) & 0xFF == ord("q"):
            #             break
            # if current_frame_num == 234:
            #     print(match_op_hash)
            #     print(hamming_distance(match_op_hash, opening[0]))
            #     print(hamming_distance(match_op_hash, opening[1]))
            #     cv2.imshow("frame", frame)
            #     while True:
            #         if cv2.waitKey(1) & 0xFF == ord("q"):
            #             break
            #     exit()
            if (op_match_times < 2):
                match_op_hash = phash(frame)
                # print(match_op_hash)
                # print(hamming_distance(match_op_hash,opening[0]))
                if (
                    match_op_hash in opening
                    or (
                        op_match_times == 0
                        and hamming_distance(match_op_hash, opening[0]) < 3
                    )
                    or (
                        op_match_times == 1
                        and hamming_distance(match_op_hash, opening[1]) < 3
                    )
                ):
                    op = not op
                    op_match_times += 1
                    if op_match_times == 1:
                        # print(str(current_frame_num) + " | 开场白起点")
                        op_bg_num = current_frame_num
                        add_op(frame_rate, op_bg_num, opType)
                        for _ in range(int(frame_rate * 4)):
                            source_video.read()
                            current_frame_num += 1
                    if op_match_times == 2:
                        # print(str(current_frame_num) + " | 开场白结束")
                        print(f'{str(op_bg_num)} <-> {str(current_frame_num)} | 开场白')
                    begin_frame_num = last_frame_num = current_frame_num + 15
                if(op):
                    current_frame_num += 1
                    # print(match_op_hash)
                    continue

            if(hamming_distance(switch_hash,'1010010011000000101010001100000001000100000001011000011010100000') < 10):
                trans = True   #识别转场
            if ((hmdistant > 13) and (current_frame_num != 0)):
                if (current_frame_num-last_frame_num > (frame_rate/2)):
                    people = get_people(people_pic)
                    if(trans):
                        people = "trans"
                        trans = False
                        begin_frame_num += int(frame_rate/10)

                    print(f'{sub_num} | {current_frame_num-1} <-> {current_frame_num} | hmdst: {hmdistant} | gap: {current_frame_num - last_frame_num} | {frames_to_timecode(frame_rate, begin_frame_num)} --> {frames_to_timecode(frame_rate, current_frame_num)} | people: {people}')

                    add_sub("示范性字幕",frames_to_timecode(frame_rate,begin_frame_num),frames_to_timecode(frame_rate,current_frame_num),people)

                begin_frame_num = current_frame_num
                last_frame_num = current_frame_num

            last_pic_hash = pic_current_hash
            people_pic = frame[940:1040,800:1100]
            people_hash = phash(people_pic)
            current_frame_num += 1
    else:
        print("源视频读取出错")
        Err = True
    print("finish!")
    if(not Err):
        with open(subpath,'w+',encoding='utf-8') as q:
            q.write(subtitle)
    end = time.time()
    print(f'耗时：{str(end - start)}秒')
    return Err
