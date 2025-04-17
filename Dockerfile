# Use an official Python base image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /Expense_tracker

# Copy the local project files to the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port FastAPI runs on (optional but recommended)
EXPOSE 8000

# Default command to run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
