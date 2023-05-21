# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 子查询练习.py
# @datatime: 2023/5/18 21:08

# 1.查看技术部门的员工姓名
mysql> select name from employee where dep_id = (select id from department where name = '技术');
+-----------+
| name      |
+-----------+
| egon      |
| liwenzhou |
+-----------+
2 rows in set (0.00 sec)

# 2.查询不足1人的部门名
# 先查看哪些部门的员工数 > 0
select distinct dep_id from employee

mysql> select name from department where id not in (select distinct dep_id from employee );
+--------+
| name   |
+--------+
| 运营   |
+--------+
1 row in set (0.00 sec)

# 3.查询大于所有人平均年龄的员工名与年龄


mysql> select avg(age) from employee;
+----------+
| avg(age) |
+----------+
|  28.0000 |
+----------+
1 row in set (0.00 sec)

mysql> select name, age from employee where age > (select avg(age) from employee);
+---------+------+
| name    | age  |
+---------+------+
| alex    |   48 |
| wupeiqi |   38 |
+---------+------+
2 rows in set (0.00 sec)name, age from employee where age > (select avg(age) from employee);

# 4.查询大于部门内平均年龄的员工名、年龄
mysql> select dep_id, avg(age) as avg_age from employee as a group by dep_id;
+--------+---------+
| dep_id | avg_age |
+--------+---------+
|    200 | 18.0000 |
|    201 | 43.0000 |
|    202 | 28.0000 |
|    204 | 18.0000 |
+--------+---------+
4 rows in set (0.00 sec)

mysql> select e.name, e.age from employee e inner join (select dep_id, avg(age) as avg_age from employee group by dep_id) as a
    ->  on e.dep_id = a.dep_id
    ->  where e.age > a.avg_age;
+------+------+
| name | age  |
+------+------+
| alex |   48 |
+------+------+
1 row in set (0.00 sec)

