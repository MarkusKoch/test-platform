from platform.api.auth import protect
from platform.resources.main import MainResource


@protect
def get_resource():
    return MainResource()
