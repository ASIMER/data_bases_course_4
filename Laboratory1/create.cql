CREATE KEYSPACE IF NOT EXISTS designsite
WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 3};

CREATE TABLE IF NOT EXISTS users(
	login text,
	nickname text,
	password text,
	sites set<text>,
	premium date,
	plan text,
	country text,
	occupation text,
	user_styles set<text>,
	user_blocks set<text>,
	PRIMARY KEY((login), nickname)
);

CREATE TABLE IF NOT EXISTS topic_analitycs(
	topic_name text,
	block_type text,
	block_name text,
	words int,
	position text,
	styles set<text>,
	popularity int,
	paragraphs int,
	focus_time time,
	sentences int,
	images float,
	PRIMARY KEY((topic_name, block_type), block_name, words, position)
);

CREATE TABLE IF NOT EXISTS styles(
	block_type text,
	name text,
	topics text,
	popularity date,
	premium boolean,
	code text,
	owner set<text>,
	PRIMARY KEY((block_type), name)
);

CREATE TABLE IF NOT EXISTS generator(
	block_type text,
	element_id text,
	block_name text,
	position text,
	block_topics set<text>,
	block_style text,
	code text,
	source text,
	PRIMARY KEY((block_type), element_id, block_name)
);

CREATE TABLE IF NOT EXISTS sites(
	site_name text,
	site_adress text,
	owner set<text>,
	element_id set<text>,
	"index" text,
	path text,
	PRIMARY KEY((site_name), site_adress)
);