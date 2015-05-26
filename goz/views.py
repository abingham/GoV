import itertools

import pyramid.exceptions
from pyramid.view import view_config


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
    return map(_transaction_to_json,
               request.journal.xacts())


@view_config(route_name='transaction',
             request_method='GET',
             renderer='json')
def get_transaction(request):
    xact_id = request.matchdict['id']

    try:
        return _transaction_to_json(next(
            itertools.ifilter(lambda xact: xact.id() == xact_id,
                              request.journal.xacts())))
    except StopIteration:
        raise pyramid.exceptions.NotFound(
            'No transaction with ID={}'.format(xact_id))
