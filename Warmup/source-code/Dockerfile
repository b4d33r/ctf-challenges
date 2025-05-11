# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install OpenSSL (needed for HTTPS) and copy dependencies
RUN apt-get update && apt-get install -y openssl && rm -rf /var/lib/apt/lists/*

# Copy all project files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir flask pyjwt

# Expose HTTPS port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the app with HTTPS
CMD ["python", "app.py"]
