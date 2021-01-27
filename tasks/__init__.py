from invoke import Collection

from tasks import (
    build,
    config,
    linting,
)

ns = Collection()

config = Collection.from_module(config, name="config")
linting = Collection.from_module(linting, name="lint")

# Subtasks
ns.add_collection(config)
ns.add_collection(linting)

# Tasks
ns.add_task(build.black)
ns.add_task(build.hass)
ns.add_task(build.hass_docker)
ns.add_task(build.clean)
ns.add_task(build.isort)
