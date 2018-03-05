from lxml import etree
provincia=input("Introduce una comunidad de Sevilla: ")
doc=etree.parse('sevilla.xml')
raiz=doc.getroot()
lista=raiz.xpath("municipio")
for elem in lista:
	if (elem.text).upper() == provincia.upper():
		cod=elem.attrib
		#codigo=str(cod).split("-")[1].strip("id").strip("'}")
		#print('http://www.aemet.es/xml/municipios/localidad_%s.xml'%codigo)
		print(cod)
#doc=etree.parse('http://www.aemet.es/xml/municipios/localidad_%s.xml'%codigo)