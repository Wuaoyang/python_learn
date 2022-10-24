# -*- coding: utf-8 -*-
'''
@Time    : 2022-10-18 22:51
@Author  : allen
@File    : demo1.py

'''

# 单行注释
'''
    多行
    注释
'''

# 全局变量
global_s = "global"


# 局部变量, 只能再范围内使用，方法内则为方法内可用
# def属于函数定义，可以下方看到再回来看下
def fun():
    a = 1


# --------------------------------------------------------------------------
print("==================== [打印 start] ↓↓↓↓↓↓ ↓↓↓↓↓↓ ====================")
# 打印文字 对应java System.out.println
# 同Java不同，语句末尾不需要加分号，print内可以用单引号也可以用双引号
print("[打印] 输出一行文字")
print("[打印]巧用1：", "aaa", "bbb", "ccc")
print("[打印]巧用2——增加分隔符：", "aaa", "bbb", "ccc", sep="|")
print("[打印]print默认末尾是换行，demo1")
print("[打印]print默认末尾设置为空字符串，demo2", end="")
print("[打印]print默认末尾是换行，demo3", end="\n")
print("==================== [打印 end] ↑↑↑↑↑↑  ====================", end="\n\n")

# --------------------------------------------------------------------------
print("==================== [变量 start] ↓↓↓↓↓↓  ====================")
# 1. 不需要像java一样，int temp = 0，事先声明变量类型，直接变量名 = 具体值即可
# 2. 布尔类型 True or Flase，首字母需要大写
a = 1
b = True
c = False
d = "str"
print("==================== [变量 end] ↑↑↑↑↑↑  ====================", end="\n\n")

# --------------------------------------------------------------------------
print("==================== [String格式化 start] ↓↓↓↓↓↓  ====================")
format_age = 25
# 普通的字符串拼接
print("[String格式化] 普通字符串拼接：" + str(format_age))
# %d表示整型占位符  #s 字符串  #c 字符 还有其他 可以搜索python 格式符号了解
print("[String格式化] 我的年龄为：%d" % format_age)
format_str = "字符串"
# print("String格式化，字符串为：s%"%format_str)
print("[String格式化] 字符串为：%s" % format_str)
# 使用f格式化
print(f"[String格式化]_f方式 ===> 我的年龄为：{format_age}")
print(f"[String格式化]_f方式 ===> 字符串为：{format_str}")
print("==================== [String格式化 end] ↑↑↑↑↑↑  ====================", end="\n\n")

# --------------------------------------------------------------------------
print("==================== [输入 start] ↓↓↓↓↓↓  ====================")
# todo
# input_str = input("[输入]请输入内容：")
# 打印输入进来的到底是什么类型 --- string类型
# print("你输入的内容类型为:" + str(type(input_str)))
# print(f"你输入的内容是：{input_str}")
print("==================== [输入 end] ↑↑↑↑↑↑  ====================", end="\n\n")

# --------------------------------------------------------------------------
print("==================== [运算表达式 start] ↓↓↓↓↓↓  ====================")
print("[运算表达式], 加法：" + str(1 + 2))
print("[运算表达式], 减法：" + str(1 - 2))
print("[运算表达式], 乘法：" + str(1 * 2))
print("[运算表达式], 除法：" + str(1 / 2))
print("[运算表达式], 取模：" + str(3 % 2))
# java 内是用^去实现，如2的10次，表达为 2^10   但python表达为 2**10
print("[运算表达式], 次方)：" + str(2 ** 3))
print("[运算表达式], 向下取整)：" + str(9 // 2))
print("[运算表达式], 向下取整)：" + str(-9 // 2))

print("==================== [运算表达式 end] ↑↑↑↑↑↑  ====================", end="\n\n")

# --------------------------------------------------------------------------
print(
    "==================== [比较运算符，赋值运算符，逻辑运算符，成员运算符, 身份运算符 start] ↓↓↓↓↓↓  ====================")
print("[比较运算符，赋值运算符，逻辑运算符，成员运算符], 见代码中文字注释")
#
'''
    [比较运算符] 基本同java. 等于== 不等于!= 大于> 小于< 大于等于>= 小于等于<=
    [赋值运算符] 基本同java. a += 1 a -= 1 
    [逻辑运算符] 不同于java. 
        【与】 java中是 &&，python中是 and; 
        【或】 java中是 ||，python中是 or; 
        【非】 java中是 !，python中是 not; 
    [成员运算符] 不同于java
        【存在某个序列中】java一般是使用集合,使用contains去判断，或者遍历去判断，没有配套api，python中是 in
        【不存在某个序列中】同上，java没有配套api，python中是 not in
    [身份运算符] 不同于java
        【判断引用来自一个对象】 java中直接==比较内存地址，python中使用is, 如 x is y
        【判断引用不来自一个对象】 java中直接==比较内存地址，python中使用is not, 如 x is not y
    [运算符优先级]
        指数 > 乘/除/取模/取整 >  加减 > 位移运算 > ... 1
'''
print("==================== [比较运算符，赋值运算符，逻辑运算符，成员运算符, 身份运算符 end] ↑↑↑↑↑↑  ====================",
      end="\n\n")

# --------------------------------------------------------------------------
print("==================== [条件语法 start] ↓↓↓↓↓↓  ====================")
# 缩进保证对应的if范围，不同java。
# java内 if(表达式) {} else if (..){} else {}
# python 具体见下方，{}替换为： 结构层级用相同间隔表示
if 1 == 2:
    print("[条件语法] 1==2")
elif 1 == 3:
    print("[条件语法] 1==3")
else:
    print("[条件语法] else")
print("==================== [条件语法 end] ↑↑↑↑↑↑  ====================", end="\n\n")

# --------------------------------------------------------------------------
print("==================== [引入依赖 start] ↓↓↓↓↓↓  ====================")
# 使用import关键字 引入依赖
import random

print("==================== [引入依赖 end] ↑↑↑↑↑↑  ====================", end="\n\n")

# --------------------------------------------------------------------------
print("==================== [循环语句 start] ↓↓↓↓↓↓  ====================")
# 1. for i in range(5)
for i in range(5):
    print(f"1.[循环语句] for i in range, {i}")
# 2. for i in range(0,10,3) 0-10,3为步长
for i in range(0, 10, 3):
    print(f"2.[循环语句] for i in range(0,10,3), {i}")
# 3. 不同于其他语言，可直接for i in String
for i in "wuaoyang":
    print(f"[循环语句] for i in wuaoyang, {i}")
# 4. for 集合
continue_list = ["aa", "bb", "cc", "dd"]
print("continue_list = [\"aa\", \"bb\", \"cc\", \"dd\"]")
print("3.[循环语句] for i in continue_list")
for i in continue_list:
    print(f"[循环语句 start], {i}")
print("4.[循环语句] for i in range(len(continue_list))")
for i in range(len(continue_list)):
    print(f"[循环语句], i: {i},continue_list[i]: {continue_list[i]}")

# 5. while i < 5: 其中 可以搭配else使用
# 搭配else使用，表示正常结束循环时执行的语句
# 当然，同java等其他语言一样，也可以使用break / continue，分别代表中端 / 继续
while_index = 0
print("5.[循环语句] while while_index < 3:")
while while_index < 3:
    print(f"[循环语句] while_index = {while_index}")
    while_index += 1

print("==================== [循环语句 end] ↑↑↑↑↑↑  ====================", end="\n\n")

# --------------------------------------------------------------------------
print("==================== [字符串 start] ↓↓↓↓↓↓  ====================")
# 1. 定义
string_a = '[字符串]单引号'
string_b = "[字符串]双引号"
string_c = '''
[字符串]三引号1
[字符串]三引号2
'''
print(f"[字符串]:{string_a}")
print(f"[字符串]:{string_b}")
print(f"[字符串]:{string_c}")

# 2. 技巧
# 2.1 截取
print(f"[字符串]-截取，string_b[0]: {string_b[0]}")
# 相当于后面是最后一位，len(string)
print(f"[字符串]-截取，string_b[0:]: {string_b[0:]}")
# 相当于前面补0，即 0:4
print(f"[字符串]-截取，string_b[:4]: {string_b[:4]}")
print(f"[字符串]-截取，string_b[0::2]: {string_b[0::2]}")
print(f"[字符串]-截取，string_b[0:4]: {string_b[0:4]}")
print(f"[字符串]-截取，string_b[0:4:2]: {string_b[0:4:2]}")

# 拼接 str + "xxxx"
# 重复打印 print("xxx" * 2)
# 废除转义 r开头的字符串  print(r"\n")

print("==================== [字符串 end] ↑↑↑↑↑↑  ====================", end="\n\n")

# --------------------------------------------------------------------------
print("==================== [列表 start] ↓↓↓↓↓↓  ====================")
# 1. 定义空列表
list_empty = []

# 2. 定义已有元素的列表
name_list = ["1", 2, True]
for i in name_list:
    # print(f"[列表]打印name_list第一个元素,值为{i},类型为" + str(type(i)))
    print(f"[列表]迭代name_list，值为{i},类型为{type(i)}")

# 3. 打印list长度
print(f"[列表]打印name_list长度为：{len(name_list)}")

# 4. 添加
# 4.1 末尾add
name_list.append("add~")
print(f"[列表]name_list add新增元素：{name_list[3]}")
for i in name_list:
    print(f"[列表]迭代name_list，值为{i},类型为{type(i)}")
# 4.2 指定插入insert
name_list.insert(1, "insert~")
print(f"[列表]name_list insert新增元素：{name_list[1]}")

# 5. 删除
# 5.1 object.remove(xx) -- list从前往后扫，移除第一个匹配的。
print("[列表]name_list移除元素 insert~ start")
name_list.remove("insert~")
print("[列表]name_list 是否还包含insert~元素: " + str("insert~" in name_list))
print("[列表]name_list 末尾加入两个 insert~ 元素")
name_list.append("insert~")
name_list.append("insert~")
# 5.2 要全部移除，可以搭配循环
print("[列表]name_list 要全部移除 insert~ 元素,可以搭配循环")
print("[列表]name_list 是否还包含insert~元素: " + str("insert~" in name_list))
while "insert~" in name_list:
    name_list.remove("insert~")
print("[列表]name_list 是否还包含insert~元素: " + str("insert~" in name_list))
# 5.3 del list[i] -- 移除list某个位置的元素
print(f"[列表]name_list 准备移除元素，现在list内容为: {name_list}")
del name_list[len(name_list) - 1]
print(f"[列表]name_list 使用 del 移除了最后一个元素，现在list内容为: {name_list}")
# 5.4 object.pop() -- 弹出最后的元素
name_list.pop()
print(f"[列表]name_list 使用 pop 移除了最后一个元素，现在list内容为: {name_list}")

# 6.改
name_list[1] = "一号位修改"
print(f"[列表]name_list 使用指定修改1下标，现在list内容为: {name_list}")

# 7. 查元素是否存在
print(f"[列表] \"一号位修改\" 在不在 name_list内: {'一号位修改' in name_list}")

# 8. 获取元素索引, 在
print(f"[列表]name_list 定位 \"一号位修改\"下标位置，name_list.index(\"一号位修改\"): {name_list.index('一号位修改')}")
# print(name_list.index("一号位修改",0,1)) 会报在下标0-1（左闭右开）范围内找不到的错误 应该对应java直接丢异常，要做处理

# 9. 统计出现次数
print(f"[列表]name_list 定位 \"一号位修改\" 出现次数: {name_list.count('一号位修改')}")

# 10. 反转
name_list.reverse()
print(f"[列表]name_list 反转:{name_list}")

# 11. 排序，默认升序，反转
name_list.sort()
name_list.sort(reverse=True)
print("==================== [列表 end] ↑↑↑↑↑↑  ====================", end="\n\n")

# --------------------------------------------------------------------------
print("==================== [元组 start] ↓↓↓↓↓↓  ====================")
# 1. 定义
# python 有，java无
# 可以理解为就是一些元素的集合，同list一样，没有强类型一致限制，比如可以同时存储int string boolean
# 一个元素的时候，他相当于是个普通元素，如(1),要让他变成元组，需要这样(1,) -- 是的，确实让javaer看着不大舒服hh
tup1 = (1, 2, 3, 4, True, "sss")
print(f"[元组]打印tup1:{tup1}")
print(f"[元组]打印tup1 第一个元素:{tup1[0]}")
print(f"[元组]打印tup1 最后一个元素:{tup1[-1]}")
print(f"[元组]打印tup1 最后0-3的元素:{tup1[0:4]}")

# 2. 增删改查
# 增删改全部会报错
# 增：两个元组可以直接拼凑一块
tup2 = (6, 7)
tup_all = tup1 + tup2
print(f"[元组]打印tup1 + tup2 :{tup_all}")
# 删： 特例，del tup1 其实就是删除引用，不能再用，是允许的
print("==================== [元组 end] ↑↑↑↑↑↑  ====================", end="\n\n")

# --------------------------------------------------------------------------
print("==================== [字典 start] ↓↓↓↓↓↓  ====================")
# 1. 定义
# 同java中map，即键值对，使用{}直接表示
map = {"name": "allen", "age": 25, "friends": ["liko", "Ciky"]}

# 2. 打印
print(f"[字典] map:{map}")

# 3. 查
# --- 获取单值
# 3.1 直接map[key] -- 如果内部不包含这个key，会报错
# 3.2 object.get(key) -- 如果内部不包含这个key，会返回None
# 3.3 object.get(key,defaultValue) -- 如果内部不包含这个key，会返回设定的defaultValue
print(f"[字典] map获取name的value：{map['name']}")
# 会报错 ：
# print(f"[字典] map获取不存在的key：{map['notkey']}")
print(f"[字典] map获取不存在的key：{map.get('notkey')}")
print(f"[字典] map获取不存在的key,若不存在设置为'default'：{map.get('notkey', 'default')}")

# 获取所有的键
print(f"[字典] map获取所有key：{map.keys()}")
# 获取所有的value
print(f"[字典] map获取所有vaule：{map.values()}")
# 获取所有的元素
print(f"[字典] map获取所有元素：{map.items()}")

# 遍历所有的键or值，写法很简单，如下
# for i in map.keys():
# for i in map.values():
# 遍历元素写法可以记一下，如下
# for key, val in map.items():
# for item in map.items():

# do something

# 4.新增
map["sex"] = "man"
print(f"[字典]新增sex键，value为：{map.get('sex')}")

# 5. 删除
del map["sex"]
print(f"[字典]删除sex键，打印最新map：{map}")
# tip: del 整个引用，那么整个不能用

# 6. 清空 （删除的特例，就是清空元素内容）
map_temp = map.copy()
map.clear()
print(f"[字典] map.clear()，打印最新map：{map}")
map = map_temp
print(f"清理后还原,最新map为：{map}")

# 7. 改
map["name"] = "new_allen"
print(f"[字典]修改name键，value为：{map.get('name')}")

print("==================== [字典 end] ↑↑↑↑↑↑  ====================", end="\n\n")

# --------------------------------------------------------------------------
print("==================== [集合(set!!!) start] ↓↓↓↓↓↓  ====================")
set_t = {1, 2, 3, 2, 2, 2}
print(f"[集合]，即set:{set_t}")
print("==================== [集合(set!!!) end] ↑↑↑↑↑↑  ====================", end="\n\n")

# --------------------------------------------------------------------------
print("==================== [函数 start] ↓↓↓↓↓↓  ====================")


# 1. 定义
# 1.1 无参，无返回值 def function()
def print_first():
    print("[函数] print_first 欢迎你")


# 1.2 有参，无返回值 def function(params)
def sum_2_nums(a, b):
    print(f"[函数] a + b :{a + b}")


# 1.3 有返回值 return
def get_sum_2_nums(a, b):
    return a + b


# 1.4 这个真特殊啊  带多个返回值
def get_sum_and_sub(a, b):
    return a + b, a - b


# 带返回值
# 2. 调用
print_first()
sum_2_nums(1, 2)
print(f"[函数] a + b :{get_sum_2_nums(1, 2)}")
# 对应接收多个返回值
sum, sub = get_sum_and_sub(1, 2)
print(f"[函数] a + b :{sum}, a - b: {sub}")

print("==================== [函数 end] ↑↑↑↑↑↑  ====================", end="\n\n")

# --------------------------------------------------------------------------
print("==================== [文件处理 start] ↓↓↓↓↓↓  ====================")
# 1. 文件基本操作
# file = open("file路径","w/r/wb/rb")
# file.close()

# 2. w模式(write模式)打开一个文件并写入字符，若没有该文件，会进行创建
file = open("test01.txt", "w")
file.write("hello world!")
file.close()

# 3. r模式(read模式)打开一个文件并读取字符
file = open("test01.txt", "r")
print(f"[文件处理] 读取5个字符:{file.read(5)}")
file.close()
file = open("test01.txt", "r")
print(f"[文件处理] 读取所有字符:{file.read()}")
file.close()
file = open("test01.txt", "r")
print(f"[文件处理] 按照readLine读取所有字符:{file.readlines()}")
file.close()
print("==================== [文件处理 end] ↑↑↑↑↑↑  ====================", end="\n\n")

# --------------------------------------------------------------------------
print("==================== [异常处理 start] ↓↓↓↓↓↓  ====================")
# 捕获异常 对应java-- try catch finally
try :
    file = open("123123","r")
except Exception as result:
    print(f"[异常处理] 捕获异常success,错误为:{result}")
    pass
finally:
    print("[异常处理] finally 区")


print("==================== [异常处理 end] ↑↑↑↑↑↑  ====================", end="\n\n")

# --------------------------------------------------------------------------
print("==================== [import start] ↓↓↓↓↓↓  ====================")
# 类似java 直接import
import random
print(f"[import] 直接import random, 获取随机数{random.randint(0, 5)}")
# 类似vue之类的写法，从某个pkg下引入某个类
from import_learn import ImportFile
print(f"[from dir import pyfile] , 获取随机数{ImportFile.getRandom()}")

print("==================== [import end] ↑↑↑↑↑↑  ====================", end="\n\n")


# --------------------------------------------------------------------------
print("==================== [元组 start] ↓↓↓↓↓↓  ====================")

print("==================== [元组 end] ↑↑↑↑↑↑  ====================", end="\n\n")
