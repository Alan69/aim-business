# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt to install dependencies
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 8001 for gunicorn to bind to
EXPOSE 8001

# Run the application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8001", "AIM_landing.wsgi:application"]
