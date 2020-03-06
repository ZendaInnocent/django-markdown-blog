from fabric.api import *
from fabric.contrib.files import append, exists
import random
from decouple import config

# Fabric file for automating tasks in shared host.
# If not in shared host, some folder path change them accordingly.

REPO_URL = config('REPO_URL')
user = config('USER')
folder = config('WORKING_FOLDER')
loca_git_folder = config('LOCAL_GIT_FOLDER')

def deploy():

    _local_git()

    site_folder = f'/home/{user}/{folder}/'

    if exists(site_folder):
        with cd(site_folder):
            _get_latest_source()
            _update_virtualenv()
            _update_static_files()
            _udpate_database()
            _create_or_update_dotenv()
    else:
        run(f'mkdir -p {site_folder}')

def _local_git():
    print('Performing Local git operations')
    print()

    with lcd(loca_git_folder):
        local('git push origin master')


def _get_latest_source():
    print('Getting the latest source.')
    print()

    if exists('.git'):
        run(f'git pull origin master')
    else:
        run(f'git clone {REPO_URL}')


def _update_virtualenv():
    print('Updating Virtual Environment.')
    print()

    run(f'/home/{user}/virtualenv/{folder}/3.7/bin/pip install -r requirements.txt')

def _update_static_files():
    print('Updating static files.')
    print()

    run(f'/home/{user}/virtualenv/{folder}/3.7/bin/python manage.py collectstatic --noinput')


def _udpate_database():
    print('Updating the database')
    print()

    run(f'/home/{user}/virtualenv/{folder}/3.7/bin/python manage.py migrate --noinput')

def _create_or_update_dotenv():
    print('Updating dotenv')
    print()

    append('.env', 'DEBUG=False')

    current_contents = run('cat .env')

    if 'DJANGO_SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices(
            'abcdefghijklmnopqrstuvwxyz0123456789', k=50
        ))
        append('.env', f'DJANGO_SECRET_KEY={new_secret}')