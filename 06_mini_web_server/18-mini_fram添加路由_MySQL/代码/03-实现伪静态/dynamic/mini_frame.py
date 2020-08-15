import re

# 方法2：使用装饰器，装饰器特点：程序未运行，就进行装饰
URL_FUNC_DICT = dict()


def route(url):   # 该装饰器的作用是对全局的字典添加键值对，利用py执行时装饰器默认会执行的原理
    def set_func(func):
        # URL_FUNC_DICT["/index.py"] = index
        URL_FUNC_DICT[url] = func
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func

# @route("/index.py")   # 相当于 @set_func  # index = set_func(index)
@route("/index.html")
def index():
    with open("./templates/index.html") as f:
        content = f.read()

    my_stock_info = "哈哈哈哈 这是你的本月名称....."

    content = re.sub(r"\{%content%\}", my_stock_info, content)

    return content
     
# @route("/center.py")
@route("/center.html")
def center():
    # with open("./templates/center.html", encoding="utf-8") as f:
    with open("./templates/center.html") as f:
        content = f.read()

    my_stock_info = "这里是从mysql查询出来的数据。。。"

    content = re.sub(r"\{%content%\}", my_stock_info, content)

    return content


# 方法1： 先写出键值对，网址中文件名作为键；函数名作为值，形成键值对
"""
URL_FUNC_DICT = {
    "/index.html": index,
    "/center.html": center
}
"""

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    
    file_name = env['PATH_INFO']
    print(file_name)
    # file_name = "/index.py"

    """
    if file_name == "/index.py":
        return index()
    elif file_name == "/center.py":
        return center()
    else:
        return 'Hello World! 我爱你中国....'
    """

    try:
        # func = URL_FUNC_DICT[file_name]  # func是函数的引用
        # return func()
        print(URL_FUNC_DICT)
        return URL_FUNC_DICT[file_name]()   # return index 路由的功能：根据请求的不同，调用不同的服务
    except Exception as ret:
        return "产生了异常：%s" % str(ret)







