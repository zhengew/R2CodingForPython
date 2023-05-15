/*
. 查看岗位是teacher的员工姓名、年龄
. 查看岗位是teacher且年龄大于30岁的员工姓名、年龄
. 查看岗位是teacher且薪资在9000-10000范围内的员工姓名、年龄、薪资
. 查看岗位描述不为NULL的员工信息
. 查看岗位是teacher且薪资是10000或9000或30000的员工姓名、年龄、薪资
. 查看岗位是teacher且薪资不是10000或9000或30000的员工姓名、年龄、薪资
. 查看岗位是teacher且名字是jin开头的员工姓名、年薪

*/

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

mysql> select emp_name as name, age from employee t where t.post = 'teacher';
+------------+-----+
| name       | age |
+------------+-----+
| alex       |  78 |
| wupeiqi    |  81 |
| yuanhao    |  73 |
| liwenzhou  |  28 |
| jingliyang |  18 |
| jinxin     |  18 |
| 成龙       |  48 |
+------------+-----+
7 rows in set (0.00 sec)

mysql> select emp_name as name, age from employee where post = 'teacher' and age > 30;
+---------+-----+
| name    | age |
+---------+-----+
| alex    |  78 |
| wupeiqi |  81 |
| yuanhao |  73 |
| 成龙    |  48 |
+---------+-----+
4 rows in set (0.00 sec)

mysql>
mysql>
mysql> select emp_name as name, age, salary from employee where post = 'teacher' and salary between 9000 and 10000;
+------------+-----+----------+
| name       | age | salary   |
+------------+-----+----------+
| jingliyang |  18 |  9000.00 |
| 成龙       |  48 | 10000.00 |
+------------+-----+----------+
2 rows in set (0.00 sec)

mysql> select * from employee where post_comment is not null;
Empty set (0.00 sec)

mysql> select emp_name as name, age, salary from employee where post = 'teacher' and salary in (10000, 9000, 30000);
+------------+-----+----------+
| name       | age | salary   |
+------------+-----+----------+
| jingliyang |  18 |  9000.00 |
| jinxin     |  18 | 30000.00 |
| 成龙       |  48 | 10000.00 |
+------------+-----+----------+
3 rows in set (0.00 sec)

mysql> select emp_name as name, age, salary from employee where post = 'teacher' and salary not  in (10000, 9000, 30000);
+-----------+-----+------------+
| name      | age | salary     |
+-----------+-----+------------+
| alex      |  78 | 1000000.31 |
| wupeiqi   |  81 |    8300.00 |
| yuanhao   |  73 |    3500.00 |
| liwenzhou |  28 |    2100.00 |
+-----------+-----+------------+
4 rows in set (0.00 sec)


mysql> select emp_name as name, salary * 12 as annual_year from employee where post = 'teacher' and emp_name regexp('^jin');
+------------+-------------+
| name       | annual_year |
+------------+-------------+
| jingliyang |   108000.00 |
| jinxin     |   360000.00 |
+------------+-------------+
2 rows in set (0.02 sec)