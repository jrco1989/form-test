# form-test

Ejemplo de selectores encadenados para la creación de registros por medio de un formulario 

##Instalación:

    *-*Ejecutar el siguiente comando para instalar las librerias necesarias:
        `pip install -r requirements.txt`

##Configuración:

    * Reemplazar el nombre de la base de datos en la línea 62 del archivo "settings.py"  por el nombre de la base de datos de Posgrest creada localmente (el proycto está configurado para recibir una base de datos de Postgres ). 

    * Aplicar las migraciones con los comandos:

        * `python manage.py makemigrations`
        - `python manage.py migrate`

    * Crear un super usuario, para ingresar al admin y crear las opciones anidadas, con el comando:

        * `python manage.py createsuperuser username xxx`
    
    * Ejecutar el servidor local con:
      
        * `python manage.py runserver`

Para ingresar al administador de django la url es: 
    127.0.0.1:8000/admin/

