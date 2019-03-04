
from xml.dom.minidom import parse 
import xml.dom.minidom
import xml.etree.ElementTree as et

# DOMTree = xml.dom.minidom.parse("/Users/eduardofelipe/Documents/Ontologias/MeSH/mtms/pordesc2019-resumo.xml")


# collection = DOMTree.documentElement

# descritores = collection.getElementsByTagName("DescriptorRecord")

# print( collection )

# print( descritores )

# for descritor in descritores:
#     print( "Desc: " )
#     d = descritor.getElementsByTagName("DescriptorName")[0] 
#     print ( d )


tree = et.parse("/Users/eduardofelipe/Documents/Ontologias/MeSH/mtms/pordesc2019-resumo.xml")
raiz = tree.getroot()

for folha in raiz.findall("DescriptorRecord"):
    dn = folha.findall("DescriptorName")
    for nome in dn:
        print (nome[0].text)

    chave = folha.find("DescriptorUI")
    print (chave.text)

    