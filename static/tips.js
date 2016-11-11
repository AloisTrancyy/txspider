/**
 * Created by funny on 16/11/10.
 */

LOADING = 1;
LOADED = 2;
var tips_panel_prefix = "tips_panel_";
var tips_container_prefix = "tips_container_";
var small_img_prefix = "equip_small_img_";
var loading_img_prefix = "loading_";
function hidden_tips(equipid) {
    $("EquipTipsBox").setStyle("display", "none");
    var tips_el_id = tips_panel_prefix + equipid;
    if ($(tips_el_id))$(tips_el_id).style.display = "none";
    var small_img_id = small_img_prefix + equipid;
    if ($(small_img_id).loading_status == LOADING)$(small_img_id).if_display = false;
}
function create_tips_container_x(id) {
    var fdiv = document.createElement("div");
    fdiv.id = id;
    document.body.appendChild(fdiv);
}
function loading_img_onmouseover(equipid) {
    $(small_img_prefix + equipid).className = "alt";
    if ($(small_img_prefix + equipid).loading_status == LOADING)
        $(small_img_prefix + equipid).if_display = true;
}
function loading_img_onmouseout(equipid) {
    if ($(small_img_prefix + equipid).loading_status == LOADING)
        $(small_img_prefix + equipid).if_display = false;
}
function itemdesc_callback_x(msg) {
    var equipid = msg[0]["position"];
    $(loading_img_prefix + equipid).style.display = "none";
    create_tips_container_x(tips_container_prefix + equipid);
    var div = document.createElement("div");
    div.id = tips_panel_prefix + equipid;
    with (div.style) {
        display = "none";
        zIndex = 10001;
        position = "absolute";
    }
    div.innerHTML = msg[0]["content"];
    $(tips_container_prefix + equipid).appendChild(div);
    if ($(small_img_prefix + equipid).if_display)
        set_flayer_inscreen(last_tips_x, last_tips_y, tips_panel_prefix + equipid);
    $(small_img_prefix + equipid).loading_status = LOADED;
}
function gen_equip_tips_html(equipid, equip_desc) {
    var parser = new EquipDescParser();
    var equip_data = JSON.decode($("formated_equip_desc_" + equipid).value);
    var html = "";
    if (equip_data["name"]) {
        html += '<span class="name" style="color:#' + equip_data["name_color"] + '">' + equip_data["name"] + '</span>';
    }
    if (equip_data["type_name"]) {
        html += '<span class="type_name">' + equip_data["type_name"] + '</span>'
    }
    html += '<p style="line-height:10px;">&nbsp;</p>' + parser.parse(equip_data["content"])
    $("tips_equip_desc").innerHTML = html;
    var img_el = $("equip_small_img_" + equipid);
    adjust_tips_position(img_el, $("EquipTipsBox"))
}
function gen_money_tips_html(equipid, equip_name, client_desc, server_desc, bigimg) {
    var server_desc = js_eval(server_desc);
    var dic = {
        "client_desc": client_desc,
        "server_desc": server_desc,
        "bigimg": bigimg,
        "name": equip_name,
        "equipid": equipid
    };
    create_tips_container_x(tips_container_prefix + equipid);
    render_to_replace(tips_container_prefix + equipid, "money_tips_template", dic);
    $(loading_img_prefix + equipid).style.display = "none";
    $(small_img_prefix + equipid).loading_status = LOADED;
}
function gen_role_tips_html(equipid, server_desc, equip_name) {
    var server_desc = js_eval(server_desc);
    var equip_pos = [15, 0, 19, 16, 8, 20, 17, 1, 21, 18, 9, 2, 5, 22, 13, 10, 4, 14, 3, 7, 6, 11];
    var total_jiahu = 0;
    for (var i = 0; i < equip_pos.length; i++) {
        var p = equip_pos[i];
        if (server_desc['equ'][p] != undefined && server_desc['equ'][p]['cenh'] != undefined)
            total_jiahu += server_desc['equ'][p]['cenh'];
    }
    var dic = {
        "name": equip_name,
        "lv": server_desc.lv,
        "bigimg": ResRoot + "/images/bigface/" + server_desc.sch + "" + server_desc.sex + ".jpg",
        "sch": cbg_setting.school_dict[server_desc.sch],
        "equipid": equipid,
        "xiuwei": server_desc.xiuwei,
        "equ_xiuwei": server_desc.equ_xiuwei,
        "total_jiahu": total_jiahu
    };
    create_tips_container_x(tips_container_prefix + equipid);
    render_to_replace(tips_container_prefix + equipid, "role_tips_template", dic);
    $(loading_img_prefix + equipid).style.display = "none";
    $(small_img_prefix + equipid).loading_status = LOADED;
}
function gen_pet_tips_html(equipid, server_desc, bigimg) {
    var server_desc = js_eval(server_desc);
    var dic = {
        "name": server_desc.real_name,
        "type_name": server_desc.type_name,
        "mstar": server_desc.mstar,
        "lv": server_desc.lv,
        "bigimg": bigimg,
        "equipid": equipid,
        "xiuwei": server_desc.xiuwei,
        "en_lv": server_desc.en_lv
    };
    create_tips_container_x(tips_container_prefix + equipid);
    render_to_replace(tips_container_prefix + equipid, "pet_tips_template", dic);
    $(loading_img_prefix + equipid).style.display = "none";
    $(small_img_prefix + equipid).loading_status = LOADED;
}
function generate_tips(equipid, equip_name, equip_type_desc, equip_face_img, big_img_root, pet_skill_url, storage_type) {
    if ($(small_img_prefix + equipid).loading_status == LOADED) {
        return;
    }
    var equip_desc = $("equip_desc_" + equipid).value.trim();
    $(small_img_prefix + equipid).if_display = true;
    if ($(small_img_prefix + equipid).loading_status == LOADING)
        return;
    if (storage_type == StorageTypeMoney)
        gen_money_tips_html(equipid, equip_name, equip_type_desc, equip_desc, big_img_root + equip_face_img); else if (storage_type == StorageTypeEquip)
        gen_equip_tips_html(equipid, equip_desc); else if (storage_type == StorageTypePet)
        gen_pet_tips_html(equipid, equip_desc, big_img_root + equip_face_img); else if (storage_type == StorageTypeRole)
        gen_role_tips_html(equipid, equip_desc, equip_name);
}
function set_extrainfo(equipid, storage_type) {
    if (storage_type == StorageTypeRole) {
        var role_info = js_eval($("equip_desc_" + equipid).value.trim());
        $("equip_small_img_" + equipid).src = cbg_setting.get_role_smallicon_url(role_info["sch"] + "" + role_info["sex"]);
    }
    else if (storage_type == StorageTypeEquip) {
        try {
            var equip_info = js_eval($("equip_desc_" + equipid).value.trim());
            if (equip_info.cwrap && equip_info.cwrap > 1) {
                $("equip_num_" + equipid).innerHTML = "x " + equip_info.cwrap;
            }
        } catch (SyntaxError) {
            $("equip_num_" + equipid).innerHTML = "x 未知(请联系客服)";
        }
    }
}