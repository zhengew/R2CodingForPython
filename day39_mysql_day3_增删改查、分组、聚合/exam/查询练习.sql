mysql> select concat('名字:', emp_name) from employee;
+-----------------------------+
| concat('名字:', emp_name)   |
+-----------------------------+
| 名字:egon                   |
| 名字:alex                   |
| 名字:wupeiqi                |
| 名字:yuanhao                |
| 名字:liwenzhou              |
| 名字:jingliyang             |
| 名字:jinxin                 |
| 名字:成龙                   |
| 名字:歪歪                   |
| 名字:丫丫                   |
| 名字:丁丁                   |
| 名字:星星                   |
| 名字:格格                   |
| 名字:张野                   |
| 名字:程咬金                 |
| 名字:程咬银                 |
| 名字:程咬铜                 |
| 名字:程咬铁                 |
+-----------------------------+
18 rows in set (0.00 sec)

mysql> select concat('<名字:', emp_name, '>') as name, concat('<薪资:', salary, '>') as annual_salary from employee;
+---------------------+---------------------+
| name                | annual_salary       |
+---------------------+---------------------+
| <名字:egon>         | <薪资:7300.33>      |
| <名字:alex>         | <薪资:1000000.31>   |
| <名字:wupeiqi>      | <薪资:8300.00>      |
| <名字:yuanhao>      | <薪资:3500.00>      |
| <名字:liwenzhou>    | <薪资:2100.00>      |
| <名字:jingliyang>   | <薪资:9000.00>      |
| <名字:jinxin>       | <薪资:30000.00>     |
| <名字:成龙>         | <薪资:10000.00>     |
| <名字:歪歪>         | <薪资:3000.13>      |
| <名字:丫丫>         | <薪资:2000.35>      |
| <名字:丁丁>         | <薪资:1000.37>      |
| <名字:星星>         | <薪资:3000.29>      |
| <名字:格格>         | <薪资:4000.33>      |
| <名字:张野>         | <薪资:10000.13>     |
| <名字:程咬金>       | <薪资:20000.00>     |
| <名字:程咬银>       | <薪资:19000.00>     |
| <名字:程咬铜>       | <薪资:18000.00>     |
| <名字:程咬铁>       | <薪资:17000.00>     |
+---------------------+---------------------+
18 rows in set (0.00 sec)

mysql> desc employee;
+--------------+-----------------------+------+-----+---------+----------------+
| Field        | Type                  | Null | Key | Default | Extra          |
+--------------+-----------------------+------+-----+---------+----------------+
| id           | int                   | NO   | PRI | NULL    | auto_increment |
| emp_name     | varchar(20)           | NO   |     | NULL    |                |
| sex          | enum('male','female') | NO   |     | male    |                |
| age          | int unsigned          | NO   |     | 28      |                |
| hire_date    | date                  | NO   |     | NULL    |                |
| post         | varchar(50)           | YES  |     | NULL    |                |
| post_comment | varchar(100)          | YES  |     | NULL    |                |
| salary       | double(15,2)          | YES  |     | NULL    |                |
| office       | int                   | YES  |     | NULL    |                |
| depart_id    | int                   | YES  |     | NULL    |                |
+--------------+-----------------------+------+-----+---------+----------------+
10 rows in set (0.00 sec)

mysql> select distinct post from employee;
+-----------------------------------------+
| post                                    |
+-----------------------------------------+
| 老男孩驻沙河办事处外交大使              |
| teacher                                 |
| sale                                    |
| operation                               |
+-----------------------------------------+
4 rows in set (0.00 sec)

mysql> select emp_name as name, salary * 12 as annual_year from employee;
+------------+-------------+
| name       | annual_year |
+------------+-------------+
| egon       |    87603.96 |
| alex       | 12000003.72 |
| wupeiqi    |    99600.00 |
| yuanhao    |    42000.00 |
| liwenzhou  |    25200.00 |
| jingliyang |   108000.00 |
| jinxin     |   360000.00 |
| 成龙       |   120000.00 |
| 歪歪       |    36001.56 |
| 丫丫       |    24004.20 |
| 丁丁       |    12004.44 |
| 星星       |    36003.48 |
| 格格       |    48003.96 |
| 张野       |   120001.56 |
| 程咬金     |   240000.00 |
| 程咬银     |   228000.00 |
| 程咬铜     |   216000.00 |
| 程咬铁     |   204000.00 |
+------------+-------------+
18 rows in set (0.01 sec)

mysql>