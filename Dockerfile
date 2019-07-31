# Builder
FROM arm32v7/python:alpine

LABEL maintainer="Andrea Cervesato <koma@redhat.com> (https://github.com/u/Koma-Andrea)"

ENV \
GIT_VERSION="v1.1" \
REPO="https://github.com/Koma-Andrea/dht-exporter.git" \
WORKDIR=/tmp/dht-exporter

# Install dependencies
RUN \
apk add libc-dev gcc git; \
pip install prometheus_client Adafruit_DHT; \
git clone --depth 1 --branch ${GIT_VERSION} ${REPO} ${WORKDIR}; \
cp  ${WORKDIR}/dht_exporter.py /bin/dht_exporter.py; \
rm -fr /root/.cache/pip/; rm -rf /var/cache/apk/*

ENV \
SENSOR="DHT11" \
PULL="5" \
GPIO="4" \
ROOM="none"

EXPOSE  8001

ENTRYPOINT  [ "/bin/dht_exporter.py" ]

CMD         [ "--sensor", "${$SENSOR}", "--pull", "${PULL}", "--gpio", "${GPIO}", "--room", "${ROOM}" ]
