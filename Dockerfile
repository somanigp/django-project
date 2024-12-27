# # django will be installed in python environment.

# Set the python version as a build-time argument
# with Python 3.12 as the default. Can be changed during docker build.
# docker build --build-arg PYTHON_VERSION=3.9-slim-buster -t my-django-app .
ARG PYTHON_VERSION=3.12-slim-bullseye
FROM python:${PYTHON_VERSION}

# Create a virtual environment. /opt/venv: This is the directory where the virtual environment will be created. /opt is a standard directory on Linux systems for optional or third-party software.
RUN python -m venv /opt/venv

# Set the virtual environment as the current location. The PATH variable specifies the directories where the operating system searches for executable files when you run a command without providing the full path.
# After creating the virtual environment at /opt/venv, this ensures that when you run commands like python or pip inside the container, the versions within the virtual environment are used first, instead of any system-wide Python installations. This keeps your project's dependencies isolated and prevents conflicts.
# If the original PATH was /usr/local/bin:/usr/bin:/bin, after this command, the new PATH will be /opt/venv/bin:/usr/local/bin:/usr/bin:/bin. 
ENV PATH=/opt/venv/bin:$PATH

# Upgrade pip
RUN pip install --upgrade pip

# Set Python-related environment variables
# This prevents Python from writing .pyc files (compiled bytecode). .pyc files are normally used for optimization, but they can sometimes cause issues in containerized environments
ENV PYTHONDONTWRITEBYTECODE 1  
# This forces Python to buffer output less. Normally, output might be buffered (held temporarily in memory) before being written to the terminal or a file. 
ENV PYTHONUNBUFFERED 1

# Install os dependencies for our mini vm
RUN apt-get update && apt-get install -y \
    # for postgres
    libpq-dev \
    # for Pillow
    libjpeg-dev \
    # for CairoSVG
    libcairo2 \
    # other
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Create the mini vm's code directory
RUN mkdir -p /code

# Set the working directory to that same code directory
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /tmp/requirements.txt

# copy the project code into the container's working directory
COPY ./src /code

# Install the Python project requirements
RUN pip install -r /tmp/requirements.txt

# database isn't available during build
# run any other commands that do not need the database
# such as:
# RUN python manage.py collectstatic --noinput

# set the Django default project name
ARG PROJ_NAME="somanigp"

# create a bash script to run the Django project
# this script will execute at runtime when
# the container starts and the database is available
# PORT:-8000. If PORT is not set, use 8000
RUN printf "#!/bin/bash\n" > ./paracord_runner.sh && \
    printf "RUN_PORT=\"\${PORT:-8000}\"\n\n" >> ./paracord_runner.sh && \
    printf "python manage.py migrate --no-input\n" >> ./paracord_runner.sh && \
    printf "gunicorn ${PROJ_NAME}.wsgi:application --bind \"0.0.0.0:\$RUN_PORT\"\n" >> ./paracord_runner.sh

# make the bash script executable
RUN chmod +x paracord_runner.sh

# Clean up apt cache to reduce image size
RUN apt-get remove --purge -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Run the Django project via the runtime script
# when the container starts
CMD ./paracord_runner.sh