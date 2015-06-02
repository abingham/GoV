import beancount
from pyramid.view import view_config

from goz.json_util import transaction_to_json


@view_config(route_name='home', renderer='templates/goz.mak')
def home(request):
    return {'project': 'goz'}


@view_config(route_name='transactions',
             request_method='GET',
             renderer='json')
def get_all_transactions(request):
    """Get a list of all transactions.
    """

    entries = list(map(
        transaction_to_json,
        filter(lambda e: isinstance(e, beancount.core.data.Transaction),
               request.entries)))

    return entries


# @view_config(route_name='transaction',
#              request_method='GET',json
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

# @view_config(route_name='accounts',
#              request_method='GET',
#              renderer='json')
# def
