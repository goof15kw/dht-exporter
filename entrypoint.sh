#!/bin/sh
_term() { 
  echo "Caught SIGTERM signal!" 
  kill -TERM "$child" 2>/dev/null
}
trap _term SIGTERM
echo "Starting exporter on port 8001 with options: --sensor ${SENSOR} -p ${PULL} --gpio ${GPIO} --room ${ROOM}"
/bin/dht_exporter.py --sensor ${SENSOR} -p ${PULL} --gpio ${GPIO} --room ${ROOM} &
child=$! 
wait "$child"