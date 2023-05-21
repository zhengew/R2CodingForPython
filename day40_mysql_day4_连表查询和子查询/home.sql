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
-- 查询课程1的学生id, 课程1的成绩
select student_id, num c1_num from score where course_id = '1';
-- 查看课程2的学生id，课程2的成绩
select student_id, num c2_num from score where course_id = '2';

-- inner 上面2个表，在比较课程1和合成2的成绩，再通过student_id 查询学生表的sid 和 sname
select s1.student_id, stu.sname, s1.c1_num, s2.c2_num
 from student stu inner join (select student_id, num c1_num from score where course_id = '1') s1
 on stu.sid = s1.student_id
 inner join (select student_id, num c2_num from score where course_id = '2') s2
 on s1.student_id = s2.student_id
 where c2_num < c1_num;

 +------------+--------+--------+--------+
| student_id | sname  | c1_num | c2_num |
+------------+--------+--------+--------+
|          1 | 理解   |     10 |      9 |
|          3 | 张三   |     77 |     66 |
|          4 | 张一   |     79 |     11 |
|          5 | 张二   |     79 |     11 |
|          9 | 李一   |     91 |     88 |
|         10 | 李二   |     90 |     77 |
|         11 | 李四   |     90 |     77 |
|         12 | 如花   |     90 |     77 |
+------------+--------+--------+--------+
8 rows in set (0.00 sec)

mysql> select s1.student_id, stu.sname
    ->  from student stu inner join (select student_id, num c1_num from score where course_id = '1') s1
    ->  on stu.sid = s1.student_id
    ->  inner join (select student_id, num c2_num from score where course_id = '2') s2
    ->  on s1.student_id = s2.student_id
    ->  where c2_num < c1_num;
+------------+--------+
| student_id | sname  |
+------------+--------+
|          1 | 理解   |
|          3 | 张三   |
|          4 | 张一   |
|          5 | 张二   |
|          9 | 李一   |
|         10 | 李二   |
|         11 | 李四   |
|         12 | 如花   |
+------------+--------+
8 rows in set (0.00 sec)


9、查询“生物”课程比“物理”课程成绩高的所有学生的学号；
select cid from course where cname = '生物'; -- 1
select cid from course where cname = '物理'; -- 2

select s1.student_id, s1.c1_num, s2.c2_num
 from (select student_id, num c1_num from score where course_id = (select cid from course where cname = '生物')) s1
 inner join (select student_id, num c2_num from score where course_id = (select cid from course where cname = '物理')) s2
 on s1.student_id = s2.student_id
 where c1_num > c2_num;
+------------+--------+--------+
| student_id | c1_num | c2_num |
+------------+--------+--------+
|          1 |     10 |      9 |
|          3 |     77 |     66 |
|          4 |     79 |     11 |
|          5 |     79 |     11 |
|          9 |     91 |     88 |
|         10 |     90 |     77 |
|         11 |     90 |     77 |
|         12 |     90 |     77 |
+------------+--------+--------+
8 rows in set (0.01 sec)

mysql> select s1.student_id
    ->  from (select student_id, num c1_num from score where course_id = (select cid from course where cname = '生物')) s1
    ->  inner join (select student_id, num c2_num from score where course_id = (select cid from course where cname = '物理')) s2
    ->  on s1.student_id = s2.student_id
    ->  where c1_num > c2_num;
+------------+
| student_id |
+------------+
|          1 |
|          3 |
|          4 |
|          5 |
|          9 |
|         10 |
|         11 |
|         12 |
+------------+
8 rows in set (0.01 sec)

10、查询平均成绩大于60分的同学的学号和平均成绩;
select student_id, group_concat(num), avg(num) avg_num from score group by student_id having avg(num) > 60;
+------------+-------------------+---------+
| student_id | group_concat(num) | avg_num |
+------------+-------------------+---------+
|          3 | 77,66,87,99       | 82.2500 |
|          4 | 79,11,67,100      | 64.2500 |
|          5 | 79,11,67,100      | 64.2500 |
|          6 | 9,100,67,100      | 69.0000 |
|          7 | 9,100,67,88       | 66.0000 |
|          8 | 9,100,67,88       | 66.0000 |
|          9 | 91,88,67,22       | 67.0000 |
|         10 | 90,77,43,87       | 74.2500 |
|         11 | 90,77,43,87       | 74.2500 |
|         12 | 90,77,43,87       | 74.2500 |
|         13 | 87                | 87.0000 |
+------------+-------------------+---------+
11 rows in set (0.00 sec)

mysql> select student_id, avg(num) avg_num from score group by student_id having avg(num) > 60;
+------------+---------+
| student_id | avg_num |
+------------+---------+
|          3 | 82.2500 |
|          4 | 64.2500 |
|          5 | 64.2500 |
|          6 | 69.0000 |
|          7 | 66.0000 |
|          8 | 66.0000 |
|          9 | 67.0000 |
|         10 | 74.2500 |
|         11 | 74.2500 |
|         12 | 74.2500 |
|         13 | 87.0000 |
+------------+---------+
11 rows in set (0.00 sec)

11、查询所有同学的学号、姓名、选课数、总成绩；
select s.student_id 学号, count(student_id) 选课数, sum(num) 总成绩
 from score s inner join student stu on s.student_id = stu.sid
 group by s.student_id;
 +--------+-----------+-----------+
| 学号   | 选课数    | 总成绩    |
+--------+-----------+-----------+
|      1 |         3 |        85 |
|      2 |         3 |       175 |
|      3 |         4 |       329 |
|      4 |         4 |       257 |
|      5 |         4 |       257 |
|      6 |         4 |       276 |
|      7 |         4 |       264 |
|      8 |         4 |       264 |
|      9 |         4 |       268 |
|     10 |         4 |       297 |
|     11 |         4 |       297 |
|     12 |         4 |       297 |
|     13 |         1 |        87 |
+--------+-----------+-----------+
13 rows in set (0.00 sec)

12、查询姓“李”的老师的个数；
mysql> select * from teacher where tname regexp('^李');
+-----+--------------+
| tid | tname        |
+-----+--------------+
|   2 | 李平老师     |
|   5 | 李杰老师     |
+-----+--------------+
2 rows in set (0.01 sec)

mysql> select count(tid) from teacher where tname regexp('^李');
+------------+
| count(tid) |
+------------+
|          2 |
+------------+
1 row in set (0.00 sec)


13、查询没学过“张磊老师”课的同学的学号、姓名；
select tid from teacher where tname = '张磊老师'; -- 1
-- 查询张磊教过的课程
select cid from course where teacher_id = (select tid from teacher where tname = '张磊老师');

-- 查询学过张磊课程的学生id
select student_id, course_id from score where course_id in (select cid from course where teacher_id = (select tid from teacher where tname = '张磊老师'));

-- 去重查询没学过张磊课程的学生的学号和姓名
select sid, sname from student where sid not in (select distinct student_id from score where course_id in (select cid from course where teacher_id = (select tid from teacher where tname = '张磊老师')));
+-----+--------+
| sid | sname  |
+-----+--------+
|  13 | 刘三   |
|  14 | 刘一   |
|  15 | 刘二   |
|  16 | 刘四   |
+-----+--------+
4 rows in set (0.00 sec)

14、查询学过“1”并且也学过编号“2”课程的同学的学号、姓名；
select student_id from score where course_id = 1;
select student_id from score where course_id = 2;

select stu.sid, stu.sname
 from student stu inner join (select student_id from score where course_id = 1) s1
 on stu.sid = s1.student_id
 inner join (select student_id from score where course_id = 2) s2
 on s1.student_id = s2.student_id;
 +-----+--------+
| sid | sname  |
+-----+--------+
|   1 | 理解   |
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
11 rows in set (0.00 sec)


15、查询学过“李平老师”所教的所有课的同学的学号、姓名；
-- 李平老师的tid
select tid from teacher where tname = '李平老师'; -- 2
-- 李平老师教过的课程id
select cid from course where teacher_id = (select tid from teacher where tname = '李平老师'); -- 2, 4

-- 教的课程总数 2
select count(cid) from course where teacher_id = (select tid from teacher where tname = '李平老师'); -- 2, 4

-- score表
select s.student_id, stu.sname
 from score s inner join student stu on s.student_id = stu.sid
 where s.course_id in (select cid from course where teacher_id = (select tid from teacher where tname = '李平老师'))
 group by s.student_id
 having count(s.student_id) = (select count(cid) from course where teacher_id = (select tid from teacher where tname = '李平老师'));
+------------+--------+
| student_id | sname  |
+------------+--------+
|          1 | 理解   |
|          3 | 张三   |
|          4 | 张一   |
|          5 | 张二   |
|          6 | 张四   |
|          7 | 铁锤   |
|          8 | 李三   |
|          9 | 李一   |
|         10 | 李二   |
|         11 | 李四   |
|         12 | 如花   |
+------------+--------+
11 rows in set (0.00 sec)


-- 查询学过
select distinct stu.sid, stu.sname
 from student stu
 inner join () s1
 where s.course_id in ()
 order by stu.sid;