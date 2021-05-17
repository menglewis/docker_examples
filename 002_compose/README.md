### Docker Compose

Useful for configuring a dev environment for multiple Docker containers or even a single Docker container if it has a lot of arguments.

Configured using a yaml file that specifies the containers that should be run.

`docker-compose.yml`

Running `docker-compose up` in the directory that contains a `docker-compose.yml` file will automatically use that file. `-f` can be used to specify the path to a `docker-compose.yml` file.

`docker-compose up -d` will bring up the containers and then run them in the background.

`docker-compose ps` will show the Docker containers and their current status. Useful for debugging if all of the containers are running properly.

`docker-compose logs web` will show the logs for the web container.

`docker-compose exec` is used for running arbitrary commands against the containers.

`docker-compose exec web bash` will run a bash shell on the web container.

`docker-compose exec db psql -U dev -d tutorial` will run `psql` on the db container.
