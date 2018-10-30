from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
def index(request):
    context = {}
    article_list =[1,2,3]
    context['article_list'] = article_list
    return render(request, 'index.html', context)

def cbg_page(request):
    params = get_params(request)
    print(params)
    result = {}
    article_list =[1,2,3]

    result['article_list'] = article_list
    return render(request, 'cbg-page.html', result)

def delete_role(request):
    result = {}
    result['returncode'] = 0
    result['message'] = "this is message"
    result['result'] = [112,123,23]

#     CbgRoleEntity
#     cbgRoleEntity = cbgRoleMapper.findById(id);
#     if (cbgRoleEntity != null & & !Strings.isNullOrEmpty(cbgRoleEntity.getDataUrl())) {
#     String httpResult = HttpClientUtil.get(cbgRoleEntity.getDataUrl());
#     if (StringUtils.isEmpty(httpResult)){
#     return;
#     }
#     JSONObject
#     jsonObject = JSON.parseObject(httpResult);
#     String
#     json_status = jsonObject.getString("status");
#     if (json_status == null | | !json_status.equals("1")) {
#     return;
#
# }
# JSONObject
# equip = jsonObject.getJSONObject("equip");
# if (equip == null)
# {
# return;
# }
# String
# equip_status = equip.getString("status");
# if (!"2".equals(equip_status)) {
# CbgRoleEntity
# updateRole = new
# CbgRoleEntity();
# updateRole.setYn(0);
# updateRole.setId(cbgRoleEntity.getId());
# cbgRoleMapper.updateByIdSelected(updateRole);
# }
# }
    return HttpResponse(json.dumps(result), content_type="application/json")

def get_params(request):
    params = {}
    params['pageNo'] = request.POST.get('pageNo')
    params['pageNo'] = request.POST.get('pageNo')
    params['pageNo'] = request.POST.get('pageNo')
    params['pageNo'] = request.POST.get('pageNo')
    params['pageNo'] = request.POST.get('pageNo')
    params['pageNo'] = request.POST.get('pageNo')
    params['pageNo'] = request.POST.get('pageNo')
    params['pageNo'] = request.POST.get('pageNo')
    return params

#
# < select
# id = "findByCondition"
# resultMap = "extResultMap"
# parameterType = "com.funny.txstack.entity.cbg.CbgSearch" >
# select
# r.id, r.name, r.url, r.price, r.jiahu, fly_soul_phase, fly_soul_lv,
# lv, xiuwei, equ_xiuwei, sch, pattack_max, mattack_max, pattack_min, mattack_min,
# hit, modadd, cri_add_p, cri_sub_p, mdef, pdef, inprotect, avoid, critical, sex,
# attackhuman, movespeed, castspeed, lianhu, qinghua, xuansu, guhong,
# xiangyun, tinglan, haitang, feihuhuaqiu, tianhulishang, xianhucaijue, canghaisangtian, yeyujiangnan,
# huikanfanghu, duncifanghu, huoyuanfanghu, shuifengdufanghu, wanfeng, huxin,
# taichu, shilifushou, xiyangyang, mawangye, wanshengtianzun, yehuo, dulanggui, haizi_tiayu, vip9, bihai, changong, changkong, fengyuzihuang,
# shuyinghengxie, tianyu, jinbi, junzi, dayu, yuanbao, haizi_jiahu, renwu_tianyu, mourixingguan, zhanying, leizuan, honglian
# from cbg_role r
#
# left
# join
# cbg_data
# d
# on
# r.id = d.role_id
# where
# r.yn = 1
# < if test="lv_level != null " >
# < choose >
# < when
# test = "lv_level == 1" >
# and lv = 69
# < / when >
# < when
# test = "lv_level == 2" >
# and lv & gt;= 70 and lv & lt;= 74
# < / when >
# < when
# test = "lv_level == 3" >
# and lv & gt;= 75 and lv & lt;= 79
# < / when >
# < when
# test = "lv_level == 4" >
# and lv = 80 and fly_soul_phase = 1
# < / when >
# < when
# test = "lv_level == 5" >
# and lv = 80 and fly_soul_phase = 2
# < / when >
# < otherwise >
# and lv & gt;= 69
# < / otherwise >
# < / choose >
# < / if >
# < if test="lv_level == null " >
# < if test="lvmin != null " >
# and lv & gt;=  # {lvmin}
# < / if >
# < if test="lvmax != null " >
# and lv & lt;=  # {lvmax}
# < / if >
# < / if >
# < if test="schoolList != null and schoolList.size() > 0 " >
# and sch in
# < foreach
# collection = "schoolList"
# open = "("
# close = ")"
# separator = ","
# item = "id" >
# # {id}
# < / foreach >
# < / if >
# < if test="jiahu != null " >
# and jiahu & gt;=  # {jiahu}
# < / if >
# < if test="pricemin != null " >
# and price & gt;=  # {pricemin}
# < / if >
# < if test="pricemax != null " >
# and price & lt;=  # {pricemax}
# < / if >
#
# < if test="mhp != null " >
# and mhp & gt;=  # {mhp}
# < / if >
# < if test="msp != null " >
# and msp & gt;=  # {msp}
# < / if >
#
# < if test="xiuwei != null " >
# and xiuwei & gt;=  # {xiuwei}
# < / if >
# < if test="equXiuwei != null " >
# and equ_xiuwei & gt;=  # {equXiuwei}
# < / if >
#
# < if test="pattackMax != null " >
# and pattack_max & gt;=  # {pattackMax}
# < / if >
# < if test="mattackMax != null " >
# and mattack_max & gt;=  # {mattackMax}
# < / if >
# < if test="pattackMin != null " >
# and pattack_min & gt;=  # {pattackMin}
# < / if >
# < if test="mattackMin != null " >
# and mattack_min & gt;=  # {mattackMin}
# < / if >
# < if test="hit != null " >
# and hit & gt;=  # {hit}
# < / if >
# < if test="modadd != null " >
# and modadd & gt;=  # {modadd}
# < / if >
# < if test="attadd != null " >
# and attadd & gt;=  # {attadd}
# < / if >
# < if test="criAddP != null " >
# and cri_add_p & gt;=  # {criAddP}
# < / if >
# < if test="criSubP != null " >
# and cri_sub_p & gt;=  # {criSubP}
# < / if >
# < if test="mdef != null " >
# and mdef & gt;=  # {mdef}
# < / if >
# < if test="pdef != null " >
# and pdef & gt;=  # {pdef}
# < / if >
#
# < if test="xiaogong != null " >
# and pattack_max - pattack_min & lt;=  # {xiaogong}
# < / if >
# < if test="xiaofa != null " >
# and mattack_max - mattack_min & lt;=  # {xiaofa}
# < / if >
#
# < if test="inprotect != null " >
# and inprotect & gt;=  # {inprotect}
# < / if >
# < if test="critical != null " >
# and critical & gt;=  # {critical}
# < / if >
# < if test="avoid != null " >
# and avoid & gt;=  # {avoid}
# < / if >
# < if test="attdef != null " >
# and attdef & gt;=  # {attdef}
# < / if >
# < if test="defhuman != null " >
# and defhuman & gt;=  # {defhuman}
# < / if >
# < if test="attackhuman != null " >
# and attackhuman & gt;=  # {attackhuman}
# < / if >
#
# < if test="inprotect != null " >
# and inprotect & gt;=  # {inprotect}
# < / if >
# < if test="sract != null " >
# and sract & gt;=  # {sract}
# < / if >
# < if test="srbody != null " >
# and srbody & gt;=  # {srbody}
# < / if >
# < if test="srmind != null " >
# and srmind & gt;=  # {srmind}
# < / if >
# < if test="movespeed != null " >
# and movespeed & gt;=  # {movespeed}
# < / if >
# < if test="castspeed != null " >
# and castspeed & gt;=  # {castspeed}
# < / if >
# < if test="attackspeed != null " >
# and attackspeed & gt;=  # {attackspeed}
# < / if >
# < if test="thumpAddP != null " >
# and thump_add_p & gt;=  # {thumpAddP}
# < / if >
# < if test="thumpSubP != null " >
# and thump_sub_p & gt;=  # {thumpSubP}
# < / if >
# < if test="strong != null " >
# and strong & gt;=  # {strong}
# < / if >
# < if test="body != null " >
# and body & gt;=  # {body}
# < / if >
# < if test="quick != null " >
# and quick & gt;=  # {quick}
# < / if >
# < if test="dodge != null " >
# and dodge & gt;=  # {dodge}
# < / if >
# < if test="soul != null " >
# and soul & gt;=  # {soul}
# < / if >
# < if test="mind != null " >
# and mind & gt;=  # {mind}
# < / if >
# < if test="lianhu != null " >
# and lianhu & gt;=  # {lianhu}
# < / if >
# < if test="haiziLv != null " >
# and haizi_lv & gt;=  # {haiziLv}
# < / if >
# < if test="haiziZizhi != null " >
# and haizi_zizhi & gt;=  # {haiziZizhi}
# < / if >
# < if test="haiziWuxue != null " >
# and haizi_wuxue & gt;=  # {haiziWuxue}
# < / if >
#
# < if test="awakeLv != null " >
# and awake_lv & gt;=  # {awakeLv}
# < / if >
# < if test="releaseLv != null " >
# and release_lv & gt;=  # {releaseLv}
# < / if >
# < if test="awakeValue != null " >
# and awake_value & gt;=  # {awakeValue}
# < / if >
# < if test="awakeLv != null " >
# and awake_lv & gt;=  # {awakeLv}
# < / if >
# < if test="releaseLv != null " >
# and release_lv & gt;=  # {releaseLv}
# < / if >
# < if test="awakeValue != null " >
# and awake_value & gt;=  # {awakeValue}
# < / if >
# < if test="minglian != null " >
# and minglian & gt;=  # {minglian}
# < / if >
#
# < if test="qinghua != null " >
# and qinghua = 1
# < / if >
# < if test="xuansu != null " >
# and xuansu = 1
# < / if >
# < if test="guhong != null " >
# and guhong = 1
# < / if >
# < if test="xiangyun != null " >
# and xiangyun = 1
# < / if >
# < if test="tinglan != null " >
# and tinglan = 1
# < / if >
# < if test="haitang != null " >
# and haitang = 1
# < / if >
# < if test="feihuhuaqiu != null " >
# and feihuhuaqiu = 1
# < / if >
# < if test="tianhulishang != null " >
# and tianhulishang = 1
# < / if >
# < if test="xianhucaijue != null " >
# and xianhucaijue = 1
# < / if >
# < if test="canghaisangtian != null " >
# and canghaisangtian = 1
# < / if >
# < if test="yeyujiangnan != null " >
# and yeyujiangnan = 1
# < / if >
# < if test="huikanfanghu != null " >
# and huikanfanghu = 1
# < / if >
# < if test="duncifanghu != null " >
# and duncifanghu = 1
# < / if >
# < if test="huoyuanfanghu != null " >
# and huoyuanfanghu = 1
# < / if >
# < if test="shuifengdufanghu != null " >
# and shuifengdufanghu = 1
# < / if >
#
# < if test="wanfeng != null " >
# and wanfeng = 1
# < / if >
# < if test="huxin != null " >
# and huxin = 1
# < / if >
# < if test="taichu != null " >
# and taichu = 1
# < / if >
# < if test="shilifushou != null " >
# and shilifushou = 1
# < / if >
# < if test="xiyangyang != null " >
# and xiyangyang = 1
# < / if >
# < if test="mawangye != null " >
# and mawangye = 1
# < / if >
# < if test="wanshengtianzun != null " >
# and wanshengtianzun = 1
# < / if >
# < if test="yehuo != null " >
# and yehuo = 1
# < / if >
# < if test="dulanggui != null " >
# and dulanggui = 1
# < / if >
# < if test="ligntMenpai != null " >
# and lignt_menpai = 1
# < / if >
# < if test="haiziTianyu != null " >
# and haizi_tiayu = 1
# < / if >
# < if test="vip9 != null " >
# and vip9 = 1
# < / if >
#
# < if test="bihai != null " >
# and bihai = 1
# < / if >
# < if test="changkong != null " >
# and changkong = 1
# < / if >
# < if test="changong != null " >
# and changong = 1
# < / if >
# < if test="fengyuzihuang != null " >
# and fengyuzihuang = 1
# < / if >
#
# < if test="maorixingguan != null " >
# and mourixingguan = 1
# < / if >
#
# < if test="renwuTianyu != null " >
# and renwu_tianyu = 1
# < / if >
#
# < if test="shuyinghengxie != null " >
# and shuyinghengxie = 1
# < / if >
#
# < if test="zhanying != null " >
# and zhanying = 1
# < / if >
#
# < if test="haiziJiahu != null " >
# and haizi_jiahu & gt;=  # {haiziJiahu}
# < / if >
#
# < if test="tianyu != null " >
# and tianyu & gt;=  # {tianyu}
# < / if >
#
# < if test="junzi != null " >
# and junzi & gt;=  # {junzi}
# < / if >
#
# < if test="jinbi != null " >
# and jinbi & gt;=  # {jinbi}
# < / if >
#
# < if test="yuanbao != null " >
# and yuanbao & gt;=  # {yuanbao}
# < / if >
#
# < if test="dayu != null " >
# and dayu & gt;=  # {dayu}
# < / if >
#
# < if test="qianyang != null " >
# and qianyang = 1
# < / if >
#
# < if test="moyinli != null " >
# and moyinli = 1
# < / if >
#
# < if test="mudanyuan != null " >
# and mudanyuan = 1
# < / if >
#
# < if test="yinglongya != null " >
# and yinglongya = 1
# < / if >
#
# < if test="xuelongya != null " >
# and xuelongya = 1
# < / if >
# < / select >
#
# < select
# id = "findLatestUpdate"
# resultType = "string" >
# select
# max(create_time)
# from cbg_role
# < / select >