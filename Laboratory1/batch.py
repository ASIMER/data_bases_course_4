from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from cassandra import ConsistencyLevel

cluster = Cluster()
session = cluster.connect("designsite")

query = SimpleStatement("""BEGIN BATCH
	INSERT INTO users(login, nickname, password, sites, premium, plan, country, occupation, user_styles)
	VALUES ('ASIMER', 'ASIMER', 'ASIMER', {'newsmy.com'}, NULL, NULL, 'Ukraine', 'student', {'ancient'});
	INSERT INTO styles(block_type, name, topics, popularity, premium, code, owner)
	VALUES ('footer', 'ancient', 'news', 929, False, '----', {'ASIMER'});
APPLY BATCH;""", consistency_level=ConsistencyLevel.ONE)
session.execute(query)
