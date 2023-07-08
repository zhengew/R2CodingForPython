from django.shortcuts import render, HttpResponse

# Create your views here.


def app01Index(request):
    return HttpResponse('基础估值配置')


# 验证自定义过滤器
def app01myfilter(request):

    content = 'hello world myfilter'
    name = 'xuefei'
    sex = 'female'
    age = 18
    return render(request, 'myfilter.html', {'content': content, 'name': name, 'sex': sex, 'age': age})


# 验证自定义标签
def app01mytags(request):
    name = 'dazhuang'
    sex = 'male'
    age = 20
    return render(request, 'mytags.html', {'name': name, 'sex': sex, 'age': age})

# 验证 inclusion_tag标签
def app01_inclusion_tag(request):

    s1 = '1. app应用文件夹中创建一个templatetags文件件,必须是这个名字'
    s2 = '2. templatetags文件夹中创建一个 xx.py文件,文件名字随便起'
    s3 = """
        3. 创建自定义inclusion_tag
        @register.inclusion_tag('inclusiontag.html')
        def func(v1):
    
            return {'oo':v1}
    """
    s4 = '4. func的return数据,传给了inclusiontag.html,作为模板渲染的数据,将inclusiontag.html渲染好之后,作为一个组件,生成到调用这个func的地方'
    s5 = """
        5. 使用
        {% load xx %}
        {% func l1 %}
    """

    res = [s1, s2, s3, s4, s5]

    return render(request, 'my_inclusion_tag.html', {'res': res})