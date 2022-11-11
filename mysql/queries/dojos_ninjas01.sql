use dojos_and_ninjas_schema;
select * from dojos;

insert into dojos (name) values ('durres');

update dojos set name = 'shkoder' where id = 3;
select * from ninjas;
insert into ninjas (first_name, last_name, age, dojo_id) values ('Endi', 'Mimini', 24, 1);
insert into ninjas (first_name, last_name, age, dojo_id) values ('Endi2', 'Mimini', 24, 2);

select dojos.name as qyteti, ninjas.first_name as qytetari  from dojos left join ninjas on ninjas.dojo_id = dojos.id  where dojos.id=1;
