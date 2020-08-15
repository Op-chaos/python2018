
def index():
	return "这是主页"

def login():
	return "这是登录页面"

def application(env, start_response):     # wsgi协议格式
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    
    file_name = env['PATH_INFO']
    # file_name = "/index.py"

    if file_name == "/index.py":
    	return index()
    elif file_name == "/login.py":
    	return login()
    else:
    	return 'Hello World! 我爱你中国....'
		


# import time
# 动态发送时间
#
# def login():
#     return "i----login--welcome hahahh to our website.......time:%s" % time.ctime()
#
# def register():
#     return "-----register---welcome hahahh to our website.......time:%s" % time.ctime()
#
# def application(file_name):
# 	if file_name == "/login.py":
# 		return login()
# 	elif file_name == "/register.py":
# 		return register()
# 	else:
# 		return "not found you page...."