$("#btn").click(function(){
    $.ajax({
        url:'/login/',
        // url: "{% url 'login' %}", // url别名反向解析
        type:'post',
        data:{
            csrfmiddlewaretoken:$('[name=csrfmiddlewaretoken]').val(), // 方式一
            // csrfmiddlewaretoken: "{{ csrf_token }}", // 方式二
            uname:$('#username').val(),
            pwd:$('#password').val(),
        },
        success:function (res){
            var resStr = JSON.parse(res)
            console.log(res, typeof res)
            if (resStr['code'] === 3) { <!-- 登录失败 -->
                $('form span').remove();
                var spanEle = document.createElement('span');
                $(spanEle).text(resStr['msg']).css({'color':'red'});
                $('form').append(spanEle);
            } else if (resStr['code'] === 0){ <!-- 登录成功 -->
                location.href=resStr['redirect_url'];
            }
        }
    })
})