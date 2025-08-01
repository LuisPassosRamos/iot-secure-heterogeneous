FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir requests
EXPOSE 6000
CMD ["python", "gateway_udp.py"]
