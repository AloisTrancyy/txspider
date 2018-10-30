$(function () {
    init_zhiye();
    init_xiuwei();
    init_zhuangbei();
    init_zongxiuwei();
    init_server_fenbu();
    init_shili_fenbu();
});
function init_zhiye() {
    // 基于准备好的dom，初始化echarts实例
    var map_zhiye = echarts.init(document.getElementById('map_zhiye'),'shine');
    var school_count = new Array();
    $.ajax({
        type: 'get',
        url: '/report/school',
        dataType: 'json',
        async: false,
        success: function (data) {
            if (data.returncode == 0) {
                for (var index in data.result) {
                    school_count.push(data.result[index].count)
                }
            } else {
                alert(data.message);
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert(errorThrown)
            return false;
        }
    });
    // 指定图表的配置项和数据
    var map_zhiye_option = {
        title: {
            text: '门派分布',
            x: 'center'
        },
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
            orient: 'vertical',
            left: 'left',
            data: ['荒火教', '天机营', '翎羽山庄', '魍魉', '太虚观', '云麓仙居', '冰心堂', '弈剑听雨阁', '鬼墨', '龙巫宫']
        },
        series: [
            {
                name: '门派分布',
                type: 'pie',
                radius: '55%',
                center: ['50%', '60%'],
                data: [
                    {value: school_count[0], name: '荒火教'},
                    {value: school_count[1], name: '天机营'},
                    {value: school_count[2], name: '翎羽山庄'},
                    {value: school_count[3], name: '魍魉'},
                    {value: school_count[4], name: '太虚观'},
                    {value: school_count[5], name: '云麓仙居'},
                    {value: school_count[6], name: '冰心堂'},
                    {value: school_count[7], name: '弈剑听雨阁'},
                    {value: school_count[8], name: '鬼墨'},
                    {value: school_count[9], name: '龙巫宫'}
                ],
                itemStyle: {
                    emphasis: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ]
    };
    // 使用刚指定的配置项和数据显示图表。
    map_zhiye.setOption(map_zhiye_option);
}
function init_xiuwei() {
    // 基于准备好的dom，初始化echarts实例
    var map_xiuwei_fenbu = echarts.init(document.getElementById('map_xiuwei_fenbu'),'shine');
    var xiuwei_count = new Array();
    $.ajax({
        type: 'get',
        url: '/report/xiuwei',
        dataType: 'json',
        async: false,
        success: function (data) {
            if (data.returncode == 0) {
                for (var index in data.result) {
                    xiuwei_count.push(data.result[index].count)
                }
            } else {
                alert(data.message);
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert(errorThrown)
            return false;
        }
    });
    // 指定图表的配置项和数据
    var map_xiuwei_fenbu_option = {
        title: {
            text: '人物修为',
            x: 'center'
        },
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
            orient: 'vertical',
            left: 'left',
            data: ['低于3万', '30000-35000', '35000-40000', '45000-50000', '55000-60000', '大于6万']
        },
        series: [
            {
                name: '人物修为',
                type: 'pie',
                radius: '55%',
                center: ['50%', '60%'],
                data: [
                    {value: xiuwei_count[0], name: '低于30000'},
                    {value: xiuwei_count[1], name: '30000-35000'},
                    {value: xiuwei_count[2], name: '35000-40000'},
                    {value: xiuwei_count[3], name: '45000-50000'},
                    {value: xiuwei_count[4], name: '55000-60000'},
                    {value: xiuwei_count[5], name: '大于60000'}
                ],
                itemStyle: {
                    emphasis: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ]
    };
    // 使用刚指定的配置项和数据显示图表。
    map_xiuwei_fenbu.setOption(map_xiuwei_fenbu_option);
}
function init_zhuangbei() {
    // 基于准备好的dom，初始化echarts实例
    var map_zhuangbei_fenbu = echarts.init(document.getElementById('map_zhuangbei_fenbu'),'shine');
    var equ_count = new Array();
    $.ajax({
        type: 'get',
        url: '/report/equ',
        dataType: 'json',
        async: false,
        success: function (data) {
            if (data.returncode == 0) {
                for (var index in data.result) {
                    equ_count.push(data.result[index].count)
                }
            } else {
                alert(data.message);
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert(errorThrown)
            return false;
        }
    });
    // 指定图表的配置项和数据
    var map_zhuangbei_fenbu_option = {
        title: {
            text: '装备评价',
            x: 'center'
        },
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
            orient: 'vertical',
            left: 'left',
            data: ['60000-65000', '65000-70000', '75000-80000', '80000-85000', '85000-90000', '90000-95000','95000-100000','大于10万']
        },
        series: [
            {
                name: '装备评价',
                type: 'pie',
                radius: '55%',
                center: ['50%', '60%'],
                data: [
                    {value: equ_count[0], name: '60000-65000'},
                    {value: equ_count[1], name: '65000-70000'},
                    {value: equ_count[2], name: '75000-80000'},
                    {value: equ_count[3], name: '80000-85000'},
                    {value: equ_count[4], name: '85000-90000'},
                    {value: equ_count[5], name: '90000-95000'},
                    {value: equ_count[6], name: '95000-100000'},
                    {value: equ_count[7], name: '大于10万'}
                ],
                itemStyle: {
                    emphasis: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ]
    };
    // 使用刚指定的配置项和数据显示图表。
    map_zhuangbei_fenbu.setOption(map_zhuangbei_fenbu_option);
}
function init_zongxiuwei() {
    // 基于准备好的dom，初始化echarts实例
    var map_zongxiuwei_fenbu = echarts.init(document.getElementById('map_zongxiuwei_fenbu'),'shine');
    var equxiuwei_count = new Array();
    $.ajax({
        type: 'get',
        url: '/report/equxiuwei',
        dataType: 'json',
        async: false,
        success: function (data) {
            if (data.returncode == 0) {
                for (var index in data.result) {
                    equxiuwei_count.push(data.result[index].count)
                }
            } else {
                alert(data.message);
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert(errorThrown)
            return false;
        }
    });
    // 指定图表的配置项和数据
    var map_zongxiuwei_fenbu_option = {
        title: {
            text: '总修为分布',
            x: 'center'
        },
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
            orient: 'vertical',
            left: 'left',
            data: ['100000-110000', '110000-120000', '120000-130000', '130000-140000', '140000-150000', '150000-160000', '大于16万']
        },
        series: [
            {
                name: '总修为分布',
                type: 'pie',
                radius: '55%',
                center: ['50%', '60%'],
                startAngle:90,
                data: [
                    {value: equxiuwei_count[0], name: '100000-110000'},
                    {value: equxiuwei_count[1], name: '110000-120000'},
                    {value: equxiuwei_count[2], name: '120000-130000'},
                    {value: equxiuwei_count[3], name: '130000-140000'},
                    {value: equxiuwei_count[4], name: '140000-150000'},
                    {value: equxiuwei_count[5], name: '150000-160000'},
                    {value: equxiuwei_count[6], name: '大于16万'}
                ],
                itemStyle: {
                    emphasis: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ]
    };
    // 使用刚指定的配置项和数据显示图表。
    map_zongxiuwei_fenbu.setOption(map_zongxiuwei_fenbu_option);
}
function init_server_fenbu() {
    // 基于准备好的dom，初始化echarts实例
    var server_fenbu = echarts.init(document.getElementById('server_fenbu'),'shine');
    var server_name_count = new Array();
    var server_count = new Array();
    $.ajax({
        type: 'get',
        url: '/report/server',
        dataType: 'json',
        async: false,
        success: function (data) {
            if (data.returncode == 0) {
                for (var index in data.result) {
                    server_name_count.push(data.result[index].server)
                    server_count.push(data.result[index].count)
                }
            } else {
                alert(data.message);
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert(errorThrown)
            return false;
        }
    });
    // 指定图表的配置项和数据
    var server_fenbu_option = {
        title: {
            text: '服务器分布'
        },
        tooltip: {},
        legend: {
            data: ['人数']
        },
        xAxis: {
            data: server_name_count,
            axisLabel: {
                interval:0,
                rotate: 60,
            }
        },
        yAxis: {},
        series: [{
            name: '人数',
            type: 'bar',
            data: server_count
        }]
    };
    // 使用刚指定的配置项和数据显示图表。
    server_fenbu.setOption(server_fenbu_option);
}
function init_shili_fenbu() {
    // 基于准备好的dom，初始化echarts实例
    var shili_fenbu = echarts.init(document.getElementById('shili_fenbu'),'shine');
    var family_name_count = new Array();
    var family_count = new Array();
    $.ajax({
        type: 'get',
        url: '/report/family',
        dataType: 'json',
        async: false,
        success: function (data) {
            if (data.returncode == 0) {
                for (var index in data.result) {
                    family_name_count.push(data.result[index].family)
                    family_count.push(data.result[index].count)
                }
            } else {
                alert(data.message);
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert(errorThrown)
            return false;
        }
    });
    // 指定图表的配置项和数据
    var shili_fenbu_option = {
        title: {
            text: '势力分布'
        },
        tooltip: {},
        legend: {
            data: ['人数']
        },
        xAxis: {
            data: family_name_count,
            axisLabel: {
                interval:0,
                rotate: 60,
            }
        },
        yAxis: {},
        series: [{
            name: '人数',
            type: 'bar',
            data: family_count
        }]
    };
    // 使用刚指定的配置项和数据显示图表。
    shili_fenbu.setOption(shili_fenbu_option);
}
