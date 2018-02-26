from lxml import etree
provincia=input("Introduce una comunidad de Sevilla: ")
doc=etree.parse('sevilla.xml')
raiz=doc.getroot()
lista=raiz.findall("municipio")
for elem in lista:
	if (elem.text).upper() == provincia.upper():
		cod=raiz.attrib
		codigo=str(cod).split("-")[1].strip("id").strip("'}")
		print('http://www.aemet.es/xml/municipios/localidad_%s.xml'%codigo)
#doc=etree.parse('http://www.aemet.es/xml/municipios/localidad_%s.xml'%codigo)