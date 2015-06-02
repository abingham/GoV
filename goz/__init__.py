from beancount.loader import load_file
from pyramid.config import Configurator

import goz.json_util

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    journal_file = settings['beancount_file']
    entries, errors, options = load_file(journal_file)

    config = Configurator(settings=settings)
    config.add_renderer('json', goz.json_util.make_json_renderer())
    config.add_request_method(lambda _: entries,
                              'entries',
                              reify=True)

    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('transactions', '/api/transactions')
    config.add_route('transaction',  '/api/transactions/:id')
    config.scan()
    return config.make_wsgi_app()
