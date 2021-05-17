FROM python:3.9.5

# Sets the working directory. Commands that follow will use that directory.
WORKDIR /src

COPY ./app/requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt

# Copy the contents from ./app to /src
COPY ./app /src

# Set an environment variable
ENV FLASK_APP=/src/app.py
ENV FLASK_ENV=development

# Expose a port 
EXPOSE 5000

### Everything above here runs at build time
### Everything below here runs at run time

# Set the command for the Docker image
CMD flask run --host=0.0.0.0
