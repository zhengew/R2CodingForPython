# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 练习.py
# @datatime: 2023/5/18 20:05

# 1.找到技术部的所有人的姓名
mysql> select e.name from department d inner join employee e on d.id = e.dep_id where d.id = 200;
+-----------+
| name      |
+-----------+
| liwenzhou |
| egon      |
+-----------+
2 rows in set (0.00 sec)

# 2.找到人力资源部的年龄大于40岁的人的姓名
mysql> select e.name, d.name as dname from employee e inner join department d on e.dep_id = d.id where d.name = '人力资源' and e.age > 40;
+------+--------------+
| name | dname        |
+------+--------------+
| alex | 人力资源     |
+------+--------------+
1 row in set (0.00 sec)

# 3.找出年龄大于25岁的员工以及员工所在的部门
mysql> select e.name, d.name as dname from employee e inner join department d on e.dep_id = d.id where e.age > 25;
+---------+--------------+
| name    | dname        |
+---------+--------------+
| wupeiqi | 人力资源     |
| alex    | 人力资源     |
| yuanhao | 销售         |
+---------+--------------+
3 rows in set (0.00 sec)

# 4.以内连接的方式查询employee和department表，并且以age字段的升序方式显示
mysql> select e.*, d.* from employee e inner join department d on e.dep_id = d.id order by e.age;
+----+-----------+--------+------+--------+------+--------------+
| id | name      | sex    | age  | dep_id | id   | name         |
+----+-----------+--------+------+--------+------+--------------+
|  1 | egon      | male   |   18 |    200 |  200 | 技术         |
|  5 | liwenzhou | male   |   18 |    200 |  200 | 技术         |
|  4 | yuanhao   | female |   28 |    202 |  202 | 销售         |
|  3 | wupeiqi   | male   |   38 |    201 |  201 | 人力资源     |
|  2 | alex      | female |   48 |    201 |  201 | 人力资源     |
+----+-----------+--------+------+--------+------+--------------+
5 rows in set (0.00 sec)

# 5.求每一个部门有多少人, # 且按照人数从高到低排序
mysql> select d.name, count(e.id) num from department d left join employee e on e.dep_id = d.id group by d.name order by num desc;
+--------------+-----+
| name         | num |
+--------------+-----+
| 技术         |   2 |
| 人力资源     |   2 |
| 销售         |   1 |
| 运营         |   0 |
+--------------+-----+
4 rows in set (0.00 sec)

