FROM python:3.11.9

# Set the working directory to the root directory of your project
WORKDIR /MountCapstone/mysite

# Copy all project files to the working directory in the container
COPY . /MountCapstone/mysite/

# Install Django and project dependencies
RUN pip install --upgrade pip
RUN pip install django

# Generate requirements.txt file
RUN pip freeze > requirements.txt


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]