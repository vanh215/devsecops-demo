# Dùng bản python:3.8-slim-buster (phiên bản cũ, chứa nhiều lỗi bảo mật)
FROM python:3.8-slim-buster
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
