import redis

rd = redis.Redis(password='Z2EPRqdpKQkjnhCeCxy1',
                 username='default',
                 port=6638,
                 host='containers-us-west-135.railway.app')
print(rd.set('pars','echo'))