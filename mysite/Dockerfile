FROM python:3.11.9

# Set the working directory to the Django app directory
WORKDIR /myapp

# Copy all project files to the working directory in the container
COPY . /myapp/

# Install Django and project dependencies
RUN pip install --upgrade pip
RUN pip install django

# Generate requirements.txt file
RUN pip freeze > requirements.txt