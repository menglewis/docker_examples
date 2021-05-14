FROM python:3.9.5

# Sets the working directory. Commands that follow will use that directory.
WORKDIR /src

# Copy the contents from . to /src
COPY . /src

# Run a specified command
RUN pip install -r requirements.txt

# Set an environment variable
ENV FLASK_APP=/src/app.py
ENV FLASK_ENV=development

### Everything above here runs at build time
### Everything below here runs at run time

# Set the command for the Docker image
CMD flask run --host=0.0.0.0
