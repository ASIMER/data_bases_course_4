INSERT INTO users(login, nickname, password, sites, premium, plan, country, occupation, user_styles)
VALUES ('ASIMER', 'ASIMER', 'ASIMER', {'newsmy.com'}, NULL, NULL, 'Ukraine', 'student', {'ancient'});
INSERT INTO users(login, nickname, password, sites, premium, plan, country, occupation, user_styles)
VALUES ('Kelioris', 'Kelioris', 'Kelioris', {'newstest.com'}, '2020-09-1', 'econom', 'Russia', 'work', {'futuristic'});
INSERT INTO users(login, nickname, password, sites, premium, plan, country, occupation, user_styles)
VALUES ('Tereshchenko', 'Tereshchenko', 'Tereshchenko', {'coolnews.com'}, '2020-10-1', 'pro', 'Belarus', 'teacher', {'modern'});
SELECT * FROM users;

INSERT INTO topic_analitycs(topic_name, block_type, block_name, words, position, styles, popularity, paragraphs, focus_time, sentences, images)
VALUES ('comedy', 'div', 'news', 1245, 'center', {'futuristic'}, 154, 12, '0:1:13.878746', 14, 0.4);
INSERT INTO topic_analitycs(topic_name, block_type, block_name, words, position, styles, popularity, paragraphs, focus_time, sentences, images)
VALUES ('news', 'div', 'info', 452, 'left', {'modern'}, 332, 2, '0:0:23.369432', 6, 0.8);
INSERT INTO topic_analitycs(topic_name, block_type, block_name, words, position, styles, popularity, paragraphs, focus_time, sentences, images)
VALUES ('history', 'footer', 'copyright', 2245, 'bottom', {'ancient'}, 441, 16, '0:2:1.647847', 18, 0.4);
SELECT * FROM topic_analitycs;

INSERT INTO styles(block_type, name, topics, popularity, premium, code, owner)
VALUES ('footer', 'ancient', 'news', 929, False, '----', {'ASIMER'});
INSERT INTO styles(block_type, name, topics, popularity, premium, code, owner)
VALUES ('div', 'modern', 'news', 123, False, '----', {'Kelioris'});
INSERT INTO styles(block_type, name, topics, popularity, premium, code, owner)
VALUES ('div', 'futuristic', 'info', 914, False, '----', {'Tereshchenko'});
SELECT * FROM styles;

INSERT INTO generator(block_type, element_id, block_name, position, block_topics, block_style, code, source)
VALUES ('div', 'news_1', 'news', 'bottom', {'comedy'}, 'modern', '<h1>Today news</h1>', 'https://news.google.com/');
INSERT INTO generator(block_type, element_id, block_name, position, block_topics, block_style, code, source)
VALUES ('div', 'info_1', 'info', 'left', {'news'}, 'futuristic', '<h1>Most important heading here</h1>
    <h3>Less important heading here</h3>
    <p>Some additional information here</p>', '');
INSERT INTO generator(block_type, element_id, block_name, position, block_topics, block_style, code, source)
VALUES ('footer', 'copyright_1', 'copyright', 'footer', {'history'}, 'ancient', '<p>Posted by: Hege Refsnes</p>
  <p>Contact information: <a href="mailto:someone@example.com">
  someone@example.com</a>.</p>', '');
SELECT * FROM generator;

INSERT INTO sites(site_name, site_adress, owner)
VALUES ('Good news', 'newsmy.com', {'ASIMER'});
INSERT INTO sites(site_name, site_adress, owner)
VALUES ('Bad news', 'newstest.com', {'Kelioris'});
INSERT INTO sites(site_name, site_adress, owner)
VALUES ('Cool news', 'coolnews.com', {'Tereshchenko'});
SELECT * FROM sites;


UPDATE users
SET password = '22121s'
WHERE nickname = 'ASIMER' AND login = 'ASIMER';
UPDATE users
SET password = '312aa'
WHERE nickname = 'Kelioris' AND login = 'Kelioris';
UPDATE users
SET password = '123123aas'
WHERE nickname = 'Tereshchenko' AND login = 'Tereshchenko';
SELECT * FROM users;

UPDATE topic_analitycs
SET popularity = 21314
WHERE topic_name = 'comedy' AND block_name = 'news' AND block_type = 'div' AND words = 1245 AND position = 'center';
UPDATE topic_analitycs
SET popularity = 215112
WHERE topic_name = 'news' AND block_name = 'info' AND block_type = 'div' AND words = 452 AND position = 'left';
UPDATE topic_analitycs
SET popularity = 51223
WHERE topic_name = 'history' AND block_name = 'copyright' AND block_type = 'footer' AND words = 2245 AND position = 'bottom';
SELECT * FROM topic_analitycs;

UPDATE styles
SET popularity = 21314
WHERE name = 'ancient' AND block_type = 'footer';
UPDATE styles
SET popularity = 215112
WHERE name = 'modern' AND block_type = 'div';
UPDATE styles
SET popularity = 51223
WHERE name = 'futuristic' AND block_type = 'div';
SELECT * FROM styles;

UPDATE generator
SET source = 'https://www.bing.com/news'
WHERE element_id = 'news_1' AND block_type = 'div' AND block_name = 'news';
UPDATE generator
SET source = 'https://news.google.com/'
WHERE element_id = 'info_1' AND block_type = 'div' AND block_name = 'info';
UPDATE generator
SET source = 'https://www.bing.com/news'
WHERE element_id = 'copyright_1' AND block_type = 'footer' AND block_name = 'copyright';
SELECT * FROM generator;

UPDATE sites
SET owner = owner + {'Tereshchenko'}
WHERE site_adress = 'newsmy.com' AND site_name = 'Good news';
UPDATE sites
SET owner = owner + {'Tereshchenko'}
WHERE site_adress = 'newstest.com' AND site_name = 'Bad news';
UPDATE sites
SET owner = owner + {'ASIMER'}
WHERE site_adress = 'coolnews.com' AND site_name = 'Cool news';
SELECT * FROM sites;



SELECT nickname, premium
FROM users;

SELECT topic_name, block_name, position, popularity
FROM topic_analitycs;

SELECT name, block_type
FROM styles;

SELECT block_name, code
FROM generator;

SELECT site_adress, site_name, path
FROM sites;



DELETE country FROM users
WHERE nickname = 'ASIMER' AND login = 'ASIMER';
DELETE country FROM users
WHERE nickname = 'Kelioris' AND login = 'Kelioris';
DELETE country FROM users
WHERE nickname = 'askorbinka' AND login = 'askorbinka';
SELECT * FROM users;

DELETE paragraphs FROM topic_analitycs
WHERE topic_name = 'comedy' AND block_name = 'news' AND block_type = 'div' AND words = 1245 AND position = 'center';
DELETE paragraphs FROM topic_analitycs
WHERE topic_name = 'news' AND block_name = 'info' AND block_type = 'div' AND words = 452 AND position = 'left';
DELETE paragraphs FROM topic_analitycs
WHERE topic_name = 'history' AND block_name = 'copyright' AND block_type = 'footer' AND words = 2245 AND position = 'bottom';
SELECT * FROM topic_analitycs;

DELETE popularity FROM styles
WHERE name = 'ancient' AND block_type = 'footer';
DELETE popularity FROM Styles
WHERE name = 'modern' AND block_type = 'div';
DELETE popularity FROM Styles
WHERE name = 'futuristic' AND block_type = 'div';
SELECT * FROM styles;

DELETE source FROM generator
WHERE element_id = 'news_1' AND block_type = 'div' AND block_name = 'news';
DELETE source FROM generator
WHERE element_id = 'info_1' AND block_type = 'div' AND block_name = 'info';
DELETE source FROM generator
WHERE element_id = 'copyright_1' AND block_type = 'footer' AND block_name = 'copyright';
SELECT * FROM Generator;

DELETE path FROM sites
WHERE site_adress = 'newsmy.com' AND site_name = 'Good news';
DELETE path FROM sites
WHERE site_adress = 'newstest.com' AND site_name = 'Bad news';
DELETE path FROM sites
WHERE site_adress = 'coolnews.com' AND site_name = 'Cool news';
SELECT * FROM Generator;