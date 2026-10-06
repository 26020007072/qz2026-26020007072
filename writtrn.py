#选择题 + 简答题
#一、选择题（每题 2 分，共 10 题，满分 20 分）
#1.B 2.B 3.B 4.B 5.B 6.B 7.B 8.B 9.B 10.B


#二、简答题
#第1题：浅拷贝与深拷贝
#b = a.copy()是浅拷贝，b中元素与a中的子列表一样；c = copy,deepcopy(a)是深拷贝：c是一个全新的列表，与a完全独立
#执行后b = [[1,2,99],[3,4]]   c = [[1,2],[3,4]]

#第2题：字典与列表的综合应用
logs = [
    {"user": "张三", "action": "login", "level": "INFO"},
    {"user": "李四", "action": "logout", "level": "INFO"},
    {"user": "张三", "action": "error", "level": "ERROR"},
    {"user": "王五", "action": "login", "level": "INFO"},
    {"user": "李四", "action": "error", "level": "ERROR"},
]
#1.
errors = []
for log in logs:
    if log["level"] == "ERROR":
        errors.append(log)
#2.
count = {}
for log in logs:
    user = log["user"]
    if user in count:
        count[user] = count[user] + 1
    else:
        count[user] = 1
#3.len用于统计日志个数而非每个用户出现几次，count用于计数;用一个for循环遍历logs，再用一个字典累计每个用户出现的次数

#第3题：异常处理设计
def safe_divide(a,b):
    try:
        x = int(a)
        y = int(b)
        result = x / y
        return result
    except ValueError:
        return None
    except ZeroDivisionError:
        return None
#使用try/expect不会出现报错的情况，代码运行更通畅

