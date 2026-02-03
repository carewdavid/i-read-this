create table if not exists links(
id integer primary key autoincrement,
url text not null,
added_at default current_timestamp);
