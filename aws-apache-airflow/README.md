# About aws-mwaa-local-runner

This repository provides a command line interface (CLI) utility that replicates an Amazon Managed Workflows for Apache Airflow (MWAA) environment locally.

## About the CLI

The CLI builds a Docker container image locally that’s similar to a MWAA production image. This allows you to run a local Apache Airflow environment to develop and test DAGs, custom plugins, and dependencies before deploying to MWAA.

## What this repo contains

```text
dags/
  requirements.txt
  tutorial.py
docker/
  .gitignore
  mwaa-local-env
  README.md
  config/
    airflow.cfg
    constraints.txt
    requirements.txt
    webserver_config.py
  script/
    bootstrap.sh
    entrypoint.sh
  docker-compose-dbonly.yml
  docker-compose-local.yml
  docker-compose-sequential.yml
  Dockerfile
```

