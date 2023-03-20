
import execjs

print(execjs.get())

# 毫秒为单位
# print(execjs.eval("Date.now()"))

# 执行JS
js_code = '''
      function xl(){
           return 'hello world'
        }
'''
# 想传参的话，函数定义的时候直接写，外面调用的时候，指明函数名和参数即可
js_code2 = '''
      function xl(a,b,d){
           return a + b + d
        }
'''
cell = execjs.compile(js_code2)  # 执行对应功能之前先编译对应的js代码
res = cell.call('xl', 1, 2, 3)
print(res)

# with open('03-test.js',encoding='utf-8') as f:
#     jscode = f.read()

# _cell = execjs.compile(jscode)
# ress = _cell.call('xl','13','14','15','16')   # 第一个参数为函数名，之后为参数
# print(ress)
