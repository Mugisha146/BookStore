# Use the official Python image from the Docker Hub
FROM python:3.10

# Set environment variables to prevent .pyc files and enable output buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Define environment variables
ENV DJANGO_ENV=production

# Collect static files (optional but recommended for production)
RUN python manage.py collectstatic --noinput

# Start the application using Gunicorn without SSL (SSL will be handled by Nginx)
CMD ["gunicorn", "book_rental.wsgi:application", "--bind", "0.0.0.0:8000"]
