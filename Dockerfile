# Use official Python base image
FROM python:3.13-slim


# Set working directory
WORKDIR /E444-F2025-PRA2

# Copy requirements first (for caching)
COPY requirements.txt /E444-F2025-PRA2/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . /E444-F2025-PRA2

# Expose port 5000
EXPOSE 5000

# Run the app
CMD ["python", "hi.py"]
