from invoke import task


from tasks.config import (
    HASS_CONFIG_PATH,
    SOURCE_PATH
)


@task
def clean(ctx):
    """Removes python build artifacts (*.pyc, *.pyo, caches, ...)"""
    ctx.run(
        "find . -type f -name '*.pyc' -delete && "
        "find . -type f -name '*.pyo' -delete && "
        "rm -rf .pytest_cache && "
        "rm -rf .mypy_cache"
    )


@task
def hass(ctx):
    """Run hass for testing."""
    ctx.run(
        f"hass -c {HASS_CONFIG_PATH}"
    )


@task
def hass_docker(ctx):
    """Runs home assistant in a docker container."""
    ctx.run(
        "docker-compose -f ./.dev-container/docker-compose.yaml up hass"
    )
    ctx.run(
        "docker-compose -f ./.dev-container/docker-compose.yaml down"
    )


@task
def isort(ctx):
    """Calls the isort tool to order the imports."""
    ctx.run(
        f"isort {SOURCE_PATH}"
    )


@task
def black(ctx):
    """Calls black to format the code."""
    ctx.run(
        f"black -l 79 -t py38 {SOURCE_PATH}"
    )
