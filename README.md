# xg_callcenter

[Live Demo xp-callcenter.herokuapp.com/](http://xp-callcenter.herokuapp.com/)

### Prerequisitos

- npm
`npm install npm@latest -g`
- Python 3.9


### Instalacion

1. Clonar el repositorio  
   ```sh
   git clone https://github.com/antorpo/teoria_lenguajes_2021-1.git
   ```
   
2. Ir al directorio de la practica #1
   ```sh
   cd practica_01
   ```
   
3. Instalar dependencias del back-end
   ```sh
   pip install -r requirements.txt
   ```
   
4. Migrar la Base de Datos
   ```PY
   python manage.py migrate
   ```
   
5. Ir al directorio del front-end
   ```sh
   cd frontend
   ```
   
6. Instalar dependencias del front-end
   ```sh
   npm install
   ```
   
7. Compilamos la app para producción
   ```sh
   npm run build
   ```
   
8. Volvemos al directorio de la practica #1 y corremos el servidor de desarrollo
   ```sh
   cd .. && python manage.py runserver
   ```
   
9. Abrimos el aplicativo en el navegador con ruta `localhost:8000/`
