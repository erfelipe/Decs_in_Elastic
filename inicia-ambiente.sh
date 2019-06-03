#!/bin/bash


cd ~/Documents/flask

#python3.7 -m venv venv 

source ~/Documents/flask/venv/bin/activate 

#docker run -dt -p 9200:9200 -e "http.host=0.0.0.0" -e "transport.host=127.0.0.1" --network=elastic --name=elastic docker.elastic.co/elasticsearch/elasticsearch:6.6.0

#docker run -dt -p 5601:5601 -e "ELASTICSEARCH_URL=http://elastic:9200" --network=elastic --name=kibana docker.elastic.co/kibana/kibana:6.6.0

