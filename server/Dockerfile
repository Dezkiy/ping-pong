FROM python:3.8-alpine

RUN pip install falcon

WORKDIR /app/server
COPY server.py .

EXPOSE 80

CMD ["python", "./server.py"]

