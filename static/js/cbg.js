var CbgJS = function(){
    var submitForm = function(){
        $("#search-form").ajaxSubmit({
            type: 'post', // 提交方式 get/post
            url: "/getCbgPage",
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
        $("#js-reset-btn").click(function () {
            $('#search-form')[0].reset()
        })
        submitForm();
    };
    var buy = function(id,url){
        update(id);
        window.open(url);
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
    var update = function (id) {
        $.ajax({
            type:'post',
            url:'/update',
            data:{'id':id},
            dataType:'json',
            success:function (data) {
            },
            error:function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown)
                return false;
            }
        });
    }

    var detail = function(id,name,level,school){
        update(id);
        var url = "http://bang.tx3.163.com/bang/search#name="+name+"&school="+school+"&level="+level
        window.open(url);
    };
    return {
        init: function () {
            init();
        },
        buy: function (id,url) {
            buy(id,url);
        },
        initPage: function (totalPage, pageNum) {
            pageAjax(totalPage, pageNum);
        },
        soldOut: function (id) {
            soldOut(id);
        },
        detail: function (id,name, level, school) {
            detail(id,name, level, school);
        }
    }
}();
