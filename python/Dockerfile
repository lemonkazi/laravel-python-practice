FROM python:3.10-slim

WORKDIR /usr/src/app

# Copy requirements.txt first (for better caching)
#COPY requirements.txt ./

# Copy requirements.txt first (for better caching)
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# CMD ["python", "app.py"]

COPY . .

CMD ["uvicorn", "my_news_aggregator.app.main:app", "--host", "0.0.0.0", "--port", "5001", "--reload"]
