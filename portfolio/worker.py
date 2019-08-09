import os
import redis

from rq import Worker, Queue, Connection

redis_url = os.getenv('REDISTOGO_URL', 'redis://redis:6379/0')

conn = redis.from_url(redis_url)

listen = ['default']

print("Worker is running!")

# with Connection(conn):
#     worker = Worker(map(Queue, listen))
#     worker.work()
#     del conn

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
