
from elasticsearch import Elasticsearch
import xml.etree.ElementTree as et
import json

def get_DadosPeloDeCS(tBr, tEs, tEn):
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
    #print(res['hits']['hits']) #tirar em producao - apenas teste
    return res['hits']['hits']

# Metodo a ser retirado
def get_Dados_somente_Br(tBr):
    es = Elasticsearch()
    res = es.search(index="acervo", body={
        "query": {
            "match": {
                "dcDescription": tBr
            }
        }
    })
    #print(res['hits']['hits'])
    return res['hits']['hits']

# Verificar se o MD5 do arquivo jah estah na base
def get_Doc_existente_na_base(hs):
    return False

# Usado quando desejar atualizar a listagem resumo
def extrai_e_grava_TermosChave():
    dados = {}
    tree = et.parse("/Users/eduardofelipe/Documents/Ontologias/MeSH/mtms/pordesc2019.xml")
    raiz = tree.getroot()

    dados['termo'] = []

    for folha in raiz.findall("DescriptorRecord"):
        ui = folha.find("DescriptorUI")
        chave = ui.text
        dn = folha.find("DescriptorName")
        expressao = dn[0].text.partition('[')
        # primeira parte da string, termo em pt-br
        tBr = expressao[0]
        # ultima parte da string english, e exclui o ultimo caracter ']' por slice
        tEn = expressao[2][:-1]
        # pega o termo em espanhol no outro arquivo
        tEs = 'Termo_es'

        dados['termo'].append({
        'ui': chave,
        'pt-br': tBr,
        'es': tEs,
        'en': tEn })
    
    with open('/Users/eduardofelipe/Documents/Ontologias/MeSH/mtms/termos.txt', 'w') as arq:
        json.dump(dados, arq, indent=4, ensure_ascii=False)
       

def get_TermosChaveGravados_Em_Lista_Json():
    with open('/Users/eduardofelipe/Documents/Ontologias/MeSH/mtms/termos.txt', 'r') as arq:
        dados = json.load(arq)
        return dados
    
def get_Termos_Outros_Idiomas(termoBr): 
    dados = {'es': 'None', 'en': 'None'}
    listaDados = get_TermosChaveGravados_Em_Lista_Json()
    if ( len(listaDados) > 0) :
        for linha in listaDados['termo']:
            tlinha = linha['pt-br'].lower()
            if (tlinha == termoBr.lower()) :
                dados['es'] = linha['es']
                dados['en'] = linha['en']
    return dados

