from lxml import etree
provincia=input("Introduce una comunidad de Sevilla: ")
doc=etree.parse('sevilla.xml')
raiz=doc.getroot()
cod=raiz[0].attrib
print(str(cod).split("-")[1])
#doc=etree.parse('http://www.aemet.es/xml/municipios/localidad_%s.xml'%codigo)