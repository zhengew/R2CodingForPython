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


3、删除学习“叶平”老师课的SC表记录；

4、向SC表中插入一些记录，这些记录要求符合以下条件：①没有上过编号“002”课程的同学学号；②插入“002”号课程的平均成绩；



5、按平均成绩从低到高显示所有学生的“语文”、“数学”、“英语”三门的课程成绩，按如下形式显示： 学生ID,语文,数学,英语,有效课程数,有效平均分；

**【更改为】按平均成绩从低到高显示所有学生的“生物”、“物理”、“体育”、"美术"四门的课程成绩，按如下形式显示： 学生ID,生物,物理,体育,美术,有效课程数,有效平均分；**


6、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；

7、按各科平均成绩从低到高和及格率的百分数从高到低顺序；


8、查询各科成绩前三名的记录:(不考虑成绩并列情况)


9、查询每门课程被选修的学生数；

10、查询同名同姓学生名单，并统计同名人数；

11、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；


12、查询平均成绩大于85的所有学生的学号、姓名和平均成绩；


13、查询课程名称为“数学”，且分数低于60的学生姓名和分数；

**【更改为】查询课程名称为“生物”，且分数低于60的学生姓名和分数；**


14、查询课程编号为003且课程成绩在80分以上的学生的学号和姓名；


15、求选了课程的学生人数