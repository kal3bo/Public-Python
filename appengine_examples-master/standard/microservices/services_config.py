import os

# To add services insert key value pair of the name of the service and
# the port you want it to run on when running locally
SERVICES = {
    'default': 8080,
    'backend': 8081
}


def init_app(app):
    # The GAE_INSTANCE environment variable will be set when deployed to GAE.
    gae_instance = os.environ.get(
        'GAE_INSTANCE', os.environ.get('GAE_MODULE_INSTANCE'))
    environment = 'production' if gae_instance is not None else 'development'
    app.config['SERVICE_MAP'] = map_services(environment)


def map_services(environment):
    """Generates a map of services to correct urls for running locally
    or when deployed."""
    url_map = {}
    for service, local_port in SERVICES.items():
        if environment == 'production':
            url_map[service] = production_url(service)
        if environment == 'development':
            url_map[service] = local_url(local_port)
    return url_map


def production_url(service_name):
    """Generates url for a service when deployed to App Engine."""
    project_id = os.environ.get('GOOGLE_CLOUD_PROJECT')
    project_url = '{}.appspot.com'.format(project_id)
    if service_name == 'default':
        return 'https://{}'.format(project_url)
    else:
        return 'https://{}-dot-{}'.format(service_name, project_url)


def local_url(port):
    """Generates url for a service when running locally"""
    return 'http://localhost:{}'.format(str(port))