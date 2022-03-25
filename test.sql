select * from authtoken_token
select * from HeroForgeApi_equipment
where classs_id =5 AND level=1

UPDATE HeroForgeApi_equipment
SET ASF = 2, ACP = 6
where name="Hide"

select * from HeroForgeApi_equipment

DELETE from HeroForgeApi_characterfeat
where id = 7

where skill_id=50
select * from HeroForgeApi_skill

update auth_user
set is_staff = 1
where id= 1

DELETE from HeroForgeApi_proficient
where id > 1

DROP TABLE HeroForgeApi_classlevel

DELETE FROM django_migrations WHERE app = "HeroForgeApi"