# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependency file first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# # Command to run the application
# CMD ["python", "app.py"]

# NEW: Run Gunicorn with 4 workers
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:create_app()"]



# id : dpg-d4ipsm7pm1nc73cs6a9g-a
# postgresql://url_db_gse2_user:bUCb8RRoAXXgQaWZfMeg7bPkmgXeO3QB@dpg-d4ipsm7pm1nc73cs6a9g-a/url_db_gse2
# redis://red-d4iq25ogjchc73es15i0:6379