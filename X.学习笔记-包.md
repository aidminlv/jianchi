# 模块
- 一个模块就是一个包含python代码的文件，后缀名称是.py就可以。模块就是个python文件
- 为什么用模块？
    - 程序太大，编写维护非常不方便，需要拆分
    - 模块可以增加代码重复利用的方式
    - 当作命名空间使用，避免命名冲突
- 如何定义模块
    - 模块就是一个普通文件，所以任何代码都可以直接书写
    - 不过根据模块的规范，最好在模块中编写以下内容
        - 函数（单一功能）与Mixin一样，功能单一
        - 类 （相似功能的组合，或者类似业务模块）
        - 测试代码
        
- 如何使用模块
    - 模块可以直接导入
        - 假如模块名称直接以数字开头。需要借助于importlib包实现。
        - 案例：
        
            import importlib
            ##### 相当于导入了一个叫01的模块并把导入模块赋值给了tuling
            tuling = importlib.import_module("01")
            stu = tuling.Student()
            stu.say()  
        
    - 语法
    
            import module_name
            module_name.function_name
            module_name.class_name
    - import 模块.as 别名
        - 导入的同时给模块起一个别名
        - 其余用法跟第一种相同
    - from module_name import func_name, class_name
        - 按上述方法可以有选择性的导入
        - 使用的时候可以直接使用导入的内容，不需要前缀
    - from module_name import *
        - 导入模块所有内容
                
    - if __name__ == "__main__": 的使用
        - 可以有效避免模块代码被导入的时候被动执行的问题
        - 建议所有程序的入口都以此代码为入口

# 模块的搜索路径和存储
- 什么是模块的搜索路径
    - 加载模块的时候，系统会在那些地方寻找此模块
- 系统默认的模块搜索路径
    - 语法
    
            import sys
            sys.path 属性可以获取路径列表
    - 案例
    
            import sys

            print(type(sys.path))
            print(sys.path)

            for p in sys.path:
                print(p)
- 添加搜索路径

        sys.path.append(dir)
- 模块的加载顺序
    1.搜索内存中已经加载好的模块
    2.搜索python的内置模块
    3.搜索 sys.path 路径
    
# 包
- 包是一种组织管理代码的方式，包里面存放的是模块
- 用于将模块包含在一起的文件夹就是包
- 自定义包的结构

        /--- 包
        /---/--- __init__.py 包的标志性文件
        /---/--- 模块1
        /---/--- 模块2
        /---/--- 子包（子文件夹）
        /---/---/--- __init__.py 包的标志性文件
        /---/---/--- 子包模块1
        /---/---/--- 子包模块2
- 包的导入操作
    - import package_name 该语句的意思是直接导入一个包
    - 使用语法：
    
            package_name.func_name
            package.name_class_name.func_name()
    - import package_name as 别名
        - 注意：此种方法时默认对__init__.py内容的导入
        
    - import package.module
        - 导入包中某一个具体的模块
        - 使用方法
        
                package.module.func_name
                package.module.class.fun（）
                package.module.class.var
    - import package.module as 别名
- from ... import 导入
    - from package import module， module1， module2， ......
    - 此种导入方法不执行 '__init__.py' 的内容
    
            from 包名 import 模块名
            模块名.模块内函数名
    - from package import *
        - 导入当前包 "__init__.py"文件中所有的函数和类
        - 使用方法：
        
                func_name（）
                class_name.func_name（）
                class_name.var
- from package.module import *
    - 导入包中指定模块的所有内容
    - 使用方法：
    
            func_name()
            class_name.func_name()
- 在开发环境中经常会用其它模块，可以在当前包中直接导入其他模块中
    - import 完整的包或者模块的路径

- "__all__" 方法
    - 在使用from package import * 的时候，* 可以导入的内容
    - "__init__.py"中如果文件为空，或者没有"__all__"，那么只可以把"__init__"中的内容导入
    - "__init__" 如果设置了"__all__"的值，那么按照"__all__"指定的子包或者模块进行载入，不会载入"__init__"中的内容
    - __all__ 语法：
    
            __all__ = ['模块名1', '模块名2'， '包名1', ...]

# 命名空间
- 用于区分不同位置不同功能但相同名称的函数或者变量的一个特定前缀
- 作用是防止命名冲突

        setName()
        Student.setName()
        Dog.setName()
                