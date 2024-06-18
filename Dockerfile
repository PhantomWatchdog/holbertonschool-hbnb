FROM python:3.9-alpine
WORKDIR /data
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]
