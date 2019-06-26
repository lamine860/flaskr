drop table if exists entries;
create table entries (
    id integer primary key autoincrement,
    title text not null,
    'text' text not null
);


drop table if exists user;
create table user (
    int integer primary key autoincrement,
    username varchar not null,
    'password' varchar not null
);