from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/home.mak')
def home(request):
    return {'project': 'goz'}
