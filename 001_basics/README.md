
To build a Docker image locally

`docker build -t local-image .`

View Docker Images that are saved on your computer

`docker images`

View Currently running Docker Images
`docker ps`

Run a Docker image
`docker run local-image`

Run an interactive Terminal in your Docker container
`docker run -it --rm local-image /bin/bash`

The `-it` is magic required to have an interactive session.

The `--rm` cleans up the container and file system after exiting from the container.

The `/bin/bash` overrides the command on the Docker image so it runs bash instead of flask.
