import webbrowser
class reporte:
    def reportar(self,productos):
        arrProd = []
        for i in productos:
            arrProd.append(i)

        for i in range(len(arrProd)-1):
            for j in range(len(arrProd)-i-1):
                if int(arrProd[j]['cantidad'])*float(arrProd[j]['precio']) < int(arrProd[j+1]['cantidad'])*float(arrProd[j+1]['precio']):
                    arrProd[j],arrProd[j+1] = arrProd[j+1],arrProd[j]

        ventas = []
        for i in productos:
            ventas.append(i)

        for i in range(len(ventas)-1):
            for j in range(len(ventas)-i-1):
                if int(ventas[j]['cantidad']) < int(ventas[j+1]['cantidad']):
                    ventas[j],ventas[j+1] = ventas[j+1],ventas[j]

        reporte = """<!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Reporte</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
        <!--===============================================================================================-->	
            <link rel="icon" type="image/png" href="Reporte/images/icons/logousac.png"/>
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="Reporte/vendor/bootstrap/css/bootstrap.min.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="Reporte/fonts/font-awesome-4.7.0/css/font-awesome.min.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="Reporte/vendor/animate/animate.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="Reporte/vendor/select2/select2.min.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="Reporte/vendor/perfect-scrollbar/perfect-scrollbar.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="Reporte/css/util.css">
            <link rel="stylesheet" type="text/css" href="Reporte/css/main.css">
        <!--===============================================================================================-->
        </head>
        <body>
            <div class="limiter">
                <div class="container-table100">
                    <div class="wrap-table100">
                        <div class="table100">
                            <table style="margin-bottom: 50px;">
                                <thead>
                                    <tr class="table100-head">
                                        <th class="column1">
                                            201908355 - Danny Hugo Bryan Tejax&uacute;n Pichiy&aacute;
                                        </th>
                                    </tr>
                                </thead>
                            </table>
                            <table style="margin-bottom: 50px;">
                                <thead>
                                    <tr class="table100-head">
                                        <th class="column1">Producto</th>
                                        <th class="column2">Precio</th>
                                        <th class="column3">Unidades Vendidas</th>
                                        <th class="column6">Total</th>
                                    </tr>
                                </thead>
                                <tbody>"""

        for i in arrProd:
            reporte += """<tr>
                                            <td class="column1">"""+str(i['nombre'])+"""</td>
                                            <td class="column2">Q """+str(i['precio'])+"""</td>
                                            <td class="column3">"""+str(i['cantidad'])+"""</td>
                                            <td class="column6">Q """+str(round(float(i['precio'])*int(i['cantidad']),2))+"""</td>
                                        </tr>"""

        reporte += """</tbody>
                            </table>
                            <table style="margin-bottom: 50px;">
                                <thead>
                                    <tr class="table100-head">
                                        <th class="column1">Producto</th>
                                        <th class="column2">Precio</th>
                                        <th class="column6">Unidades Vendidas</th>
                                    </tr>
                                </thead>
                                <tbody>
                                <tr>
                                            <td class="column1">"""+str(ventas[0]['nombre'])+"""</td>
                                            <td class="column2">Q """+str(ventas[0]['precio'])+"""</td>
                                            <td class="column6">"""+str(ventas[0]['cantidad'])+"""</td>
                                        </tr>
                                </tbody>
                            </table>
                            </tbody>
                            </table>
                            <table style="margin-bottom: 50px;">
                                <thead>
                                    <tr class="table100-head">
                                        <th class="column1">Producto</th>
                                        <th class="column2">Precio</th>
                                        <th class="column6">Unidades Vendidas</th>
                                    </tr>
                                </thead>
                                <tbody>
                                <tr>
                                            <td class="column1">"""+str(ventas[len(ventas)-1]['nombre'])+"""</td>
                                            <td class="column2">Q """+str(ventas[len(ventas)-1]['precio'])+"""</td>
                                            <td class="column6">"""+str(ventas[len(ventas)-1]['cantidad'])+"""</td>
                                        </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>


            

        <!--===============================================================================================-->	
            <script src="Reporte/vendor/jquery/jquery-3.2.1.min.js"></script>
        <!--===============================================================================================-->
            <script src="Reporte/vendor/bootstrap/js/popper.js"></script>
            <script src="Reporte/vendor/bootstrap/js/bootstrap.min.js"></script>
        <!--===============================================================================================-->
            <script src="Reporte/vendor/select2/select2.min.js"></script>
        <!--===============================================================================================-->
            <script src="Reporte/js/main.js"></script>

        </body>
        </html>"""

        file = open("Reporte.html","w")
        amount_written = file.write(reporte)
        file.close()

        webbrowser.open_new_tab("Reporte.html")