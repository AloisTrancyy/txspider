/**
 * Created by funny on 16/11/10.
 */

var EquipDescParser = new Class({
    initialize: function () {
        this.colors = {"R": "red", "G": "green", "B": "blue", "Y": "yellow", "P": "pink", "W": "white", "K": "black"};
        this.re = /#([RGBYPWsbuhnr]|c[0-9A-Za-z]{6}|[0-9]{1,3})/;
        this.compact_mode = true;
    }, do_seg: function (s, pattern) {
        var segs = [];
        while (1) {
            var m = pattern.exec(s);
            if (!m) {
                segs.push(s);
                break;
            }
            segs.push(s.substr(0, m.index));
            for (var i = 1; i < m.length; i++) {
                segs.push(m[i]);
            }
            s = s.substr(m.index + m[0].length);
        }
        return segs;
    }, get_emote_img: function (emote_no) {
        return "http://res.tx3.netease.com/qt/12/bang/images/baozi/" + emote_no + ".gif";
    }, do_lex: function (text) {
        var segs = this.do_seg(text, this.re);
        var data = [];
        var seg_config = {};
        for (var i = 0; i < segs.length; i++) {
            if ((i & 1) == 0) {
                var trim_seg = segs[i].trim();
                var trim_for_lianhu = trim_seg.replace('#w(7)', '').replace('#w(0)', '')
                if (trim_seg.indexOf('속빱令') == 0) {
                    if (segs[i].indexOf('^') != -1) {
                        seg_config['jiahuzhi'] = segs[i];
                        data.push([$extend({}, seg_config), '']);
                        delete seg_config.jiahuzhi;
                    }
                } else if (segs[i].indexOf('^83') != -1) {
                    continue;
                } else if (trim_for_lianhu.indexOf('조빱令') == 0) {
                    if (segs[i].indexOf('^') != -1) {
                        seg_config['lianhuzhi'] = segs[i];
                        data.push([$extend({}, seg_config), '']);
                        delete seg_config.lianhuzhi;
                    } else {
                        segs[i] = segs[i].replace('#w(7)', '').replace('#w(0)', '').replace('#W', '');
                        data.push([$extend({}, seg_config), segs[i]]);
                    }
                } else {
                    segs[i] = segs[i].replace('#w(7)', '').replace('#w(0)', '').replace('#W', '');
                    data.push([$extend({}, seg_config), segs[i]]);
                }
                continue;
            }
            if (segs[i] in this.colors) {
                seg_config["color"] = segs[i];
            } else if (segs[i].charAt(0) == "c") {
                seg_config["color"] = "#" + segs[i].substr(1);
            } else if (segs[i] == "s") {
                seg_config["shake"] = true;
            } else if (segs[i] == "b") {
                seg_config["blink"] = true;
            } else if (segs[i] == "u") {
                seg_config["underline"] = true;
            } else if (segs[i] == "h") {
                seg_config["hide"] = true;
            } else if (segs[i] == "n") {
                seg_config = {};
            } else if (segs[i] == "r") {
                seg_config["br"] = true;
                data.push([$extend({}, seg_config), ""]);
                delete seg_config.br;
            } else if (segs[i].match(/^\d+$/)) {
                seg_config["img"] = true;
                data.push([$extend({}, seg_config), this.get_emote_img(parseInt(segs[i], 10))]);
                delete seg_config.img;
            }
        }
        return data;
    }, get_jia_hu_info: function (info) {
        var no_active_len = info.split("^84").length - 1;
        var result = {};
        result["total_len"] = info.split("^").length - 1;
        result["active_len"] = result["total_len"] - no_active_len;
        return result;
    }, get_jia_hu_html: function (desc) {
        var info = this.get_jia_hu_info(desc);
        var html = "<div class='jhz-box'>" + '<span class="jiaHuZhi">속빱令:</span>' + '<p class="percentBg" style="width:' + info["total_len"] * 8 + 'px">' + '<span class="percentFornt" style="width:' + info["active_len"] * 8 + 'px"></span></p>' + '<br/>' + "</div>";
        return html;
    }, get_lian_hu_info: function (seg) {
        var total_len = seg.split("^").length - 1;
        var last1_tag = seg.split("^92").length - 1;
        var last2_tag = seg.split("^93").length - 1;
        var active_len = total_len - (last1_tag + last2_tag);
        return {"total_len": total_len, "active_len": active_len};
    }, get_lian_hu_html: function (desc) {
        var info = this.get_lian_hu_info(desc);
        var html = "<div class='lhz-box'>" + '<span class="jiaHuZhi">조빱令:</span>' + '<p class="percentBg" style="width:' + info["total_len"] * 8 + 'px">' + '<span class="percentFornt" style="width:' + info["active_len"] * 8 + 'px"></span></p><br/>' + "</div>";
        return html;
    }, get_style_info: function (seg_config) {
        var color = "";
        var cls_list = [];
        for (var n in seg_config) {
            if (n == "color") {
                if (!seg_config["hide"]) {
                    if (seg_config[n].charAt(0) != "#") {
                        cls_list.push(this.colors[seg_config[n]]);
                    } else {
                        color = seg_config[n];
                    }
                }
            } else {
                cls_list.push(n);
            }
        }
        var style_info = [];
        if (color) {
            style_info.push("style='color:" + color + "'");
        }
        if (cls_list) {
            style_info.push("class='" + cls_list.join(" ") + "'");
        }
        return style_info.join(" ");
    }, parse: function (equip_desc) {
        var html_array = [];
        var previous_contains_new_line = true;
        var lex_result = this.do_lex(equip_desc);
        var last_new_line = true;
        for (var i = 0; i < lex_result.length; i++) {
            var seg_config = lex_result[i][0];
            var seg = lex_result[i][1];
            if (seg_config["br"]) {
                if (this.compact_mode && last_new_line) {
                    continue;
                }
                html_array.push("<br />");
                last_new_line = true;
            } else if (seg_config["img"]) {
                html_array.push("<img src='" + seg + "' />");
                last_new_line = false;
            } else if (seg_config["jiahuzhi"]) {
                html_array.push(this.get_jia_hu_html(seg_config["jiahuzhi"]));
            } else if (seg_config["lianhuzhi"]) {
                html_array.push(this.get_lian_hu_html(seg_config["lianhuzhi"]));
            } else {
                if (!seg.replace(/ +/g, "") && this.compact_mode) {
                    continue;
                } else {
                    last_new_line = false;
                }
                var style_info = this.get_style_info(seg_config);
                var span = "<span " + style_info + ">" + seg + "</span>";
                html_array.push(span);
            }
        }
        return html_array.join("");
    }
});