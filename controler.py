
from elasticsearch import Elasticsearch

def getDados(t):
    es = Elasticsearch()
    res = es.search(index="acervo", body={
        "query": {
            "match": {
                "dcDescription": t
            }
        }
    })
    print(res['hits']['hits'])
    return res['hits']['hits']

def dataAlreadyExists(hs):
    return True

