create database oo;
use oo;
create table hospital(sno varchar(6),name varchar(10),age varchar(3),phone varchar(14),gender varchar(8),dob varchar(20),address varchar(20),height varchar(2),weight varchar(2),pid varchar(10),disease varchar(20),admit_date varchar(15),discharge_date varchar(20),guardian_name varchar(20));
insert into hospital values('1','mittu','55','7569642310','male','20-nov-1998','india','5','41','6281314216','dengue','27-aug-2008','09-sept-2008','hari');
insert into hospital values('2','akshay','21','7569642318','female','20-nov-2002','hyderabad','6','49','6281314211','typhoid','29-aug-2008','19-sept-2008','navya');
insert into hospital values('3','vamsi','44','7569642313','male','20-dec-1998','telangana','7','51','6281317216','cancer','26-aug-2002','09-sept-2002','satya');


select *from hospital;