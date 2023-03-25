# Use an official Python runtime as a parent image
FROM python:3-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the client code into the container at /app
COPY . /app
# COPY services/greeter/greeter_client.py /app/greeter_client.py
# COPY requirements.txt /app/requirements.txt

# # This will speed up the build time
RUN pip install --upgrade pip

# # Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# RUN python3 -m grpc_tools.protoc -I../../protos --python_out=. --pyi_out=. --grpc_python_out=. helloworld.proto
# RUN python3 -m grpc_tools.protoc -I/app/assignment01/protos --python_out=. --grpc_python_out=. /app/assignment01/protos/helloworld.proto

#Run greeter_client.py when the container launches
CMD ["python", "greeter_client.py"]

