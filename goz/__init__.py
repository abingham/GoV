import ledger
from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    journal_file = settings['ledger_file']
    journal = ledger.read_journal(journal_file)

    config = Configurator(settings=settings)

    config.add_request_method(lambda _: journal,
                              'journal',
                              reify=True)

    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('transactions', '/api/transactions')
    config.add_route('transaction',  '/api/transactions/:id')
    config.scan()
    return config.make_wsgi_app()
