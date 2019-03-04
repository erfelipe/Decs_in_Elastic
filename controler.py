from elasticsearch import Elasticsearch

def getDados(t):
    es = Elasticsearch()
    res = es.search(index="teste", body={
        "query": {
            "match": {
                "corpo": t
            }
        }
    })
    print(res['hits']['hits'])
    return res['hits']['hits']

def dataAlreadyExists(hs):
    return True

