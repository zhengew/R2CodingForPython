1、查询男生、女生的人数；
mysql> select gender, count(sid) num from student group by gender;
+--------+-----+
| gender | num |
+--------+-----+
| 男     |  10 |
| 女     |   6 |
+--------+-----+
2 rows in set (0.00 sec)

2、查询姓“张”的学生名单；
mysql> select * from student where sname like '张%';
+-----+--------+----------+--------+
| sid | gender | class_id | sname  |
+-----+--------+----------+--------+
|   3 | 男     |        1 | 张三   |
|   4 | 男     |        1 | 张一   |
|   5 | 女     |        1 | 张二   |
|   6 | 男     |        1 | 张四   |
+-----+--------+----------+--------+
4 rows in set (0.00 sec)


3、课程平均分从高到低显示
select s.course_id, c.cname, avg(s.num) avg_num
from score s inner join course c on s.course_id = c.cid
group by s.course_id order by avg_num desc;
+-----------+--------+---------+
| course_id | cname  | avg_num |
+-----------+--------+---------+
|         4 | 美术   | 85.2500 |
|         2 | 物理   | 65.0909 |
|         3 | 体育   | 64.4167 |
|         1 | 生物   | 53.4167 |
+-----------+--------+---------+
4 rows in set (0.00 sec)


4、查询有课程成绩小于60分的同学的学号、姓名；
select stu.sid, stu.sname --, s.num
 from student stu inner join score s on stu.sid = s.student_id
 where s.num < 60;
+-----+--------+-----+
| sid | sname  | num |
+-----+--------+-----+
|   1 | 理解   |  10 |
|   1 | 理解   |   9 |
|   2 | 钢蛋   |   8 |
|   4 | 张一   |  11 |
|   5 | 张二   |  11 |
|   6 | 张四   |   9 |
|   7 | 铁锤   |   9 |
|   8 | 李三   |   9 |
|   9 | 李一   |  22 |
|  10 | 李二   |  43 |
|  11 | 李四   |  43 |
|  12 | 如花   |  43 |
+-----+--------+-----+
12 rows in set (0.01 sec)


5、查询至少有一门课与学号为1的同学所学课程相同的同学的学号和姓名；
-- 学号为1的学生课程
select course_id from score where student_id = 1;
-- 查询选修课程与1重合的学生
select distinct stu.sid, stu.sname
from student stu inner join score s on stu.sid = s.student_id
where s.course_id in (select course_id from score where student_id = 1)
and stu.sid != 1;

+-----+--------+
| sid | sname  |
+-----+--------+
|   2 | 钢蛋   |
|   3 | 张三   |
|   4 | 张一   |
|   5 | 张二   |
|   6 | 张四   |
|   7 | 铁锤   |
|   8 | 李三   |
|   9 | 李一   |
|  10 | 李二   |
|  11 | 李四   |
|  12 | 如花   |
+-----+--------+
11 rows in set (0.01 sec)


6、查询出只选修了一门课程的全部学生的学号和姓名；
select s.student_id, stu.sname
 from score s inner join student stu on s.student_id = stu.sid
 group by s.student_id having count(s.course_id) = 1;
 +------------+--------+
| student_id | sname  |
+------------+--------+
|         13 | 刘三   |
+------------+--------+
1 row in set (0.00 sec)


7、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
select course_id 课程ID, max(num) 最高分, min(num) 最低分
 from score group by course_id order by course_id;
+----------+-----------+-----------+
| 课程ID   | 最高分    | 最低分    |
+----------+-----------+-----------+
|        1 |        91 |         8 |
|        2 |       100 |         9 |
|        3 |        87 |        43 |
|        4 |       100 |        22 |
+----------+-----------+-----------+
4 rows in set (0.00 sec)


8、查询课程编号“2”的成绩比课程编号“1”课程低的所有同学的学号、姓名；
--


9、查询“生物”课程比“物理”课程成绩高的所有学生的学号；
10、查询平均成绩大于60分的同学的学号和平均成绩;
11、查询所有同学的学号、姓名、选课数、总成绩；
12、查询姓“李”的老师的个数；
13、查询没学过“张磊老师”课的同学的学号、姓名；
14、查询学过“1”并且也学过编号“2”课程的同学的学号、姓名；
15、查询学过“李平老师”所教的所有课的同学的学号、姓名；