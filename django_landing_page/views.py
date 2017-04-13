import logging

from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
import os

class WebsiteAppView(View):
    """
    Serves the compiled frontend entry point (only works if you have run `yarn
    run build`).
    """

    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except Exception:
            logging.exception('Production build of app not found')
            return HttpResponse(
                """
                <h1>
                This URL is only used when you have built the production
                version of the app. Visit http://localhost:3000/ instead, or
                run `yarn run build` to test the production version.
                </h1>
                """,
                status=501,
            )
