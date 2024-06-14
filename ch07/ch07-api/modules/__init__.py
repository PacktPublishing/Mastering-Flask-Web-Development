from flask import Flask
import toml
import redis
from cassandra.cqlengine.connection import setup
from mongoengine.connection import connect
import happybase

from datetime import timedelta

# needed for any cluster connection
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
# needed for options -- cluster, timeout, SQL++ (N1QL) query, etc.
from couchbase.options import ClusterOptions


def create_app(config_file):

    app = Flask(__name__)   
    app.config.from_file(config_file, toml.load)

    # Cassandra configuration
    setup(['127.0.0.1'], "packtspace", protocol_version=4)
    
    # Redis configuration
    redis.Redis.from_url("redis://localhost:6379/0", encoding="utf8",
                            decode_responses=True)
    # MongoDb configuration
    connect(host='localhost', port=27017, db='tfs', uuidRepresentation='standard') 
    
    # Hbase configuration
    global pool
    pool = happybase.ConnectionPool(size=5, host='localhost', port=9090)
    
    # Couchbase configuration
    # 1. Connect options - authentication
    auth = PasswordAuthenticator("sjctrags", "packt2255",)
    
    # 2. Get a reference to our cluster
    # NOTE: For TLS/SSL connection use 'couchbases://<your-ip-address>' instead
    cluster = Cluster('couchbase://localhost', ClusterOptions(auth))
    # 3. Wait until the cluster is ready for use.
    cluster.wait_until_ready(timedelta(seconds=5))
    # 4. Get a reference to our bucket
    global cb
    cb = cluster.bucket("packtbucket")
     
    with app.app_context():
        #import modules.api.couchbase.direct_messages
       
        import modules.api.mongo.tutor_savings
        import modules.api.mongo.tutor_profile
        import modules.api.mongo.tutor_login
        import modules.api.cassandra.students
        import modules.api.cassandra.courses
        import modules.api.hbase.payments
        import modules.api.hbase.bookings
        import modules.api.redis.search_course
        
    return app