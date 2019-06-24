# Django sandbox

## setup

1. virtualenv
    ```
    python3 -m venv venv
    . venv/bin/activate
    ```

1. install packages
    ```
    pip install django
    ```

1. local settings
    ```
    cat <<__EOF__ > local_settings.py
    ALLOWED_HOSTS = ['YOUR_DEBUG_SERVER']
    EMAIL_HOST = 'xxx.xxx.xxx.xxx'
    EMAIL_PORT = 2525
    EMAIL_HOST_USER = 'xxxxxxxxxxxxxxx'
    EMAIL_HOST_PASSWORD = 'xxxxxxxxxxxxxxx'
    __EOF__
    ```

1. initalize
    ```
    python manage.py createcachetable
    python manage.py migrate
    python manage.py createsuperuser # ID, e-Mail, password
    ```

1. start debug server
    ```
    python manage.py runserver 0.0.0.0:8000
    ```
    
