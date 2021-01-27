import os

from invoke import task


# PATH STUFF
PROJECT_ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
HASS_CONFIG_PATH = os.path.join(PROJECT_ROOT_PATH, '.hass')
SOURCE_PATH = os.path.join(PROJECT_ROOT_PATH, 'custom_components/ferienapidotde')
TASKS_PATH = os.path.join(PROJECT_ROOT_PATH, 'tasks')


@task(default=True)
def config(ctx):
    """Shows the general configuration."""
    for k, v in globals().items():
        if k.endswith("_PATH"):
            print(k.ljust(20), v)
