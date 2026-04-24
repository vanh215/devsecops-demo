# LỖI BẢO MẬT 3: Dùng bản Python 3.8 cũ chứa nhiều lỗ hổng (Trivy sẽ tóm cái này)
FROM python:3.8-slim-buster
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]