import datetime
import decimal

import beancount
from pyramid.renderers import JSON


def posting_to_json(posting):
    simple = ['account', 'flag', 'meta']
    rslt = {n: getattr(posting, n) for n in simple}
    rslt['position'] = str(posting.position)
    rslt['price'] = str(posting.price)
    return rslt


def transaction_to_json(xact):
    # tags, postings
    simple = ['meta', 'flag', 'payee', 'narration', 'links', 'date']
    rslt = {n: getattr(xact, n) for n in simple}

    rslt['postings'] = list(map(posting_to_json, xact.postings))

    if xact.tags is not None:
        rslt['tags'] = list(xact.tags)

    # TODO: Using id() like this is probably wrong. What does bean-web do?
    rslt['id'] = id(xact)
    return rslt


def _date_adapter(obj, request):
    return obj.isoformat()


def _decimal_adapter(obj, request):
    return str(obj)


def make_json_renderer():
    json_renderer = JSON()

    json_renderer.add_adapter(datetime.date,
                              _date_adapter)
    json_renderer.add_adapter(decimal.Decimal,
                              _decimal_adapter)
    return json_renderer
