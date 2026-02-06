create table if not exists links(
	id integer primary key autoincrement,
	url text not null,
	added_at timestamp default current_timestamp,
	is_live boolean);

create table if not exists pages(
	id integer PRIMARY KEY,
	url text not null,
	retrieved_at timestamp default current_timestamp,
	content text);
