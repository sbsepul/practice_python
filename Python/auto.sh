#!/bin/bash
echo Arbitraje Seba SA
cont=0
#vamos a mandar señales 100 veces, cada 10 min, 
#donde la configuracion de espera se debe hacer manual
while [ $cont -lt 100 ]; do
cd /home/lion/Escritorio/api
python3 apip.py
echo
echo Autor: Sebastian Sepulveda
echo Derechos reservados. Cualquier copia sera multada
echo Mas informacion hable con el autor
echo Que tenga un buen dia
echo
echo Espere un minuto para recibir nuevas señales
echo O cierre el archivo con Ctrl+C
let cont=cont+1
sleep 600
done
