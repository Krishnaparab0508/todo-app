from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Use BASE_DIR for database location
    }
}
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
DEBUG = True
ROOT_URLCONF = 'todo_project.urls'

INSTALLED_APPS = [
    'django.contrib.admin',          # Admin app
    'django.contrib.auth',           # Authentication
    'django.contrib.contenttypes',   # Content types framework
    'django.contrib.sessions',       # Session framework
    'django.contrib.messages',       # Messaging framework
    'django.contrib.staticfiles',    # Static files handling
    'rest_framework',                # Django Rest Framework (for APIs)
    'todo_app',                      # Your custom app
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add directories here if you have custom templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Must come before AuthenticationMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Required for admin
    'django.contrib.messages.middleware.MessageMiddleware',  # Required for admin
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# URL to access static files
STATIC_URL = '/static/'

# Directory to collect static files during production
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Optional: Add your custom static files directory here
]

# Directory where Django will collect all static files
STATIC_ROOT = BASE_DIR / "staticfiles"

from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
SECRET_KEY = 'mz3^4%1n#+kjh8b*hj_oc*w5h72zeaf7!)6-ti)u-3984unns('
