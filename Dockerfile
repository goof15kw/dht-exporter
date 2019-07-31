# Builder
FROM arm32v7/python:alpine

MAINTAINER Andrea Cervesato <koma@redhat.com> (https://github.com/u/Koma-Andrea)

ENV GIT_VERSION "v1.0"

ENV REPO "https://github.com/Koma-Andrea/dht-exporter.git"

ENV WORKDIR /tmp/dht-exporter

RUN apk add libc-dev gcc git

RUN pip install prometheus_client Adafruit_DHT

RUN git clone --depth 1 --branch ${GIT_VERSION} ${REPO} ${WORKDIR}

RUN cp  ${WORKDIR}/dht_exporter.py /bin/dht_exporter.py

EXPOSE  8001

ENV SENSOR DHT11

ENV PULL 5

ENV GPIO 4

ENV ROOM none

ENTRYPOINT  [ "/bin/dht_exporter.py" ]

CMD         [ "--sensor", "${$SENSOR}", "--pull", "${PULL}", "--gpio", "${GPIO}", "--room", "${ROOM}" ]
