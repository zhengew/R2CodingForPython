# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: day38_作业.py
# @datatime: 2023/5/15 20:10

"""
SELECT DATABASE();

-- 班级表
create table class(
	cid int unsigned primary key auto_increment,
	caption char(10) not null unique
);

-- 老师表
create table teacher(
	tid int unsigned primary key auto_increment,
	tname char(18) not null  unique
);

-- 课程表
create table course(
	cid int unsigned primary key auto_increment,
	cname char(18) not null unique,
	tearch_id int unsigned,
	foreign key(tearch_id) references teacher(tid)
);

-- 学生表
create table student(
	sid int unsigned primary key auto_increment,
	sname char(18) not null unique,
	gender enum('male', 'female') default('male'),
	class_id int unsigned,
	foreign key(class_id) references class(cid)
);

-- 成绩表
create table score(
	sid int unsigned primary key auto_increment,
	student_id int unsigned,
	course_id int unsigned,
	number tinyint unsigned not null,
	foreign key(student_id) references student(sid),
	foreign key(course_id) references course(cid)
);


insert into class(caption) values ('三年二班'),('一年三班'),('三年一班');
insert into teacher(tname) values ('波多'),('苍空'),('饭岛');
insert into student(sname,gender,class_id) values ('钢蛋','female',1),('钢锤','female',1),('山炮','male',2);
insert into course(cname,tearch_id) values ('生物',1),('体育',2),('物理',2);
insert into score values (1,1,1,60),(2,1,2,59),(3,2,2,100);

"""