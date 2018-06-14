# [web-uiautomation-selenium](https://github.com/gaozhao1989/web-uiautomation-selenium) web端ui自动化测试工具

------

使用Python组合工具**Selenium**实现对web端进行ui自动化测试工具。使用 Selenium 作为底层驱动，Pytest 作为测试管理工具，Allure 作为报告输出工具。
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
>   |-pages<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-basepage.py<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-demopage.py<br>
>   |<br>
>   |-report<br>
>   |<br>
>   |-screenshots<br>
>   |<br>
>   |-tests<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-test_demo.py<br>
>   |<br>
>   |-utils<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-configparserfactory.py<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-drivergenerator.py<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-findbyfactory.py<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-loggingfactory.py<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-pathparserfactory.py<br>
>   |<br>
>   -README.md<br>
>   -runner.py<br>

## [web-uiautomation-selenium](https://github.com/gaozhao1989/web-uiautomation-selenium) 结构文件说明
### config
存放配置文件**config.ini**，按照标准ini文件格式储存，configparserfactory.py使用该文件<br>
当前设置包含参数如下：<br>
broswerName | 浏览器名称（如：chrome, firefox)<br>
url | 测试 url 地址<br>
testScope | 测试范围（如：指定测试的文件夹）<br>
workSpaceName | 当前工程文件名称<br>
### drivers
存放webdriver驱动位置，按照linux，mac，windows平台进行区分，其中驱动按照分类文件夹名称（系统名称）进行区分
### pages
存放基础页面**basepage**以及其他测试页面<br>
basepage负责实现页面通用方法<br>
其他测试页面负责实现该页面独有元素、定位方法以及页面操作事件
### report
存放测试结果以及测试报告，其中测试结果由**Pytest**执行用例后生成，测试报告由**Allure**在执行完成后配置Pytest的结果生成，通过网页进行显示<br>
测试结果文件：****.json<br>
测试报告入口：/html/index.html
### screenshots
存放测试过程中生成的截图，建议截图名称均以"时间页面事件.png"的名称进行保存
### tests
存放测试文件，有别于**pages**，测试文件包含测试用例，使用pages文件中操作事件生成测试步骤，可单独进行测试的运行与调试
### utils
存放通用工具文件，包含：<br>
* configparserfactory.py 用于获取配置文件配置
* drivergenerator.py 用于生成driver的入口
* findbyfactory.py 用于设置获取元素查找方法
* loggingfactory.py 用于生成日志的方法
* pathparserfactory.py 用于获取文件路径的
###### README.md
介绍文件
###### runner.py
执行测试入口文件

------

## 所需插件及安装方式
### 1.Selenium
pip install -U selenium
### 2.Selenium
pip install pytest
### 3.Allure
pip install allure-pytest

------

## 调试&运行
### 调试
通过tests目录下的单独**test_xxxx**运行测试，适用范围仅限于当前测试文件
### 运行
通过**config.ini与runner.py**文件指定运行scope，运行指定测试范围