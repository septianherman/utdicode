from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'],port=9042)
session = cluster.connect()

rows = session.execute("SELECT release_version FROM system.local").one()
if rows:
    print(rows[0])
    