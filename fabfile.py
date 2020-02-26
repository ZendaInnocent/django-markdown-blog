from fabric.api import cd, env, local, run
from fabric.colors import red, green
import time
from pprint import pprint
from fabric.contrib.files import exists, append


REPO_URL = 'https://github.com/ZendaInnocent/personal-blog.git'

def deploy():
    site_folder = '/home/zendainn/django-markdown-blog/'
    
    with cd(site_folder):
        _get_latest_source()
        

def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git clone {REPO_URL} .')