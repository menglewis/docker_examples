
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

The `-it` enables an interactive session. The `-i` keeps stdin open and the `-t` creates a pseudo-terminal. Using these together enables the user to send input to the container.

The `--rm` cleans up the container and file system after exiting from the container.

The `/bin/bash` overrides the command on the Docker image so it runs bash instead of flask.

To map a port from the host machine to the Docker container use the `-p` argument

`-p 5000:5000`

To mount a volume from your filesystem to the Docker container use the `-v` argument.

`-v $(pwd):/src`

Here `$(pwd)` is getting my current directory and mounting that to `/src` in the Docker container.

Final command:

`docker run -it --rm -p 5000:5000 -v $(pwd):/src local-image`
