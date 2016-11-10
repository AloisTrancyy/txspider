/**
 * Created by funny on 16/11/10.
 */

var EquipColors = {
    'R': 'ff0000',
    'G': '02e802',
    'B': '1d6598',
    'W': 'ffffff',
    'P': 'ffc0cb',
    'K': '000000',
    'Y': 'f8d038',
    'default': '#ffffff',
    'n': '#ffffff'
};
function get_color(equip_desc, idx) {
    var len = 0;
    for (var i = idx; i < idx + 6; i++) {
        var char_item = equip_desc.charAt(i);
        if ((char_item >= 'a' && char_item <= 'z') || (char_item >= 'A' && char_item <= 'Z') || (char_item >= '0' && char_item <= '9')) {
            len = len + 1;
        } else {
            break;
        }
    }
    var color = equip_desc.substring(idx, idx + len);
    for (var i = 0; i < (6 - len); i++) {
        color = "0" + color;
    }
    return {"color": color, "len": len};
}
function re_replace_emote($1) {
    var match_str = $1.substring(1);
    if (match_str.length == 1) {
        match_str = "0" + match_str;
    }
    var emote_path = 'http://res.tx3.netease.com/qt/12/bang/images/baozi/' + match_str + ".gif";
    return "<img src='" + emote_path + "' />";
}
function replace_emote(content) {
    var remote_re = new RegExp("#113|#112|#111|#110|#109|#108|#107|#106|#105|#104|#103|#102|#101|#99|#98|#97|#96|#95|#94|#93|#92|#91|#90|#89|#88|#87|#86|#85|#84|#83|#82|#81|#80|#79|#78|#77|#76|#75|#74|#64|#63|#62|#61|#60|#59|#58|#57|#56|#55|#54|#53|#52|#51|#50|#49|#48|#47|#46|#45|#44|#43|#42|#41|#40|#39|#38|#37|#36|#35|#34|#33|#32|#31|#30|#29|#28|#27|#26|#25|#24|#23|#22|#21|#20|#19|#18|#17|#16|#15|#14|#13|#12|#11|#10|#9|#8|#7|#6|#5|#4|#3|#2|#1|#0", "g");
    return content.replace(remote_re, re_replace_emote);
}
function parse_equip_desc(equip_desc) {
    var result = []
    var line_list = equip_desc.split("#r");
    for (var i = 0; i < line_list.length; i++) {
        var line = line_list[i].trim();
        if (line.length == 0) {
            continue;
        }
        var part_list = [];
        var item_list = line.split("#");
        for (var j = 0; j < item_list.length; j++) {
            var part = item_list[j];
            var op = part.charAt(0);
            var part_info = "";
            if (EquipColors[op]) {
                var color = EquipColors[op];
                part_info = '<span style="color:#' + color + '">' + part.substring(1) + '</span>';
            } else if (op == 'c') {
                var color_info = get_color(part, 1);
                if (color_info["len"] == 0) {
                    part_info = part;
                } else {
                    var color = color_info["color"];
                    var left_content = part.substr(color_info["len"] + 1).replace(' ', '　');
                    part_info = '<span style="color:#' + color + '">' + left_content + '</span>';
                }
            } else {
                part_info = part;
            }
            part_list.push(part_info);
        }
        result.push("<p>" + part_list.join("") + "</p>");
    }
    return result.join("");
}
function show_role_tips_box(event) {
    var el = $(this);
    show_tips(event.event, el.getAttribute("data_tips_box"), 10);
}
function hidden_role_tips_box() {
    var el = $(this);
    $(el.getAttribute("data_tips_box")).setStyle("display", "none");
}
var RoleInfoParser = new Class({
    initialize: function (role_desc) {
        this.raw_info = js_eval(role_desc);
        this.conf = cbg_setting;
        this.result = {};
    }, run: function () {
        this.parse_basic_role_info();
        this.parse_skill();
        this.parse_equip_info();
        this.parse_rider_info();
        this.parse_pet_info();
        this.parse_child_info();
        this.parse_ying_hun_info();
        this.parse_awakening();
        if (this.raw_info["famousWing"]) {
            var formated_data = get_formated_role_data();
            this.result["famous_wing_id"] = formated_data["famous_wing_id"];
        }
        return this.result;
    }, parse_awakening: function () {
        if (!this.raw_info["final_skill"]) {
            this.result["final_skill"] = null;
            return;
        }
        var final_skill = this.raw_info["final_skill"];
        final_skill["name"] = this.safe_attr(this.conf.awakening_skill_dict[final_skill.fsId]);
        final_skill["icon"] = this.conf.get_awakening_skill_icon(final_skill.fsId);
        for (var i = 0; i < final_skill["subSkills"].length; i++) {
            var subSkill = final_skill["subSkills"][i];
            subSkill["name"] = this.safe_attr(this.conf.awakening_sub_skill_dict[subSkill.libId]);
            subSkill["icon"] = this.conf.get_awakening_sub_skill_icon(subSkill.libId);
        }
        this.result["final_skill"] = final_skill;
    }, parse_ying_hun_info: function () {
        if (!this.raw_info["multiMS"]) {
            this.result["ying_hun_list"] = [];
            return;
        }
        this.result["ying_hun_list"] = this.raw_info["multiMS"];
    }, safe_attr: function (attr_value) {
        if (attr_value == undefined || attr_value == null) {
            return "未知";
        }
        return attr_value;
    }, get_total_jiahu: function () {
        var total_jiahu = 0;
        var equip_pos = [15, 0, 19, 16, 8, 20, 17, 1, 21, 18, 9, 2, 5, 22, 13, 10, 4, 14, 3, 7, 6, 11];
        for (var i = 0; i < equip_pos.length; i++) {
            var pos = equip_pos[i];
            if (this.raw_info['equ'][pos] != undefined && this.raw_info['equ'][pos]['cenh'] != undefined)
                total_jiahu += this.raw_info['equ'][pos]['cenh'];
        }
        return total_jiahu;
    }, get_wing_style: function () {
        var total_jiahu = this.get_total_jiahu();
        if (total_jiahu == 360) {
            return 20;
        } else if (total_jiahu >= 324 && total_jiahu < 360) {
            return 18;
        } else if (total_jiahu >= 288 && total_jiahu < 324) {
            return 16;
        } else if (total_jiahu >= 234 && total_jiahu <= 288) {
            return 13;
        } else if (total_jiahu >= 144 && total_jiahu <= 234) {
            return 8;
        } else if (total_jiahu < 144) {
            return 0;
        }
        return -1;
    }, get_wing_name_by_jiahu: function () {
        var wing_level = 0;
        var total_jiahu = this.get_total_jiahu();
        if (total_jiahu == 360) {
            wing_level = 6;
        } else if (total_jiahu >= 324 && total_jiahu < 360) {
            wing_level = 5;
        } else if (total_jiahu >= 288 && total_jiahu < 324) {
            wing_level = 4;
        } else if (total_jiahu >= 234 && total_jiahu < 288) {
            wing_level = 3;
        } else if (total_jiahu >= 180 && total_jiahu < 234) {
            wing_level = 2;
        } else if (total_jiahu >= 144 && total_jiahu < 180) {
            wing_level = 1;
        } else {
        }
        var wing_name = this.conf.wing_name[wing_level];
        if (wing_name) {
            return wing_name;
        } else {
            return "";
        }
    }, show_wing: function () {
        if (this.raw_info["wing_inlay_prop"] == undefined) {
            $("wing_img").destroy();
            return;
        }
        var wing = this.get_wing_style();
        if (wing == 0) {
            $("wing_img").destroy();
            return;
        }
        var wing_name = "";
        if (this.raw_info["double_wing_enable_attr"]) {
            var wing_type = this.raw_info["double_wing_lv"] % 10;
            var img_url = ResRoot + "/images/double_wing/" + wing_type + ".gif";
            $("wing_img").src = img_url;
            wing_name = this.conf.double_wing_name[this.raw_info["double_wing_lv"]];
        } else {
            $("wing_img").src = this.conf.get_wing_img(wing);
            if (this.raw_info["enh_wing_lv"]) {
                wing_name = this.conf.wing_name[this.raw_info["enh_wing_lv"]];
            } else {
                wing_name = this.get_wing_name_by_jiahu();
            }
        }
        if (!this.raw_info['wing_inlay_prop']) {
            return;
        }
        var tips_box_id = "wing_tips_box";
        var el = new Element("div", {"id": tips_box_id})
        el.setStyles({"display": "none", "position": "absolute", "zIndex": 10001});
        el.inject($(document.body));
        var html = "";
        if (wing_name) {
            html += '<span class="name" style="color:#FFFF00">' + wing_name + '</span>';
            html += '<span class="type_name">通溟</span><p style="line-height:10px;">&nbsp;</p>';
        }
        var formated_data = get_formated_role_data();
        if (this.raw_info["double_wing_enable_attr"]) {
            if (formated_data["double_wing_enhance_tips"]) {
                html += parse_equip_desc(formated_data["double_wing_enhance_tips"] + "#r#r");
            }
        } else {
            if (formated_data["wing_tips"]) {
                html += parse_equip_desc(formated_data["wing_tips"] + "#r#r");
            }
        }
        html += parse_equip_desc(this.raw_info["wing_inlay_prop"]);
        el.set("html", '<div class="detail eDesc">' + html + "</div>");
        $("wing_img").setAttribute("data_tips_box", tips_box_id);
        $("wing_img").addEvent("mouseover", show_role_tips_box);
        $("wing_img").addEvent("mouseout", hidden_role_tips_box);
    }, parse_basic_role_info: function () {
        var lifeskill = [];
        for (var each in this.raw_info["ssks"]) {
            lifeskill.push(this.safe_attr(this.conf.lifeskill_dict[each]) + " " + this.raw_info["ssks"][each] + "级");
        }
        var baseinfo = [["生命值", this.raw_info["mhp"]], ["技力值", this.raw_info["msp"]], ["力", this.raw_info["attr"]["str"]], ["体", this.raw_info["attr"]["con"]], ["敏", this.raw_info["attr"]["dex"]], ["当前经验", this.raw_info["exp"]], ["潜能", this.raw_info["ap"]], ["疾", this.raw_info["attr"]["dog"]], ["魂", this.raw_info["attr"]["int"]], ["念", this.raw_info["attr"]["mind"]]];
        var attinfo = [["攻击力", this.raw_info["pattack_min"] + "-" + this.raw_info["pattack_max"]], ["命中", this.raw_info["hit"]], ["法力", this.raw_info["mattack_min"] + "-" + this.raw_info["mattack_max"]], ["重击", this.raw_info["modadd"]], ["会心", this.raw_info["critical"]], ["附伤", this.raw_info["attadd"]]];
        var definfo = [["防御", this.raw_info["pdef"]], ["回避", this.raw_info["avoid"]], ["法防", this.raw_info["mdef"]], ["神明", this.raw_info["inprotect"]], ["化解", this.raw_info["attdef"]], ["知彼", parseInt(this.raw_info["defhuman"])]];
        var advinfo = [["追电", this.raw_info["movespeed"]], ["骤雨", this.raw_info["attackspeed"]], ["疾语", this.raw_info["castspeed"]], ["明思", this.raw_info["spreduce"]], ["扰心", this.raw_info["inbreak"]], ["人祸", this.raw_info["attackhuman"]]];
        var kanginfo = [["身法", this.raw_info["sract"]], ["坚韧", this.raw_info["srbody"]], ["定力", this.raw_info["srmind"]]];
        if (this.raw_info["cri_add_p"] != undefined) {
            kanginfo.push(["诛心", this.raw_info["cri_add_p"]]);
            kanginfo.push(["御心", this.raw_info["cri_sub_p"]]);
            kanginfo.push(["万钧", this.raw_info["thump_add_p"]]);
            kanginfo.push(["铁壁", this.raw_info["thump_sub_p"]]);
        }
        var zhenwu_info = [];
        if (this.raw_info["absolutely_attack"] != undefined) {
            zhenwu_info.push(["破阵", this.raw_info["absolutely_attack"]]);
            zhenwu_info.push(["磐石", this.raw_info["absolutely_defence"]]);
        }
        var creditinfo = [];
        for (var id in this.raw_info["credit"]) {
            creditinfo.push([this.safe_attr(this.conf.credit_dict[id]), this.raw_info["credit"][id]]);
        }
        var toGoldDesc = function (_cop) {
            var cop = parseInt(_cop);
            if (cop + "" != _cop)
                return _cop;
            if (cop == 0)
                return "0铜";
            var gold = parseInt(cop / 10000);
            var rest = cop % 10000;
            var silver = parseInt(rest / 100);
            var copper = rest % 100;
            var desc = "";
            if (gold != 0)
                desc += gold + "金";
            if (silver != 0)
                desc += silver + "银";
            if (copper != 0)
                desc += copper + "铜";
            return desc;
        };
        var otherinfo = {};
        if (this.raw_info["coinA"] != undefined) {
            otherinfo["yuan_bao"] = this.raw_info["coinA"];
        } else {
            otherinfo["yuan_bao"] = this.raw_info["coin"];
        }
        otherinfo["jun_xiang"] = this.safe_attr(this.raw_info["coinB"]);
        ;
        otherinfo["cash"] = toGoldDesc(this.raw_info["cash"]);
        otherinfo["talent_point"] = this.safe_attr(this.raw_info["talent_point"]);
        otherinfo["fly_soul_lv"] = this.safe_attr(this.raw_info["fly_soul_lv"]);
        var fly_soul_phase = "";
        if (this.raw_info["fly_soul_phase"] == 1) {
            fly_soul_phase = "【地魂】";
        } else if (this.raw_info["fly_soul_phase"] == 2) {
            fly_soul_phase = "【天魂】";
        } else {
        }
        otherinfo["fly_soul_lv"] = fly_soul_phase + otherinfo["fly_soul_lv"];
        var migrate_time = undefined;
        if (this.raw_info["migrate_time"] != undefined && this.raw_info["migrate_time"] != 0) {
            migrate_time = format_datetime(new Date(this.raw_info["migrate_time"] * 1000));
        }
        var cheng_wei_re = /^(\$T)/;
        if (cheng_wei_re.test(this.raw_info["petName"])) {
            var cheng_wei = "";
        } else {
            var cheng_wei = this.raw_info["petName"];
        }
        var role_info = {
            "dengji": this.raw_info["lv"],
            "menpai": this.safe_attr(this.conf.school_dict[this.raw_info["sch"]]),
            "chengwei": cheng_wei,
            "shenghuojineng": lifeskill.join("，"),
            "qishu": this.safe_attr(this.conf.riderskill_dict[this.raw_info["ride_skill"]]),
            "hunyin": this.raw_info["coupleName"] ? this.raw_info["coupleName"] : "未婚",
            "shili": this.raw_info["clanName"] ? this.raw_info["clanName"] : "无",
            "xingbie": this.raw_info["sex"] == 1 ? "男" : "女",
            "xiuwei": this.raw_info["xiuwei"],
            "zhuangbeixiuwei": this.raw_info["equ_xiuwei"],
            "icon": this.raw_info["sch"] + "" + this.raw_info["sex"],
            "baseinfo": baseinfo,
            "attinfo": attinfo,
            "definfo": definfo,
            "advinfo": advinfo,
            "kanginfo": kanginfo,
            "zhenwu_info": zhenwu_info,
            "creditinfo": creditinfo,
            "otherinfo": otherinfo,
            "migrate_time": migrate_time
        };
        this.result["basic_info"] = role_info;
    }, parse_skill: function () {
        var common_skill = [];
        var tmpdict = {};
        var i = 0;
        for (var id in this.raw_info["sg"]) {
            var s = {
                "skilltype_name": this.safe_attr(this.conf.skilltype_dict[id]),
                "level": this.raw_info["sg"][id],
                "skills": []
            };
            common_skill.push(s);
            tmpdict[id] = i;
            i++;
        }
        var skilltype = ss = null;
        for (var i = 0; i < this.raw_info["rsks"].length; i++) {
            var id = this.raw_info["rsks"][i][0];
            skilltype = this.conf.get_skilltype_by_skill(id);
            if (skilltype == null) {
                continue;
            }
            ss = [id, this.safe_attr(this.conf.roleskill_dict[id]), this.raw_info["rsks"][i][1]];
            common_skill[tmpdict[skilltype]]["skills"].push(ss);
        }
        var special_skill = [];
        var tmparray = [];
        for (var id in this.raw_info["lightSkills"])
            tmparray.push(parseInt(id, 10));
        tmparray = quick_sort(tmparray);
        for (var i = 0; i < tmparray.length; i++) {
            var id = tmparray[i];
            special_skill.push([id, this.safe_attr(this.conf.lightskill_dict[id]), this.raw_info["lightSkills"][id]]);
        }
        var fly_soul_skill = [];
        var fly_skill_id_list = [];
        if (this.raw_info["fly_soul_skill"] != undefined) {
            fly_skill_id_list = Object.keys(this.raw_info["fly_soul_skill"]).sort();
        }
        for (var i = 0; i < fly_skill_id_list.length; i++) {
            var skill_id = fly_skill_id_list[i];
            var item = this.raw_info["fly_soul_skill"][skill_id];
            fly_soul_skill.push({"id": skill_id, "name": this.conf.all_skill_info[skill_id], "level": item[0]});
        }
        this.result["skill"] = {
            "common_skill": common_skill,
            "special_skill": special_skill,
            "wuxing": this.raw_info["wuxing"],
            "shengyudian": this.raw_info["skp"],
            "fly_soul_skill": fly_soul_skill,
            "school_qinggong": this.raw_info["school_qinggong"]
        };
    }, parse_equip_info: function () {
        this.result["equips"] = this.raw_info["equ"];
        this.result["items"] = this.raw_info["inv"];
        this.result["clothes"] = this.raw_info["commode"];
        this.result["riders_info"] = this.raw_info["saddle"];
    }, parse_pet_info: function () {
        var monster_souls = [];
        var tmparray = [];
        for (var pos in this.raw_info["monster_souls"]) {
            tmparray.push(parseInt(pos, 10));
        }
        tmparray = quick_sort(tmparray);
        for (var i = 0; i < tmparray.length; i++) {
            var dotpos = this.raw_info["monster_souls"][tmparray[i] + ""]["real_name"].indexOf("·");
            if (-1 != dotpos)
                this.raw_info["monster_souls"][tmparray[i] + ""]["real_name"] = this.raw_info["monster_souls"][tmparray[i] + ""]["real_name"].substr(dotpos + 1);
            monster_souls.push(this.raw_info["monster_souls"][tmparray[i] + ""]);
        }
        this.result["monster_souls"] = monster_souls;
    }, parse_child_info: function () {
        this.result['childs'] = this.raw_info['new_childs'];
        if (this.result['childs'] === undefined)
            return;
        for (var i = 0; i < this.result['childs'].length; i++) {
            this.result['childs'][i]['school_name'] = this.conf.school_dict[this.result['childs'][i]['sch']];
        }
    }, parse_rider_info: function () {
        var hbs = [];
        var tmparray = [];
        for (var pos in this.raw_info["hbs"]) {
            tmparray.push(parseInt(pos, 10));
        }
        tmparray = quick_sort(tmparray);
        daxie = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
        for (var i = 0; i < tmparray.length; i++) {
            var cid = tmparray[i] + "";
            this.raw_info["hbs"][cid]["pos"] = tmparray[i];
            this.raw_info["hbs"][cid]["real_name"] = this.safe_attr(this.conf.hbs_dict[this.raw_info["hbs"][cid]["hb_type"]]);
            fly_level = this.raw_info["hbs"][cid]["fly_lv"];
            if (fly_level > 0 && fly_level < 37) {
                day = daxie[Math.floor((fly_level + 8) / 9)];
                jinjie = daxie[((fly_level - 1) % 9) + 1];
                this.raw_info["hbs"][cid]["fly_soul_lv"] = day + '天' + jinjie + '境界';
            }
            if (this.raw_info["hbs"][cid]["hb_equ"] != undefined) {
                for (var j = 0; j < this.raw_info["hbs"][cid]["hb_equ"].length; j++) {
                    if (this.raw_info["hbs"][cid]["hb_equ"][j] == null) {
                        this.raw_info["hbs"][cid]["hb_equ"][j] = {};
                    }
                }
            }
            hbs.push(this.raw_info["hbs"][cid]);
        }
        this.result["hbs"] = hbs;
    }
});
function create_equip_cell(equip_data, pos) {
    if (!equip_data) {
        return "&nbsp;";
    }
    var img_url = get_equip_img_url(equip_data);
    return "<img width='32' height='32' class='equipItem' src='" + img_url + "' data_pos='" + pos + "' />";
}
function get_equip_img_url(equip_data) {
    if (equip_data["real_id"]) {
        return cbg_setting.get_equip_img_url(equip_data["real_id"]);
    } else {
        return cbg_setting.get_equip_img_url(equip_data["id"]);
    }
}
function create_child_equip_cell(child_idx, pos) {
    var equip_data = role_parser.result.childs[child_idx]["equs"][pos];
    if (!equip_data) {
        return "&nbsp;";
    }
    var img_url = get_equip_img_url(equip_data);
    return "<img width='32' height='32' class='equipItem' src='" + img_url + "' data_pos='" + pos + "' data_child_idx='" + child_idx + "' />";
}
function create_child_cloth_cell(child_idx, pos) {
    var equip_data = role_parser.result.childs[child_idx]["fashion"][pos];
    if (!equip_data) {
        return "&nbsp;";
    }
    var data_pos = 100 + pos.toInt();
    var img_url = cbg_setting.get_equip_img_url(equip_data["id"]);
    return "<img width='32' height='32' class='equipItem' src='" + img_url + "' data_pos='" + data_pos + "' data_child_idx='" + child_idx + "' />";
}
function create_using_equip_cell(pos) {
    var equip_data = role_parser.result.equips[pos];
    return create_equip_cell(equip_data, pos);
}
var FormatedRoleData = null;
function get_formated_role_data() {
    if (!FormatedRoleData) {
        FormatedRoleData = JSON.decode($("formated_role_desc").value.trim());
    }
    return FormatedRoleData;
}
function show_equip_tips(el, equip_data) {
    var parser = new EquipDescParser();
    var html = "";
    if (equip_data["name"]) {
        html += '<span class="name" style="color:#' + equip_data["name_color"] + '">' + equip_data["name"] + '</span>';
    }
    if (equip_data["type_name"]) {
        html += '<span class="type_name">' + equip_data["type_name"] + '</span>'
    }
    html += '<p style="line-height:10px;">&nbsp;</p>' + parser.parse(equip_data["content"])
    $("tips_equip_desc").innerHTML = html;
    adjust_tips_position(el, $("EquipTipsBox"))
}
function hidden_equip_tips() {
    $("EquipTipsBox").setStyle("display", "none");
}
function show_using_equip_tips() {
    var el = $(this);
    var pos = $(this).getAttribute("data_pos").toInt();
    var formated_data = get_formated_role_data();
    var formated_info = formated_data["using_equips"][pos];
    show_equip_tips(el, formated_info);
}
function show_store_equip_tips() {
    var el = $(this);
    var pos = $(this).getAttribute("data_pos").toInt();
    var formated_data = get_formated_role_data();
    var formated_info = formated_data["store_equips"][pos];
    show_equip_tips(el, formated_info);
}
function show_clothes_tips() {
    var el = $(this);
    var pos = $(this).getAttribute("data_pos").toInt();
    var formated_data = get_formated_role_data();
    var formated_info = formated_data["clothes_info"][pos];
    show_equip_tips(el, formated_info);
}
function show_rider_tips() {
    var el = $(this);
    var pos = $(this).getAttribute("data_typeid").toInt();
    var formated_data = get_formated_role_data();
    var formated_info = formated_data["rider_info"][pos];
    if (role_parser.raw_info["saddle_tips"]) {
        formated_info["content"] = role_parser.raw_info["saddle_tips"][pos];
    }
    show_equip_tips(el, formated_info);
}
function add_role_equip_tips_ev() {
    var using_equips = $$("#RoleUsingEquips .equipItem");
    for (var i = 0; i < using_equips.length; i++) {
        var el = using_equips[i];
        el.addEvent("mouseover", show_using_equip_tips);
        el.addEvent("mouseout", hidden_equip_tips);
    }
    var using_equips = $$("#RoleStoreEquips .equipItem");
    for (var i = 0; i < using_equips.length; i++) {
        var el = using_equips[i];
        el.addEvent("mouseover", show_store_equip_tips);
        el.addEvent("mouseout", hidden_equip_tips);
    }
}
function add_role_clothes_tips_ev() {
    var clothes_list = $$("#RoleClothes .equipItem");
    for (var i = 0; i < clothes_list.length; i++) {
        var el = clothes_list[i];
        el.addEvent("mouseover", show_clothes_tips);
        el.addEvent("mouseout", hidden_equip_tips);
    }
}
function add_role_rider_tips_ev() {
    var clothes_list = $$("#RoleRiders .equipItem");
    for (var i = 0; i < clothes_list.length; i++) {
        var el = clothes_list[i];
        el.addEvent("mouseover", show_rider_tips);
        el.addEvent("mouseout", hidden_equip_tips);
    }
}
function show_hb_star_tips() {
    var el = $(this);
    var pos = el.getAttribute("data_pos").toInt();
    var data_hb_num = el.getAttribute("data_hb_num").toInt();
    var data_hb_pos = el.getAttribute("data_hb_pos").toInt();
    var formated_data = get_formated_role_data();
    var star_info = formated_data["hb_info"][data_hb_pos][pos];
    var hb_lv = role_parser.result.hbs[data_hb_num]["lv"];
    if (star_info["is_empty"]) {
        if (hb_lv < star_info["req_lv"]) {
            star_info["content"] = "#R" + star_info["req_lv"] + "级开启此星点"
        } else {
            star_info["content"] = "#R已开启星点，需要灵化。"
        }
    }
    show_equip_tips(el, star_info);
}
function add_hb_star_tips_ev() {
    var star_list = $$(".HbStarInfo .hb_star_point");
    for (var i = 0; i < star_list.length; i++) {
        var el = star_list[i];
        el.addEvent("mouseover", show_hb_star_tips);
        el.addEvent("mouseout", hidden_equip_tips);
    }
}
function show_child_equip_tips() {
    var el = $(this);
    var pos = el.getAttribute("data_pos");
    var data_child_idx = el.getAttribute("data_child_idx").toInt();
    var formated_data = get_formated_role_data();
    var equip_info = formated_data["child_info"][data_child_idx]["equip_list"][pos];
    show_equip_tips(el, equip_info);
}
function add_child_equip_tips_ev() {
    var equip_list = $$(".childEquip .equipItem");
    for (var i = 0; i < equip_list.length; i++) {
        var el = equip_list[i];
        el.addEvent("mouseover", show_child_equip_tips);
        el.addEvent("mouseout", hidden_equip_tips);
    }
}
function show_ying_hun_teji_tips() {
    var el = $(this);
    var ying_hun_idx = el.getAttribute("data_ying_hun_idx").toInt();
    var formated_data = get_formated_role_data();
    var teji_desc = formated_data["ying_hun_teji_tips"][ying_hun_idx];
    if (teji_desc.length == 0) {
        return;
    }
    show_equip_tips(el, {"content": teji_desc});
}
function show_ying_hun_equip_tips() {
    var el = $(this);
    var ying_hun_idx = el.getAttribute("data_ying_hun_idx").toInt();
    var idx = el.getAttribute("data_idx").toInt();
    var formated_data = get_formated_role_data();
    var tips = formated_data["ying_hun_equip_tips"][ying_hun_idx][idx];
    if (tips.length == 0) {
        return;
    }
    show_equip_tips(el, {"content": tips});
}
function get_hb_combined_info() {
    var formated_data = get_formated_role_data();
    if (formated_data["hb_combined"]) {
        var parser = new EquipDescParser();
        return parser.parse(formated_data["hb_combined"]);
    } else {
        return "";
    }
}
function get_rider_expire_time(timestamp) {
    var dt = new Date(timestamp * 1000);
    var dt_desc = dt.getFullYear() + "年" + (dt.getMonth() + 1) + "月" + dt.getDate() + "日";
    dt_desc += "&nbsp;" + dt.getHours() + "点" + dt.getMinutes() + "分";
    dt_desc += dt.getSeconds() + "秒";
    return dt_desc;
}
function get_total_pages(page_num, total_num, num_per_page) {
    if (total_num <= 0) {
        return 0;
    }
    if ((total_num % num_per_page) == 0) {
        return parseInt(total_num / num_per_page);
    } else {
        return parseInt(total_num / num_per_page) + 1;
    }
}
function show_rider_of_page(page_num) {
    if (!role_parser.result.riders_info) {
        return;
    }
    var ctx = {"rider_info": role_parser.result.riders_info, "page_num": page_num, "conf": role_parser.conf};
    render_to_replace("RoleRidersPanel", "rider_list_templ", ctx);
    add_role_rider_tips_ev();
}
var PSkillType = 1;
var NormalSkillType = 2;
function get_skill_img_url(skill_id, skill_type) {
    if (skill_type == PSkillType) {
        var img_subdir = "pskill";
    } else {
        var img_subdir = "skill";
    }
    return ResRoot + "/images/" + img_subdir + "/" + skill_id + ".jpg";
}
function get_skill_name(skill_id, skill_type) {
    if (skill_type == PSkillType) {
        return PSkillInfo[skill_id]["name"];
    } else {
        return SkillInfo[skill_id]["name"];
    }
}
function parse_time_info(time_str) {
    return new Date(Date.parse(time_str.replace(/-/g, '/')));
}
function display_xuan_xiu_change_info() {
    if (EquipInfo && EquipInfo["create_time"] && $("xuan_xiu_addon_error")) {
        var create_time = parse_time_info(EquipInfo['create_time']);
        var start_time = new Date(2015, 10, 25, 8, 0, 0);
        var end_time = new Date(2015, 11, 2, 8, 0, 0);
        if (create_time >= start_time && create_time < end_time) {
            $("xuan_xiu_addon_error").setStyle("display", "");
        }
    }
}
function content_tab_click(num, len, tab_prefix, content_prefix) {
    for (var i = 0; i < len; i++) {
        $(content_prefix + i).style.display = "none";
        $(tab_prefix + i).className = "";
    }
    $(content_prefix + num).style.display = "";
    $(tab_prefix + num).className = "current";
}
var ShowRoleDetail = new Class({
    initialize: function () {
        this.role_parser = new RoleInfoParser($("role_desc").value);
        this.role_parser.run();
        this.last_tab = null;
        this.reg_tab_ev();
    }, adjust_frame_height: function () {
        if (window.self != window.top) {
            reset_iframe();
        }
    }, reg_tab_ev: function () {
        var self_obj = this;
        $("menu_role_basic").addEvent("click", function () {
            self_obj.show_basic();
            self_obj.adjust_frame_height();
            return false;
        });
        $("menu_role_data").addEvent("click", function () {
            self_obj.show_role_data();
            self_obj.adjust_frame_height();
            return false;
        });
        $("menu_role_skill").addEvent("click", function () {
            self_obj.show_role_skill();
            self_obj.adjust_frame_height();
            return false;
        });
        $("menu_role_equip").addEvent("click", function () {
            self_obj.show_role_equip();
            self_obj.adjust_frame_height();
            return false;
        });
        $("menu_role_rider").addEvent("click", function () {
            self_obj.show_role_rider();
            self_obj.adjust_frame_height();
            return false;
        });
        $("menu_role_ling_shou").addEvent("click", function () {
            self_obj.show_role_ling_shou();
            self_obj.adjust_frame_height();
            return false;
        });
        $("menu_role_pet").addEvent("click", function () {
            self_obj.show_role_pet();
            self_obj.adjust_frame_height();
            return false;
        });
        $("menu_role_child").addEvent("click", function () {
            self_obj.show_role_child();
            self_obj.adjust_frame_height();
            return false;
        });
        $("menu_role_awakening").addEvent("click", function () {
            self_obj.show_role_awakening();
            self_obj.adjust_frame_height();
            return false;
        });
        $("menu_role_ying_hun").addEvent("click", function () {
            self_obj.show_role_ying_hun();
            self_obj.adjust_frame_height();
            return false;
        });
    }, switch_tab: function (el) {
        if (this.last_tab) {
            this.last_tab.removeClass("current");
        }
        this.last_tab = el.getParent();
        el.getParent().addClass("current");
        display_xuan_xiu_change_info();
    }, show_basic: function () {
        this.switch_tab($("menu_role_basic"));
        render_to_replace("role_content_panel", "role_basic_templ", this.role_parser);
    }, show_role_data: function () {
        this.switch_tab($("menu_role_data"));
        render_to_replace("role_content_panel", "role_data_templ", this.role_parser);
    }, show_role_skill: function () {
        this.switch_tab($("menu_role_skill"));
        render_to_replace("role_content_panel", "role_skill_templ", this.role_parser);
    }, show_role_equip: function () {
        this.switch_tab($("menu_role_equip"));
        render_to_replace("role_content_panel", "role_equip_templ", this.role_parser);
        this.role_parser.show_wing();
        add_role_equip_tips_ev();
        if ($("famous_wing_el")) {
            $("role_equip_box").addClass("equipBoxBgWithWing");
            var famous_wing_img = ResRoot + "/images/famous_wing/" + this.role_parser.result.famous_wing_id + ".jpg";
            $("famous_wing_img").src = famous_wing_img;
            $("famous_wing_el").addEvent("mouseover", function () {
                adjust_tips_position($("famous_wing_el"), $("famous_wing_box"));
            });
            $("famous_wing_el").addEvent("mouseout", function () {
                $("famous_wing_box").setStyle("display", "none");
            });
        } else {
            $("role_equip_box").addClass("equipBoxBg");
        }
        $$("#UsingColthesMenu li").addEvent("click", function () {
            $$("#UsingColthesMenu li").removeClass("on");
            $(this).addClass("on");
            var item_ids = $(this).getAttribute("data_ids").split(",");
            $("using_clothes_hat").set("html", create_using_equip_cell(parseInt(item_ids[0])));
            $("using_clothes_body").set("html", create_using_equip_cell(parseInt(item_ids[1])));
            $("using_clothes_halo").set("html", create_using_equip_cell(parseInt(item_ids[2])));
            var item_list = [$$("#using_clothes_hat img")[0], $$("#using_clothes_body img")[0], $$("#using_clothes_halo img")[0]];
            for (var i = 0; i < item_list.length; i++) {
                var el = item_list[i];
                if (!el) {
                    continue;
                }
                el.addEvent("mouseover", show_using_equip_tips);
                el.addEvent("mouseout", hidden_equip_tips);
            }
        });
        $$("#UsingColthesMenu li")[0].fireEvent("click");
    }, show_role_rider: function () {
        this.switch_tab($("menu_role_rider"));
        render_to_replace("role_content_panel", "role_rider_templ", this.role_parser);
        if (is_obj_empty(role_parser.result.equips)) {
            return;
        }
        add_role_clothes_tips_ev();
        show_rider_of_page(1);
    }, show_role_ling_shou: function () {
        this.switch_tab($("menu_role_ling_shou"));
        render_to_replace("role_content_panel", "role_ling_shou_templ", this.role_parser);
        add_hb_star_tips_ev();
    }, show_role_pet: function () {
        this.switch_tab($("menu_role_pet"));
        render_to_replace("role_content_panel", "role_pet_templ", this.role_parser);
    }, show_role_child: function () {
        this.switch_tab($("menu_role_child"));
        render_to_replace("role_content_panel", "role_child_templ", this.role_parser);
        add_child_equip_tips_ev();
        if (is_obj_empty(role_parser.result.childs)) {
            return;
        }
        if (!is_obj_empty(role_parser.result.childs[0]['fashion'])) {
            var cb = function (msg) {
                var pos = null;
                for (var j = 0; j < msg.length; j++) {
                    pos = msg[j]["position"];
                    create_tips_container(child_fashion_tips_container_prefix + '0' + '_' + pos).innerHTML = msg[j]["content"];
                }
            };
        }
    }, show_role_awakening: function () {
        this.switch_tab($("menu_role_awakening"));
        render_to_replace("role_content_panel", "role_awakening_templ", this.role_parser);
    }, show_role_ying_hun: function () {
        this.switch_tab($("menu_role_ying_hun"));
        render_to_replace("role_content_panel", "role_ying_hun_templ", this.role_parser);
        var self_obj = this;
        $$("#ying_hun_box a").addEvent("click", function () {
            $$("#ying_hun_box li").removeClass("current");
            var el = $(this);
            el.getParent().addClass("current");
            var idx = parseInt(el.getAttribute("data_idx"));
            var ying_hun = self_obj.role_parser.result["ying_hun_list"][idx];
            render_to_replace("ying_hun_detail_panel", "role_ying_hun_item_temp", {
                "ying_hun": ying_hun,
                "ying_hun_idx": idx
            });
            var hide_all = function () {
                $("ying_hun_basic_info").setStyle("display", "none");
                $("ying_hun_skill_info").setStyle("display", "none");
                $("ying_hun_equip_info").setStyle("display", "none");
            };
            $("menu_ying_hun_basic").addEvent("click", function () {
                $$("#ying_hun_menu_box td").removeClass("on");
                var el = $(this);
                el.addClass("on");
                hide_all();
                $("ying_hun_basic_info").setStyle("display", "");
            });
            $("menu_ying_hun_skill").addEvent("click", function () {
                $$("#ying_hun_menu_box td").removeClass("on");
                var el = $(this);
                el.addClass("on");
                hide_all();
                $("ying_hun_skill_info").setStyle("display", "");
                var bg_cls = BG_IMG_CLS[ying_hun["index"]];
                var ctx = {"tree_id": 1, "ying_hun": ying_hun};
                render_to_replace("ying_hun_skill_faqi", "ying_hun_skill_cell_templ", ctx);
                $("yh_faqi_skill_box").addClass(bg_cls);
                ctx["tree_id"] = 2;
                render_to_replace("ying_hun_skill_canyu", "ying_hun_skill_cell_templ", ctx);
                $("yh_canyu_skill_box").addClass(bg_cls);
                ctx["tree_id"] = 3;
                var skill_cells = cbg_setting.ying_hun_tree[ying_hun["index"]][ctx["tree_id"]];
                if (skill_cells == undefined) {
                    $("yh_pet_skill_box").setStyle("display", "none");
                    $("yh_pet_skill_box_title").setStyle("display", "none");
                } else {
                    render_to_replace("ying_hun_skill_pet", "ying_hun_skill_cell_templ", ctx);
                    $("yh_pet_skill_box").addClass(bg_cls);
                }
            });
            $("menu_ying_hun_equip").addEvent("click", function () {
                $$("#ying_hun_menu_box td").removeClass("on");
                var el = $(this);
                el.addClass("on");
                hide_all();
                $("ying_hun_equip_info").setStyle("display", "");
                if ($("ying_hun_teji_item")) {
                    $("ying_hun_teji_item").addEvent("mouseover", show_ying_hun_teji_tips);
                    $("ying_hun_teji_item").addEvent("mouseout", hidden_equip_tips);
                }
                var equip_list = $$(".ying_hun_equip_item");
                for (var i = 0; i < equip_list.length; i++) {
                    var el = equip_list[i];
                    el.addEvent("mouseover", show_ying_hun_equip_tips);
                    el.addEvent("mouseout", hidden_equip_tips);
                }
            });
            $("menu_ying_hun_basic").fireEvent("click");
            return false;
        });
        if ($$("#ying_hun_box a").length > 0) {
            $$("#ying_hun_box a")[0].fireEvent("click");
        }
    }
});
function get_skill_img(skill_id, is_pskill) {
    if (is_pskill) {
        var sub_dir = "pskill";
    } else {
        var sub_dir = "skill";
    }
    return ResRoot + "/images/" + sub_dir + "/" + skill_id + ".jpg";
}
function get_ying_hun_equip_url(idx, equipid) {
    var img_name = idx + "_" + equipid + ".png";
    return ResRoot + "/images/equip_img/" + img_name;
}
var HUMAN_NUM = {1: "一", 2: "二", 3: "三"};
var BG_IMG_CLS = {2: "sC-bg", 4: "sC-bg sC-bg_2", 3: "sC-bg sC-bg_3", 1: "sC-bg sC-bg_4"};