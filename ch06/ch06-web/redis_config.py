from redis import Redis

redis_conn = Redis(db = 0, host='127.0.0.1', port=6379,
    decode_responses=True # <-- this will ensure that binary data is decoded
)