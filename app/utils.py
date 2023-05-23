from django.templatetags.static import static
from urllib.parse import urlparse
from django.conf import settings
import os

def fetch_resources(uri, rel):
    """
    Callback function for resolving external links and resources.
    """
    # Handle URLs starting with "static/"
    if uri.startswith("static/"):
        path = os.path.join(settings.STATIC_ROOT, uri.replace("static/", ""))
        return path
    
    # Handle other URLs
    else:
        try:
            result = static(uri)
        except Exception as e:
            print(e)
            result = uri
        return result