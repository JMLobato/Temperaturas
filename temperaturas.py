from lxml import etree
from datetime import date
provincia=input("Introduce una comunidad de Sevilla: ")
doc=etree.parse('sevilla.xml')
raiz=doc.getroot()
lista=raiz.xpath("municipio")
for elem in lista:
	if (elem.text).upper() == provincia.upper():
		cod=elem.attrib
		codigo=cod["value"].split("-")[-1].strip("id")
		print('http://www.aemet.es/xml/municipios/localidad_%s.xml'%codigo)
doc=etree.parse('http://www.aemet.es/xml/municipios/localidad_%s.xml'%codigo)
raiz=doc.getroot()
today = date.today()
dia=raiz.xpath("prediccion/dia")[0].attrib["fecha"]

if str(dia) == str(today):
	print("La temperatura Max es de ",end="")
	print(raiz.xpath("prediccion/dia")[0].xpath("temperatura/maxima")[0].text)
	print("La temperatura Min es de ",end="")
	print(raiz.xpath("prediccion/dia")[0].xpath("temperatura/minima")[0].text)