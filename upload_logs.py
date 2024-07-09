import redis

# Connect to Redis Client
hostname = 'redis-11784.c322.us-east-1-2.ec2.redns.redis-cloud.com'
portnumber = 11784
password = 'h2bJd4iojfo9E7DJ4z6c0XGFNW2bCJ9r'

r = redis.StrictRedis(host=hostname,
                      port=portnumber,
                      password=password)

# Simulated Logs
with open('simulated_logs.txt', 'r') as f:
    logs_text = f.read()

encoded_logs = logs_text.split('\n')

# Push into Redis database
r.lpush('attendance:logs', *encoded_logs)
