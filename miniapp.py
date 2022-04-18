import bottle
import random
import string
from beaker.middleware import SessionMiddleware


session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}

app = SessionMiddleware(bottle.app(), session_opts)


def unique_name():
	n = 23
	rand_chrs = [random.choice(string.ascii_uppercase + string.digits) for i in range(n)]
	return ''.join(rand_chrs)


@bottle.route('/')
def test():
	s = bottle.request.environ.get('beaker.session')
	if 'uu_name' not in s:
		s['uu_name'] = s.get('uu_name',unique_name())
	else:
		s['uu_name'] = unique_name()
	s.save()

	return 'The unique name: %s' % s['uu_name']

bottle.run(app=app)
