1、查询没有学全所有课的同学的学号、姓名；
-- 查询总共有几门课程
select count(cid) from course; -- 4
-- score表根据学生id分组，筛选出数量小于 课程总数的学生id
select stu.sid, stu.sname
 from student stu right join
    (select student_id as sid
     from score
     group by student_id having count(student_id) < (select count(cid) from course)) s
 on stu.sid = s.sid;
+------+--------+
| sid  | sname  |
+------+--------+
|    1 | 理解   |
|    2 | 钢蛋   |
|   13 | 刘三   |
+------+--------+
3 rows in set (0.00 sec)


2、查询和“002”号的同学学习的课程完全相同的其他同学学号和姓名；
**【更改为：查询和“003”号的同学学习的课程完全相同的其他同学学号和姓名】**
-- 查询 002 学习的课程id
select course_id from score where student_id = 003; -- 1, 2, 3, 4
-- 查询学习任意一门 003 学习的课程的学生id,按照student_id分组，统计每组数量 = 学号003的课程数量的student_id
select student_id from score where course_id in (select course_id from score where student_id = 003) and student_id != 002 group by student_id having count(student_id) = (select count(course_id) from score where student_id = 003);
-- 获取最终的学号和姓名
select stu.sid, stu.sname
 from student stu right join (
    select student_id from score where course_id in (select course_id from score where student_id = 003) and student_id != 002 group by student_id having count(student_id) = (select count(course_id) from score where student_id = 003)
 ) s on stu.sid = s.student_id;
+------+--------+
| sid  | sname  |
+------+--------+
|    3 | 张三   |
|    4 | 张一   |
|    5 | 张二   |
|    6 | 张四   |
|    7 | 铁锤   |
|    8 | 李三   |
|    9 | 李一   |
|   10 | 李二   |
|   11 | 李四   |
|   12 | 如花   |
+------+--------+
10 rows in set (0.02 sec)

3、删除学习“叶平”老师课的SC表记录；
-- 查询 叶平老师教授的课程id
select c.cid from course c inner join teacher t on c.teacher_id = t.tid where t.tname = '李平老师'; -- 2, 4
+-----+
| cid |
+-----+
|   2 |
|   4 |
+-----+
2 rows in set (0.00 sec)
-- 删除score表 course_id in (2, 4) 的记录
delete from score where course_id in (select c.cid from course c inner join teacher t on c.teacher_id = t.tid where t.tname = '李平老师');
commit;

4、向SC表中插入一些记录，这些记录要求符合以下条件：①没有上过编号“002”课程的同学学号；②插入“002”号课程的平均成绩；
-- 查询没学过课程2的学生id
select distinct student_id from score where student_id not in (select distinct student_id from score where course_id = 2)
+------------+
| student_id |
+------------+
|          1 |
|          2 |
|          3 |
|          4 |
|          5 |
|          6 |
|          7 |
|          8 |
|          9 |
|         10 |
|         11 |
|         12 |
|         13 |
+------------+
13 rows in set (0.00 sec)
-- 查询课程2的平均成绩
select avg(num) from score group by course_id having course_id = 2;
-- 插入数据
insert into score(student_id, course_id, num) values(1, 2, 0);


5、按平均成绩从低到高显示所有学生的“语文”、“数学”、“英语”三门的课程成绩，按如下形式显示： 学生ID,语文,数学,英语,有效课程数,有效平均分；
-- 查询课程id
select cid from course where cname = '生物'; -- 1
select cid from course where cname = '物理'; -- 2
select cid from course where cname = '体育'; -- 3
-- pass

**【更改为】按平均成绩从低到高显示所有学生的“生物”、“物理”、“体育”、"美术"四门的课程成绩，按如下形式显示： 学生ID,生物,物理,体育,美术,有效课程数,有效平均分；**


6、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
select course_id 课程ID, max(num) 最高分, min(num) 最低分 from score group by course_id;
+----------+-----------+-----------+
| 课程ID   | 最高分    | 最低分    |
+----------+-----------+-----------+
|        1 |        91 |         8 |
|        2 |         0 |         0 |
|        3 |        87 |        43 |
+----------+-----------+-----------+
3 rows in set (0.01 sec)

7、按各科平均成绩从低到高和及格率的百分数从高到低顺序；
-- 计算各科平积分及总人数
select course_id, avg(num) as avg_score, count(1) as sum_num from score group by course_id;
-- 计算各科及格人数
select course_id, count(1) from score where num > 60 group by course_id;
-- 连表计算及格率
select t1.course_id, t1.avg_score, concat(round((t2.pass_num / t1.sum_num * 100), 2), '%') as pass_rate
 from (select course_id, avg(num) as avg_score, count(1) as sum_num from score group by course_id) t1
 left join (select course_id, count(1) as pass_num from score where num > 60 group by course_id) t2
 on t1.course_id = t2.course_id
 order by t1.avg_score asc, pass_rate desc;
+-----------+-----------+-----------+
| course_id | avg_score | pass_rate |
+-----------+-----------+-----------+
|         1 |   53.4167 | 58.33%    |
|         3 |   64.4167 | 75.00%    |
|         2 |   65.0909 | 72.73%    |
|         4 |   85.2500 | 91.67%    |
+-----------+-----------+-----------+
4 rows in set (0.00 sec)


8、查询各科成绩前三名的记录:(不考虑成绩并列情况)
-- 构造一张按成绩排序的表
select sid, course_id,
    (select num from score s2 where s2.course_id = s1.course_id order by num desc limit 0, 1) as first_num,
    (select num from score s2 where s2.course_id = s1.course_id order by num desc limit 1, 1) as second_num,
    (select num from score s2 where s2.course_id = s1.course_id order by num desc limit 2, 1) as third_num
from score as s1

-- 连表查询
select t1.sid, t1.course_id, t1.student_id, t1.num
from score t1 left join (
    select sid, course_id,
    (select num from score s2 where s2.course_id = s1.course_id order by num desc limit 0, 1) as first_num,
    (select num from score s2 where s2.course_id = s1.course_id order by num desc limit 1, 1) as second_num,
    (select num from score s2 where s2.course_id = s1.course_id order by num desc limit 2, 1) as third_num
from score as s1
 ) t2 on t1.sid = t2.sid where t1.num = t2.first_num or t1.num = t2.second_num or t1.num = t2.third_num order by t1.course_id, t1.num desc;


9、查询每门课程被选修的学生数；
select course_id, count(student_id) from score group by course_id;
+-----------+-------------------+
| course_id | count(student_id) |
+-----------+-------------------+
|         1 |                12 |
|         2 |                 1 |
|         3 |                12 |
+-----------+-------------------+
3 rows in set (0.00 sec)

10、查询同名同姓学生名单，并统计同名人数；
insert into student (gender, class_id, sname) values('女', 1, '钢蛋');
insert into student (gender, class_id, sname) values('男', 1, '理解');
commit;
-- 查询同名的学生姓名
select sname from student group by sname having count(sname) > 1;
-- 统计人数
select sname, count(sname) from student group by sname having sname in (select sname from student group by sname having count(sname) > 1);
+--------+--------------+
| sname  | count(sname) |
+--------+--------------+
| 理解   |            2 |
| 钢蛋   |            2 |
+--------+--------------+
2 rows in set (0.01 sec)


11、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；
select course_id, avg(num) avg_num from score group by course_id order by avg_num, course_id desc;

+-----------+---------+
| course_id | avg_num |
+-----------+---------+
|         2 |  0.0000 |
|         1 | 53.4167 |
|         3 | 64.4167 |
+-----------+---------+
3 rows in set (0.00 sec)


12、查询平均成绩大于85的所有学生的学号、姓名和平均成绩；
-- 按学生id分组，查询平均成绩大于85的学生id和平均分
select student_id, avg(num) avg_num from score group by student_id having avg(num) > 85;
-- 连接student表，查询学生姓名
select stu.sid, stu.sname, s.avg_num
 from student stu right join (select student_id, avg(num) avg_num from score group by student_id having avg(num) > 85) s
 on stu.sid = s.student_id;
+------+--------+---------+
| sid  | sname  | avg_num |
+------+--------+---------+
|   13 | 刘三   | 87.0000 |
+------+--------+---------+
1 row in set (0.00 sec)

13、查询课程名称为“数学”，且分数低于60的学生姓名和分数；

**【更改为】查询课程名称为“生物”，且分数低于60的学生姓名和分数；**
-- 查询生物课程id
select cid from course where cname = '生物'; -- 1
-- score表学习生物课程并且成绩低于60的学生id及分数
select student_id, num from score where course_id = (select cid from course where cname = '生物') and num < 60;
+------------+-----+
| student_id | num |
+------------+-----+
|          1 |  10 |
|          2 |   8 |
|          6 |   9 |
|          7 |   9 |
|          8 |   9 |
+------------+-----+
5 rows in set (0.00 sec)
-- 关联学生表，拿到学生姓名
select stu.sname, s.num
 from student stu right join (select student_id, num from score where course_id = (select cid from course where cname = '生物') and num < 60) s
 on stu.sid = s.student_id;
+--------+-----+
| sname  | num |
+--------+-----+
| 理解   |  10 |
| 钢蛋   |   8 |
| 张四   |   9 |
| 铁锤   |   9 |
| 李三   |   9 |
+--------+-----+
5 rows in set (0.00 sec)


14、查询课程编号为003且课程成绩在80分以上的学生的学号和姓名；
-- 查询学习课程3的学生id
select student_id from score where course_id = 3;
-- 连表查询学生姓名
select stu.sid, stu.sname
 from student stu right join (select student_id from score where course_id = 3) s
 on stu.sid = s.student_id;
+------+--------+
| sid  | sname  |
+------+--------+
|    2 | 钢蛋   |
|    3 | 张三   |
|    4 | 张一   |
|    5 | 张二   |
|    6 | 张四   |
|    7 | 铁锤   |
|    8 | 李三   |
|    9 | 李一   |
|   10 | 李二   |
|   11 | 李四   |
|   12 | 如花   |
|   13 | 刘三   |
+------+--------+
12 rows in set (0.00 sec)

15、求选了课程的学生人数

select count(1) from (select distinct student_id from score) t; -- 13
+----------+
| count(1) |
+----------+
|       13 |
+----------+
1 row in set (0.00 sec)