FROM python:3-slim
WORKDIR /app
COPY app.py .
COPY test_app.py .
CMD ["python", "app.py"]
