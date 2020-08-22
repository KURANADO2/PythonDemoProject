Python 培训代码

应具备的五大能力：
- A Architecture
- B Business
- C Coding Core Algorithm
- D Design
- E English
    - ted.com

whl 文件
在线安装：
python -m pip install mysql-connector-python
或下载文件后本地安装：
python -m pip install mysql_connector_python-8.0.21-py2.py3-none-any.whl

- 公司用到的所有依赖都必须经过法务部门审核，审核通过后放到公司内部调用，研发不得私自使用任何开源项目
- GitHub 屏蔽，只有法务部门才可以访问 GitHub
- 每天下午 4:30 停止工作，开始 Review 所有邮件然后再发出去
- 不得使用公司邮箱注册任何非公司账号
- 邮件一定要抄送自己的领导（主管、经理）

pip list 查看已安装模块列表
pip uninstall xxx 卸载模块

DROP DATABASE demo;
CREATE DATABASE demo DEFAULT CHARSET utf8;
USE demo;
CREATE TABLE employee(
    id INT PRIMARY KEY AUTO_INCREMENT,
    code VARCHAR(50),
    name VARCHAR(100)
);
INSERT INTO employee(code, name) VALUES('001', 'jing');


self 表示当前实例
cls 表示当前类

Rule Engine 规则引擎
Config Driven
Drools 配置化管理 https://www.drools.org/ 配置驱动程序，业务变动只需要更改配置，而不用更改代码

Django

- 项目中一般不会实现真正的删除功能，只是做了一个标记，是逻辑删除，并不是物理删除
- 若元祖里只有一个值，则要加一个多余的逗号，如：cursor.execute(sql, (id,))，当然也可以不适用元组，使用 list 也可以，如 cursor.execute(sql, [id])

- pip install aiohttp
- pip install jinja2

- 如果是跳转页面的 url 则以 `ui` 为前缀
- 如果是访问后台接口的 url 则以 `services` 为前缀

统计分析很少使用关系型数据库，因为关系库有很多局限性
为了防止前端更改页面结构，影响自动化测试，与前端约定 uid，uid 很少变动
xpath