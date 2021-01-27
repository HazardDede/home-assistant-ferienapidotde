from invoke import task

from tasks.config import (
    SOURCE_PATH
)


@task
def flake8(ctx):
    """Runs flake8 linter against codebase."""
    ctx.run("flake8 "
            "--max-line-length 79 "
            "{}".format(SOURCE_PATH))


@task
def pylint(ctx):
    """Runs pylint linter against codebase."""
    ctx.run("pylint {}".format(SOURCE_PATH))


@task(flake8, pylint, default=True)
def lint(ctx):
    """Run all configured linters against the codebase."""
