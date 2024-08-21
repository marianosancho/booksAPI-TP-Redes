# PROCEDIMIENTO SERVIDOR

Para iniciar el servidor, será necesario primero crear y activar el entorno virtual en la carpeta
descargada

python -m venv .venv
cd .\.venv\Scrips
.\activate

Una vez activado, instalar las dependencias necesarias usando el comando

pip install -r requierements.txt

Ya se podría iniciar el servidor con el comando:
python .\src\server\server.py

De esta forma, estaríamos abriendo el servidor en la direccion http://127.0.0.1:8000 .

Si se quiere acceder al servidor desde otra terminal, se deberá cambiar el valor de HOST en server.py
por la IP del servidor.


# PROCEDIMIENTO CLIENTE

El proceso de inicio del cliente es similar al del servidor. En una terminal, abrimos la carpeta
descargada y creamos el entorno virtual.

python -m venv .venv
cd .\.venv\Scrips
.\activate

Una vez activado, instalar las dependencias necesarias usando el comando

pip install -r requierements.txt

Ya se podría iniciar el cliente con el comando:

python .\src\client\client.py

Al igual que en el caso anterior, si se quiere acceder a un servidor ubicado en otra terminal, se
deberá cambiar el valor de HOST en auxiliar.py por la IP del servidor.
