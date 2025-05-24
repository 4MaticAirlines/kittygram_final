FROM python:3.9-slim
RUN pip install gunicorn
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade "pip<23.2" "setuptools<66.0.0" "wheel<0.38.0" && \
    pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:8090", "kittygram_backend.wsgi:application"]