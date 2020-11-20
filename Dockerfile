FROM python:3-slim

COPY . /app
WORKDIR /app
#RUN mkdir out?
#RUN pip install dotenv

ENV COUNT=2
ENV SIZE=1
ENV TRIES=5
ENV SLEEP=1
ENV LOG=TRUE

CMD python /app/app.py