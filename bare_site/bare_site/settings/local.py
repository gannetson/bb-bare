from .base import *
from .secrets import *


#
# Set up your local configurations below
#

# Send email to console by default
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#EMAIL_BACKEND = 'apps.bluebottle_utils.email_backend.DKIMBackend'