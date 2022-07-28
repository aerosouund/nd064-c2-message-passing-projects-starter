FROM python:3.7-alpine

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev bash curl

RUN pip install -r requirements.txt

CMD ["python", "main.py"]