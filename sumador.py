#!/usr/bin/python

import webapp


class sumador(webapp.webApp):
    """Simple add"""

    primero = 0

    def parse(self, request):
        """Parse the received request, extracting the relevant information."""

        try:
            numero = int(request.split(' ')[1][1:])
        except ValueError:
            numero = "Error"
        return numero

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns 200 OK and an HTML page.
        """

        if parsedRequest != "Error":
            if not self.primero:
                self.primero = parsedRequest
                resultado = "falta segundo numero"
                #primero = False
            else:
                resultado = self.primero + parsedRequest
                self.primero = 0
            httpCode = "200 OK"
            htmlBody = "La suma es:" + str(resultado)
        else:
            httpCode = "400 Bad Request"
            htmlBody = "Usage Error: introduzca sumando"
        return (httpCode, "<html><body><p>" + htmlBody + "</p></body></html>")


if __name__ == "__main__":
    testWebApp = sumador("localhost", 1234)
