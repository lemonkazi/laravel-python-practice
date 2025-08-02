FROM python:3.10-slim

WORKDIR /usr/src/app

# Copy requirements.txt first (for better caching)
#COPY requirements.txt ./

# Copy requirements.txt first (for better caching)
COPY requirements-test.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements-test.txt

CMD ["python", "app.py"]
