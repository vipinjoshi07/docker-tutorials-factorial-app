# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /factorial-app

# Copy the current directory contents into the container at /factorial-app
COPY . /factorial-app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "factorial.py"]
