import itertools

import pyramid.exceptions
from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/goz.mak')
def home(request):
    return {'project': 'goz'}


def _entry_to_json(entry):
    return {'id': id(entry),
            'date': str(entry.date)}


@view_config(route_name='transactions',
             request_method='GET',
             renderer='json')
def get_all_transactions(request):
    """Get a list of all transactions.
    """
    return list(map(_entry_to_json,
                    request.entries))


# @view_config(route_name='transaction',
#              request_method='GET',
#              renderer='json')
# def get_transaction(request):
#     xact_id = request.matchdict['id']

#     try:
#         return _transaction_to_json(next(
#             itertools.ifilter(lambda xact: xact.id() == xact_id,
#                               request.journal.xacts())))
#     except StopIteration:
#         raise pyramid.exceptions.NotFound(
#             'No transaction with ID={}'.format(xact_id))
