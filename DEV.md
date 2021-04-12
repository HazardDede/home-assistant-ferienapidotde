# Development Guidelines

## Before creating a new version in Github

Please check the `custom_components/ferienapidotde/manifest.json` before a new version is created via Github. You need to adjust the `version` key to match the version you are going to create.

## Using the development docker container

```bash
cd .dev-container
docker-compose up
# Check if everything is running
# Navigate to (User/pw -> admin/admin):
#   http://localhost:8123
# Ctrl+C out of it when you are done
```
