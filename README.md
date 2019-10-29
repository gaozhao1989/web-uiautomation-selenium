# [web-uiautomation-selenium](https://github.com/gaozhao1989/web-uiautomation-selenium) web端ui自动化测试工具

------

使用[Python](https://www.python.org)组合工具[Selenium](https://www.seleniumhq.org)实现对web端进行ui自动化测试工具。使用 Selenium 作为底层驱动，[Pytest](https://docs.pytest.org/en/latest/) 作为测试管理工具，[Allure](http://allure.qatools.ru) 作为报告输出工具。
目录结构如下：

>  web-uiautomation-selenium<br>
>   |-config<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-config.ini<br>
>   |<br>
>   |-drivers<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-linux<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-mac<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-win<br>
>   |<br>
>   |-locators<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-main_page_locators.py<br>
>   |<br>
>   |-pages<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-base_page.py<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-main_page.py<br>
>   |<br>
>   |-report<br>
>   |<br>
>   |-screenshots<br>
>   |<br>
>   |-tests<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-conftest.py<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-test_order.py<br>
>   |<br>
>   |-utils<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-config_parser.py<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-log.py<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-path_parser.py<br>
>   |<br>
>   -conftest.py<br>
>   -README.md<br>
>   -requirements.txt<br>
>   -runner.py<br>
>   -setup.py<br>

## [web-uiautomation-selenium](https://github.com/gaozhao1989/web-uiautomation-selenium) 结构文件说明
### config
存放配置文件**config.ini**，按照标准ini文件格式储存，config_parser.py使用该文件<br>
当前设置包含参数如下：<br>
broswerName | 浏览器名称（如：chrome, firefox)<br>
url | 测试 url 地址<br>
dateFormat | 时间格式（截图工具会使用到此参数）<br>
implicitlyWait | selenium隐式等待时间<br>
rerunFailures | 测试用例失败后的重跑次数<br>
rerunDelay | 测试用例重跑的等待时间<br>
### drivers
存放webdriver驱动位置，按照linux，mac，windows平台进行区分，其中驱动按照分类文件夹名称（系统名称）进行区分
### locators
存放页面独有元素、定位方法
### pages
存放基础页面**base_page**以及其他测试页面<br>
base_page负责实现页面通用方法<br>
其他页面负责实现该页面操作事件
### report
存放测试结果以及测试报告，其中测试结果由**Pytest**执行用例后生成，测试报告由**Allure**在执行完成后配置Pytest的结果生成，可通过网页进行查看<br>
测试结果文件：****.json<br>
测试报告入口：/html/index.html
### screenshots
存放测试过程中生成的截图，建议截图名称均以"时间页面事件.png"的名称进行保存
### tests
存放测试文件，测试文件需要以**test_xxxx**开头
* conftest.py
为测试用例提供数据支持
* test_order.py
在测试类中，测试函数同样需要以**test_xxxx**开头。测试文件包含测试用例，使用pages文件中操作事件生成测试步骤，可单独进行测试的运行与调试
### utils
存放通用工具文件，包含：<br>
* config_parser.py 用于获取配置文件配置
* log.py 用于生成日志
* path_parser.py 用于获取文件路径
###### conftest.py
**Pytest**的全局挂钩，实现测试setUp与tearDown，实现webdriver的初始化和调用
###### README.md
介绍文件
###### requirements.txt
当前工程所需依赖及版本
###### runner.py
批量执行测试入口文件（将会自动调用重跑机制，测试完成后将会自动生成网页版测试报告「该测试报告由[Allure](http://allure.qatools.ru)提供支持」）
###### setup.py
打包文件以及相关描述「一般不进行此操作，不加入版本控制」

------

## 所需依赖、插件及安装方式
#### 依赖
selenium==3.141.0<br>
pytest==4.1.0<br>
allure-pytest==2.5.4<br>
requests==2.21.0<br>
pytest-rerunfailures==5.0<br>
#### 依赖安装
pip install -r requirements.txt
#### 插件
allure==2.8.1
#### 插件安装
brew install allure

------

## 调试&运行
### 调试
通过**tests**目录下的单独**test_xxxx**运行测试，适用范围仅限于当前测试文件
### 运行
通过**runner.py**文件指定运行，运行指定测试目录默认为**tests**目录

------

## 查看测试结果
注意：直接打开*index.html*在某些浏览器中将显示结果为*404 not found*<br>
使用命令行工具：allure serve [path_of_report]<br>
可以直接启动allure服务并查看测试结果