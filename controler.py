
from elasticsearch import Elasticsearch


def getDadosPeloDeCS(tBr, tEs, tEn):
    es = Elasticsearch()
    res = es.search(index="acervo", body = {
        "query": {
            "bool": {
                "should": [
                    {
                        "match": {
                            "dcDescription": tBr
                        }
                    },
                    {
                        "match": {
                            "dcDescription": tEs
                        }
                    },
                    {
                        "match": {
                            "dcDescription": tEn
                        }
                    }
                ]
            }
        }
    })
    print(res['hits']['hits'])
    return res['hits']['hits']


def getDados(tBr, tEs, tEn):
    es = Elasticsearch()
    res = es.search(index="acervo", body={
        "query": {
            "match": {
                "dcDescription": tBr
            }
        }
    })
    print(res['hits']['hits'])
    return res['hits']['hits']


def dataAlreadyExists(hs):
    return True
