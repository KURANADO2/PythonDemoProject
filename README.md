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


self 表示当前实例
cls 表示当前类

Rule Engine 规则引擎
Config Driven
Drools 配置化管理 https://www.drools.org/ 配置驱动程序，业务变动只需要更改配置，而不用更改代码

Django
