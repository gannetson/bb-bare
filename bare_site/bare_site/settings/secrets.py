# Make this unique, and don't share it with anybody.
SECRET_KEY = 'i%hwus7x5_!*#=fqc_j^gxnt3i9t38cn0j-)xrusp1avd%9qb3'

# Database configuration.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bluebottle_bare',
        # The following settings are not used with sqlite3:
        'USER': 'jose',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}
