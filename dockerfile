# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn
RUN pip install gunicorn

# Make port 8080 available to the world outside this container
EXPOSE 5000

# Run the application with gunicorn for production
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

# docker run -d -p 5000:5000 my_demo_app