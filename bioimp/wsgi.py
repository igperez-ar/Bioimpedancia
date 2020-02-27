
import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bioimp.settings.prod')
sys.path.append('/home/mgel/Bioimpedancia')
sys.path.append('/home/mgel/Bioimpedancia/bioimp')
application = get_wsgi_application()
#SECRET_KEY = os.environ.get("SECRET_KEY", "some value if your key is not in the environment")

