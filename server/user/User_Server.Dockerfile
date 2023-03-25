# Use an official Python runtime as a parent image - for a list of others see https://hub.docker.com/_/python/
FROM python:3-stretch

# Set the working directory to /app - this is a directory that gets created in the image
WORKDIR /app

# Copy the current host directory contents into the container at /app
COPY . /app

# This will speed up the build time
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN pip install redis

RUN pip install tinydb

# RabbitMQ
RUN pip install pike

# Make port 50051 available to the world outside this container
EXPOSE 50051

# RUN python3 -m grpc_tools.protoc -I../../protos --python_out=. --pyi_out=. --grpc_python_out=. user.proto
# RUN python3 -m grpc_tools.protoc -I/app/assignment01/protos --python_out=. --grpc_python_out=. /app/assignment01/protos/user.proto

# Run greeter_server.py when the container launches
CMD ["python", "user_server.py"]

