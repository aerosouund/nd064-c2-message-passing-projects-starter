FROM python:3.7-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev python3-devel gcc-c++
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENV FLASK_ENV=development

EXPOSE 5000

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]