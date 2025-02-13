# Use the official Python image from the Docker Hub
FROM python:3-slim-buster AS builder

# Set the working directory in the container
WORKDIR /app

# Install dependencies for OpenCV, pylsd, and build tools
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    build-essential \
    cmake \
    libatlas-base-dev \
    gfortran \
    && apt-get clean

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies with detailed logging
RUN pip install --no-cache-dir -r requirements.txt --log /app/pip-install.log

# Uninstall and reinstall ocrd-fork-pylsd to ensure it is properly compiled
RUN pip uninstall -y ocrd-fork-pylsd && pip install ocrd-fork-pylsd

# Copy the rest of the application code into the container
COPY . .

# # Expose the port the app runs on
EXPOSE 7070

# # Command to run the application
CMD ["python", "main.py"]
