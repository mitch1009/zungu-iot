FROM python:3.8 as base-stage

WORKDIR /app

COPY ../ ./

FROM base-stage as dev-stage

RUN pip3 install -r resuirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:5800", "-w 5"]
