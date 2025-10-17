# Base image on Pyton 3.12
FROM python:3.12-slim

# Create and set the work Directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install all need packages in the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app's code
COPY ["AI Diet and Meal Planner/task", "."]

# Expose the Uvicorn port
EXPOSE 8000

# Command to run - Uvicorn to serve the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port","8000"]
