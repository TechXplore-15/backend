# Use the official Python image
FROM python:3.12-bookworm

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Dependencies
RUN pip install -r requirements.txt

# Run manage.py on serverside
#CMD ["python", "manage.py", "runserver"]

# Run Gunicoooorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "djangoProject.wsgi"]

# Expose Python Runserver Port
EXPOSE 8000
