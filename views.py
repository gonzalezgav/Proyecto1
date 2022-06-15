from django.http import HttpResponse
import datetime
from datetime import date
from django.template import Template, Context


def saludo(request):   #Nuestra primera vista :) 
	return HttpResponse("Hola Django - Coder")


def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :) ")

def diaDeHoy(request):

        dia = datetime.datetime.now()

        documentoDeTexto = f"Hoy es día: <br> {dia}"


        return HttpResponse(documentoDeTexto)


def miNombreEs(self, nombre):

      documentoDeTexto = f"Mi nombre es: <br><br>  {nombre}"


      return HttpResponse(documentoDeTexto)


def tercera_vista(request, fecha):
    fecha_actual = date.today()

    anio = fecha_actual.year
    
    fecha = int(fecha)

    resultado = anio - fecha
    
    retorno = f"El año en que naciste es : {resultado}"
    return HttpResponse(retorno)


def probandoTemplate(self):

    miHtml = open("C:/Users/garumani/Desktop/presentacion_coder/django/17bis/Proyecto1/Proyecto1/plantillas/template1.html")
#C:\Users\garumani\Desktop\presentacion_coder\django\17bis\Proyecto1\Proyecto1\plantillas\template1.html
    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)