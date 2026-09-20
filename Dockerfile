FROM python:3.11-slim

# Install LibreOffice
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libreoffice \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Start bot
CMD ["python", "bot.py"]
