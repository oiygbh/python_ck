# @Time : 2021/12/30 21:22 
# @Author :jiale
# @File : class3.py 
# @Software: PyCharm
#  利用元类实现框架类
# ORM模型
"""
类-------->
"""
from class_08day.find import BaseFiled, BoolFiled, CharFiled, IntFiled


# 利用元类实现模型类

class FieldMetaClass(type):
    """
    模型类的元类
    """

    def __new__(cls, name, bases, dic, *args, **kwargs):
        if name == 'BaseModel':
            return super().__new__(cls, name, bases, dic)
        else:
            table_name = name.lower()  # 将类名转换为小写，对应数据表的名称
            fields = {}  # 定义一个空字典，存放模型类和数据表中字段的对应关系
            for k, v in dic.items():  # 遍历所有属性判断属性值是否为字段类型
                if isinstance(v, BaseFiled):
                    fields[k] = v
            dic['t_name'] = table_name
            dic['fields'] = fields
            return super().__new__(cls, name, bases, dic)


class BaseModel(metaclass=FieldMetaClass):  # 指定元类
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self,k,v)  #  遍历所有关键字参数，并且对镀锡进行属性设置，对象 属性名 属性值
    def save(self):
        # 保存一条数据，生成一条对应的sql语句
        # 获取表名
        t_name=self.t_name
        # 获取字段名
        fields=self.fields
        # field_dict={},创建一个字典用来存储键值对
        # 获取对应字段值
        for field in fields.keys():
            value=getattr(self,field)

        # 生成对应的sql语句


# 用户模型类
class User(BaseModel):
    username = CharFiled()
    pwd = CharFiled()
    age = IntFiled()
    live = BoolFiled()
    # 字段1：字符串类型
    # 字段2：数值类型
    # 字段3：布尔类型


#  订单模型类
class Order(BaseModel):
    id = IntFiled()
    money = IntFiled()


print(User.fields)
print(User.t_name)
xiaoming = User(username='小明', age=18, pwd='123', live=True)
Order1=Order(id=111,money=222)
print(xiaoming.username)
print(Order1.id)