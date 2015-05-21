import itertools

import pyramid.exceptions
from pyramid.view import view_config

import ledger


@view_config(route_name='home', renderer='templates/goz.mak')
def home(request):
    return {'project': 'goz'}


def _transaction_to_json(transaction):
    return {'id': transaction.id(),
            'payee': transaction.payee}


@view_config(route_name='transactions',
             request_method='GET',
             renderer='json')
def get_all_transactions(request):
    """Get a list of all transactions.
    """
    # TODO: We should keep the journal open the entire time, I think.

    journal_file = request.registry.settings['ledger_file']
    journal = ledger.read_journal(journal_file)

    try:
        return map(_transaction_to_json,
                   journal.xacts())
    finally:
        ledger.session.close_journal_files()


@view_config(route_name='transaction',
             request_method='GET',
             renderer='json')
def get_transaction(request):
    xact_id = request.matchdict['id']

    journal_file = request.registry.settings['ledger_file']
    journal = ledger.read_journal(journal_file)

    try:
        return _transaction_to_json(next(
            itertools.ifilter(lambda xact: xact.id() == xact_id,
                              journal.xacts())))
    except StopIteration:
        raise pyramid.exceptions.NotFound(
            'No transaction with ID={}'.format(xact_id))
    finally:
        ledger.session.close_journal_files()
