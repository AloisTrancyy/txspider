# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import re

str = '#W#G可重铸#W#r#W耐久度：333/333   品相：#cFFFFFF崭新#r#W#R外观耐久度：0/333#r#W法术防御：108#r#W使用门派：荒火 #r必要等级：#G#cFFFF00天魂 #G壹天壹境界#r#W贵重等级：93#r#R禁交易 #R禁萃取 #r#c00AAEE生命值+630#r#c00AAEE回避+41#r#cBB44BB知彼：受到其他玩家的伤害抵抗力提升41#r#cFF8800·白刃：挥砍重击上升59#r#cFF8800·崩击：钝击重击上升44#r#cBB44BB·人祸：对其他玩家的伤害加成力提升18#r#cBB44BB·御心：会心减伤力+37#r#W#cFF9966怒战(8/8)#r　　#cFF9966盔 #cFF9966肩铠 #cFF9966铠 #cFF9966腿甲 #cFF9966摆 #cFF9966腕甲 #cFF9966带 #cFF9966靴 #r　　#c00FFFF特技属性：猛攻+20(最大值20)#r#G天魄等级 LV.7#r#c7ecef4·挥砍化解+8[+17]#r#c7ecef4·定力+10[+22]#r#c7ecef4·命中+3[+9]#r#c7ecef4·知彼+4[+12]#r#G天魄组合特效#r#c888888#r#c7ecef4(#G52#c7ecef4/56)#c888888天魄强力特效#r#c7ecef4(#G52#c7ecef4/56)#c888888全系技能威力+1%#r#c8A00FF崩击：钝击重击上升10#r#W加护值　^85^85^85^86^86^86^87^87^87^88^88^88^89^89^89^90^90^90^91^91'
props = ["白刃", "崩击", "人祸", "御心", "知彼"]
datas = []
for value in str.split('#'):
    if value is None or value == '':
        continue
    if value.isalpha():
        continue
    data = {}
    for prop_key in props:
        if prop_key in value:
            replaced = value.replace('cFF8800', '').replace('cBB44BB', '').replace('c7ecef4', '').replace('c8A00FF', '')
            prop_value = re.findall(r"\d+\.?\d*", replaced)
            data[prop_key] = prop_value
    if len(data) > 0:
        datas.append(data)
print(datas)
