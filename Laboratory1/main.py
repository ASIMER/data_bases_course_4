from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from cassandra import ConsistencyLevel

cluster = Cluster()
session = cluster.connect("designsite")  # or designsite

query = SimpleStatement("""INSERT INTO users (login, nickname, password, sites, premium, plan, country, occupation, user_styles)
VALUES (%s, %s, %s, {%s}, %s, %s, %s, %s, {%s});""", consistency_level=ConsistencyLevel.ONE)
session.execute(query, ('ASIMER', 'ASIMER', 'ASIMER', 'newsmy.com', None, None, 'Ukraine', 'student', 'ancient'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('Kelioris', 'Kelioris', 'Kelioris', 'newstest.com', '2020-09-1', 'econom', 'Russia', 'work', 'futuristic'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('Tereshchenko', 'Tereshchenko', 'Tereshchenko', 'coolnews.com', '2020-10-1', 'pro', 'Belarus', 'teacher', 'modern'))
query.consistency_level = ConsistencyLevel.ONE
rows = session.execute("SELECT * FROM users;")
for row in rows:
    print(row)

query = SimpleStatement("""INSERT INTO topic_analitycs(topic_name, block_type, block_name, words, position, styles, popularity, paragraphs, focus_time, sentences, images)
VALUES (%s, %s, %s, %s, %s, {%s}, %s, %s, %s, %s, %s);""", consistency_level=ConsistencyLevel.ONE)
session.execute(query, ('comedy', 'div', 'news', 1245, 'center', 'futuristic', 154, 12, '0:1:13.878746', 14, 0.4))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('news', 'div', 'info', 452, 'left', 'modern', 332, 2, '0:0:23.369432', 6, 0.8))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('history', 'footer', 'copyright', 2245, 'bottom', 'ancient', 441, 16, '0:2:1.647847', 18, 0.4))
query.consistency_level = ConsistencyLevel.ONE
rows = session.execute("SELECT * FROM topic_analitycs;")
for row in rows:
    print(row)

query = SimpleStatement("""INSERT INTO styles (block_type, name, topics, popularity, premium, code, owner)
VALUES (%s, %s, %s, %s, %s, %s, {%s});""",
                        consistency_level=ConsistencyLevel.ONE)
session.execute(query, ('footer', 'ancient', 'news', 929, False, '----', 'ASIMER'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('div', 'modern', 'news', 123, False, '----', 'Kelioris'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('div', 'futuristic', 'info', 914, False, '----', 'Tereshchenko'))
query.consistency_level = ConsistencyLevel.ONE
rows = session.execute("SELECT * FROM styles;")
for row in rows:
    print(row)

query = SimpleStatement("""INSERT INTO generator(block_type, element_id, block_name, position, block_topics, block_style, code, source)
VALUES (%s, %s, %s,%s, {%s}, %s, %s, %s);""",
                        consistency_level=ConsistencyLevel.ONE)
session.execute(query, ('div', 'news_1', 'news', 'bottom', 'comedy', 'modern', '<h1>Today news</h1>', 'https://news.google.com/'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('div', 'info_1', 'info', 'left', 'news', 'futuristic', '<h1>Most important heading here</h1>\n<h3>Less important heading here</h3>\n<p>Some additional information here</p>', ''))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('footer', 'copyright_1', 'copyright', 'footer', 'history', 'ancient', '<p>Posted by: Hege Refsnes</p>\n<p>Contact information: <a href="mailto:someone@example.com">\nsomeone@example.com</a>.</p>', ''))
query.consistency_level = ConsistencyLevel.ONE
rows = session.execute("SELECT * FROM generator;")
for row in rows:
    print(row)

query = SimpleStatement("""INSERT INTO sites(site_name, site_adress, owner)
VALUES (%s, %s, {%s});""",
                        consistency_level=ConsistencyLevel.ONE)
session.execute(query, ('newsmy.com', 'Good news', 'ASIMER'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('newstest.com', 'Bad news', 'Kelioris'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('coolnews.com', 'Cool news', 'Tereshchenko'))
query.consistency_level = ConsistencyLevel.ONE
rows = session.execute("SELECT * FROM sites;")
for row in rows:
    print(row)


query = SimpleStatement("""UPDATE users
SET password = %s
WHERE nickname = %s AND login = %s;""", consistency_level=ConsistencyLevel.ONE)
session.execute(query, ('22121s', 'ASIMER', 'ASIMER'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('312aa', 'Kelioris', 'Kelioris'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('123123aas', 'Tereshchenko', 'Tereshchenko'))
query.consistency_level = ConsistencyLevel.ONE
rows = session.execute("SELECT * FROM users;")
for row in rows:
    print(row)

query = SimpleStatement("""UPDATE topic_analitycs
SET popularity = %s
WHERE topic_name = %s AND block_name = %s AND block_type = %s AND words = %s AND position = %s;""", consistency_level=ConsistencyLevel.ONE)
session.execute(query, (21314, 'comedy', 'news', 'div', 1245, 'center'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, (215112, 'news', 'info', 'div', 452, 'left'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, (51223, 'history', 'copyright', 'footer', 2245, 'bottom'))
query.consistency_level = ConsistencyLevel.ONE
rows = session.execute("SELECT * FROM topic_analitycs;")
for row in rows:
    print(row)

query = SimpleStatement("""UPDATE styles
SET popularity = %s
WHERE name = %s AND block_type = %s;""", consistency_level=ConsistencyLevel.ONE)
session.execute(query, (21314, 'ancient', 'footer'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, (215112, 'modern', 'div'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, (51223, 'futuristic', 'div'))
query.consistency_level = ConsistencyLevel.ONE
rows = session.execute("SELECT * FROM styles;")
for row in rows:
    print(row)

query = SimpleStatement("""UPDATE generator
SET source = %s
WHERE element_id = %s AND block_type = %s AND block_name = %s;""", consistency_level=ConsistencyLevel.ONE)
session.execute(query, ('https://www.bing.com/news', 'news_1', 'div', 'news'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('https://news.google.com/', 'info_1', 'div', 'info'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('https://www.bing.com/news', 'copyright_1', 'footer', 'copyright'))
query.consistency_level = ConsistencyLevel.ONE
rows = session.execute("SELECT * FROM generator;")
for row in rows:
    print(row)

query = SimpleStatement("""UPDATE sites
SET owner = owner + {%s}
WHERE site_adress = %s AND site_name = %s;""", consistency_level=ConsistencyLevel.ONE)
session.execute(query, ('Tereshchenko', 'newsmy.com', 'Good news'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('Tereshchenko', 'newstest.com', 'Bad news'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('ASIMER', 'coolnews.com', 'Cool news'))
query.consistency_level = ConsistencyLevel.ONE
rows = session.execute("SELECT * FROM generator;")
for row in rows:
    print(row)


rows = session.execute("""SELECT nickname, premium
FROM users;""")
for row in rows:
    print(row)
rows = session.execute("""SELECT topic_name, block_name, position, popularity
FROM topic_analitycs;""")
for row in rows:
    print(row)
rows = session.execute("""SELECT name, block_type
FROM styles;""")
for row in rows:
    print(row)
rows = session.execute("""SELECT block_name, code
FROM generator;""")
for row in rows:
    print(row)
rows = session.execute("""SELECT site_adress, site_name, path
FROM sites;""")
for row in rows:
    print(row)



query = SimpleStatement("""DELETE country FROM users
WHERE nickname = %s AND login = %s;""", consistency_level=ConsistencyLevel.ONE)
session.execute(query, ('ASIMER', 'ASIMER'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('Kelioris', 'Kelioris'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('Tereshchenko', 'Tereshchenko'))
query.consistency_level = ConsistencyLevel.ONE
rows = session.execute("SELECT * FROM users;")
for row in rows:
    print(row)

query = SimpleStatement("""DELETE paragraphs FROM topic_analitycs
WHERE topic_name = %s AND block_name = %s AND block_type = %s AND words = %s AND position = %s;""", consistency_level=ConsistencyLevel.ONE)
session.execute(query, ('comedy', 'news', 'div', 1245, 'center'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('news', 'info', 'div', 452, 'left'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('history', 'copyright', 'footer', 2245, 'bottom'))
query.consistency_level = ConsistencyLevel.ONE
rows = session.execute("SELECT * FROM topic_analitycs;")
for row in rows:
    print(row)

query = SimpleStatement("""DELETE popularity FROM styles
WHERE name = %s AND block_type = %s;""", consistency_level=ConsistencyLevel.ONE)
session.execute(query, ('ancient', 'footer'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('modern', 'div'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('futuristic', 'div'))
query.consistency_level = ConsistencyLevel.ONE
rows = session.execute("SELECT * FROM styles;")
for row in rows:
    print(row)

query = SimpleStatement("""DELETE source FROM generator
WHERE element_id = %s AND block_type = %s AND block_name = %s;""", consistency_level=ConsistencyLevel.ONE)
session.execute(query, ('news_1', 'div', 'news'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('info_1', 'div', 'info'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('copyright_1', 'footer', 'copyright'))
query.consistency_level = ConsistencyLevel.ONE
rows = session.execute("SELECT * FROM generator;")
for row in rows:
    print(row)

query = SimpleStatement("""DELETE path FROM sites
WHERE site_adress = %s and site_name = %s;""", consistency_level=ConsistencyLevel.ONE)
session.execute(query, ('newsmy.com', 'Good news'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('newstest.com', 'Bad news'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('coolnews.com', 'Cool news'))
query.consistency_level = ConsistencyLevel.ONE
rows = session.execute("SELECT * FROM generator;")
for row in rows:
    print(row)