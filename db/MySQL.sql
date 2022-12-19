--Sample Database
https://dev.mysql.com/doc/employee/en/

mysql --version
mysql --help

mysql -u root -p
select version(), current_date, curdate();
select user(), now();

show databases;
show variables like 'character%';
show variables;  --show all SYSTEM VARIABLES
show status;  --server status

show variables like '%autocommit%';
set AUTOCOMMIT=0;  --turn off autocommit

select database();

-------------------------------------------------------------------------
--modify the configuration file to fix Chinese encoding, must restart service to take effect

$ sudo nano /etc/mysql/my.cnf

/*
[client]
default-character-set=utf8mb4

[mysql]
default-character-set=utf8mb4

[mysqld]
character_set_server=utf8mb4
collation-server=utf8mb4_unicode_ci
*/

$ /etc/init.d/mysql stop
$ /etc/init.d/mysql start

ALTER TABLE table_name CONVERT TO CHARACTER SET utf8mb4;  --may be necessary as well

-------------------------------------------------------------------------
create database SECRET;
use SECRET;
select database();

show tables;

create table secret (account varchar(30), id varchar(100), password varchar(100) not null, answer varchar(100),
remark varchar(200), primary key (account, id)
);

show tables;
show create table secret;

desc secret;

select count(*) from secret;

/* scripting in mysql */
source /home/neo-mashiro/Documents/.doc/.masked.sql;  --load and execute script

-------------------------------------------------------------------------
/* A sample */
create database MUSIC;
use MUSIC;
select database();

show tables;

create table music (
  id         int not null auto_increment,
  file_nm    varchar(100),
  track_no   int,
  play_time  time not null,
  year       char(4),
  artist     varchar(200),
  album      varchar(200) not null,
  root_path  varchar(999),  /* upper level file path */
  primary key (id)
);

show tables;

desc music;

select distinct artist from music;
select distinct album from music;
select * from music where artist is null or album is null;
select count(*) from music group by year;
select max(play_time) from music;
select * from music order by play_time asc limit 10;

--@: User-Defined Variables that can memorize current query results
--then use @ variables in the next query to avoid complicated sub queries
select @shortest := MIN(play_time), @longest := MAX(play_time) from music;
select * from music where play_time = @shortest or play_time = @shortest;
-------------------------------------------------------------------------
