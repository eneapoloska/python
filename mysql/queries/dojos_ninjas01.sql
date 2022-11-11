use dojos_and_ninjas_schema;
select * from dojos;
insert into dojos (name) values ('dojo1');
insert into dojos (name) values ('dojo2');
insert into dojos (name) values ('dojo3');
delete from dojos;
select * from dojos;
insert into dojos (name) values ('dojo4');
insert into dojos (name) values ('dojo5');
insert into dojos (name) values ('dojo6');
select * from dojos;

select * from ninjas;
insert into ninjas (first_name, last_name, age, dojo_id) values ('ninja1', 'jujitsu', 228, 7);
update ninjas set age = 28 where id = 4;
insert into ninjas (first_name, last_name, age, dojo_id) values ('ninja2', 'jujitsu', 25, 7);
insert into ninjas (first_name, last_name, age, dojo_id) values ('ninja3', 'jujitsu', 21, 7);
select * from ninjas;

insert into ninjas (first_name, last_name, age, dojo_id) values ('ninja4', 'jing', 20, 8);
insert into ninjas (first_name, last_name, age, dojo_id) values ('ninja5', 'jing', 23, 8);
insert into ninjas (first_name, last_name, age, dojo_id) values ('ninja6', 'jing', 30, 8);
select * from ninjas;

insert into ninjas (first_name, last_name, age, dojo_id) values ('ninja7', 'sake', 30, 9);
insert into ninjas (first_name, last_name, age, dojo_id) values ('ninja8', 'sake', 26, 9);
insert into ninjas (first_name, last_name, age, dojo_id) values ('ninja9', 'sake', 22, 9);
select * from ninjas;

select * from ninjas where dojo_id = 7;
select * from ninjas where dojo_id = 9;
select * from ninjas where id =12;






#SET SQL_SAFE_UPDATES = 0;
#SET FOREIGN_KEY_CHECKS=0; -- to disable them
#SET FOREIGN_KEY_CHECKS=1; -- to re-enable them