-- Active: 1680697388601@@127.0.0.1@3306@flask_shop
insert into t_menu (id,name,level) value (0,'全部',0);
insert into t_menu (id,name,level,pid) value (2,'用户管理',1,0);
insert into t_menu (id,name,level,pid) value (3,'权限管理',1,0);
insert into t_menu (id,name,level,pid) value (4,'商品管理',1,0);
insert into t_menu (id,name,level,pid) value (5,'订单管理',1,0);
insert into t_menu (id,name,level,pid) value (6,'数据统计',1,0);
insert into t_menu (id,name,level,pid,path) value (21,'用户列表',2,2,'/user_list');
insert into t_menu (id,name,level,pid,path) value (31,'角色列表',2,3,'/author_list');
insert into t_menu (id,name,level,pid,path) value (32,'权限列表',2,3,'/role_list');
insert into t_menu (id,name,level,pid,path) value (41,'商品列表',2,4,'/product_list');
insert into t_menu (id,name,level,pid,path) value (42,'分类列表',2,4,'/group_list');
insert into t_user (id,name,pwd,nick_name) value (2,'li','pbkdf2:sha256:150000$XE0SHgGr$d1','Jack');
insert into t_user (id,name,pwd,nick_name) value (3,'wang','pbkdf2:sha256:150000$XE0SHgGr$d1','Mark');
insert into t_user (id,name,pwd,nick_name) value (4,'chen','pbkdf2:sha256:150000$XE0SHgGr$d1','John');
insert into t_user (id,name,pwd,nick_name) value (5,'zhou','pbkdf2:sha256:150000$XE0SHgGr$d1','David');
insert into t_user (id,name,pwd,nick_name) value (6,'zhang','pbkdf2:sha256:150000$XE0SHgGr$d1','Tom');