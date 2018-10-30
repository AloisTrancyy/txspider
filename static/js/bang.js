var BangJS = function(){
    var submitForm = function(){
        $("#search-form").ajaxSubmit({
            type: 'post', // 提交方式 get/post
            url: "/getBangPage",
            success: function(data) { // data 保存提交后返回的数据，一般为 json 数据
                // 此处可对 data 作相关处理
                $("#js-page-body").html(data);
            }
        });
    };
    var pageAjax = function(totalPage, pageNum){
        $('#js-bootpag').bootpag({
            total: totalPage,
            page: pageNum,
            maxVisible: 5,
            leaps: false,
            firstLastUse: true,
            first: '首页',
            last: '尾页',
            wrapClass: 'pagination',
            activeClass: 'active',
            disabledClass: 'disabled',
            nextClass: 'next',
            prevClass: 'prev',
            lastClass: 'last',
            firstClass: 'first'
        }).on("page", function(event, num){
            $("#js-bootpag-num").val(num);
            submitForm();
            $("#js-bootpag-num").val("1");
        });
    };
    var init = function(){
        $("#js-query-btn").click(function(){
            submitForm();
        });
        $("#js-add-btn").click(function() {
            var bang_url = $('#bang_url').val();
            if (bang_url == null || bang_url == 0) {
                alert("英雄榜链接不能为空!");
                return;
            }
            $.ajax({
                url: "/bang/add",
                type: "post",
                data:{'bang_url':bang_url},
                dataType:'json',
                success: function (r) {
                    if (r.returncode == 0) {
                        $("#ajax-modal").modal("hide");
                        submitForm();
                    } else {
                        alert(r.message);
                    }
                },
                error: function (msg, textStatus) {
                    alert(msg);
                }
            });
        });
    };
    var soldOut = function(id){
        if(window.confirm("确定要删除吗？")){
            $.ajax({
                type:'post',
                url:'/delete',
                data:{'id':id},
                dataType:'json',
                success:function (data) {
                    if(data.returncode==0){
                        submitForm();
                    }else{
                        alert(data.message);
                    }
                },
                error:function (XMLHttpRequest, textStatus, errorThrown) {
                    alert(errorThrown)
                    return false;
                }
            });
        }
    };
    var detail = function(name,level,school){
        if(level>80){
            level=80;
        }
        var url = "http://bang.tx3.163.com/bang/search#name="+name+"&school="+school+"&level="+level
        window.open(url);
    };
    return {
        init: function () {
            init();
        },
        initPage: function (totalPage, pageNum) {
            pageAjax(totalPage, pageNum);
        },
        soldOut: function (id) {
            soldOut(id);
        },
        detail: function (name, level, school) {
            detail(name, level, school);
        }
    }
}();