# Use the official Python image
FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Copy the entire project to the working directory
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run the application
CMD ["python3", "run.py", "runserver", "0.0.0.0:5000"]