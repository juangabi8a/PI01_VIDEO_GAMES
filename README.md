# Proyecto Video Games

En este proyecto, realizaremos el análisis de una plataforma de videojuegos con el fin de determinar cuáles son los juegos mejor valorados por los usuarios. Este análisis se realizará mediante un modelo de machine learning. También exploraremos los géneros de videojuegos a los que los usuarios dedican más tiempo, identificaremos los usuarios que juegan más tiempo y haremos un top 3 de los juegos más recomendados, así como un top 3 de los desarrolladores menos recomendados.

A lo largo del proyecto, trabajaremos con los siguientes conjuntos de datos en formato JSON:

- `australian_user_reviews`: Contiene todas las reseñas realizadas por los usuarios.
- `output_steam_games`: Incluye el catálogo completo de videojuegos y sus categorías respectivas.
- `australian_users_items`: Contiene información sobre todos los usuarios de la plataforma.

## Análisis de Sentimientos

En la primera etapa del proyecto, realizamos el análisis de sentimientos de las reseñas dadas por los usuarios. Este proceso se automatizó mediante la librería `nltk`, que clasificó automáticamente los comentarios como positivos, negativos o neutros. Para más detalles sobre este proceso, puedes revisar el notebook `Analisis_Sentimiento.ipynb`.

## EDA y ETL

En la segunda etapa, realizamos un análisis exploratorio de datos (EDA) para comprender nuestras bases de datos y, simultáneamente, realizamos procesos de ETL para transformar y adecuar la información para su uso posterior. Esto se puede observar en el notebook `EDA_y_ETL.ipynb`.

## Funciones

En la tercera etapa, elaboramos funciones relevantes que serán utilizadas para la API. Estas funciones se basaron en una muestra del dataframe `australian_users_items`, con el objetivo de tener una base de datos más liviana y eficiente. Las funciones son:

- `PlayTimeGenre(genero: str)`: Devuelve el año con más horas jugadas para un género de videojuego dado.
- `UserForGenre(genero: str)`: Devuelve el usuario que acumula más horas jugadas para un género dado y una lista de la acumulación de horas jugadas por año.
- `UsersRecommend(año: int)`: Devuelve el top 3 de juegos más recomendados por usuarios para un año dado.
- `UsersWorstDeveloper(año: int)`: Devuelve el top 3 de desarrolladoras con juegos menos recomendados por usuarios para un año dado.

Para más detalles sobre estas funciones, puedes revisar el notebook `API_DepuradoFunciones.ipynb`.

## API

Utilizamos FastAPI y Uvicorn para crear nuestra API. Los pasos para su creación incluyeron la configuración de un entorno virtual, la creación de un archivo para llamar a las funciones, la definición de un archivo con las funciones a utilizar (`API_FUNCIONES.py`), y finalmente la ejecución de Uvicorn para probar localmente la API.

## Deploy

Para desplegar nuestra API en la nube, primero copiamos los archivos necesarios al repositorio de GitHub. Luego, utilizamos Render para configurar y seleccionar los archivos de nuestro repositorio a desplegar. Render nos proporcionó una dirección web donde quedó cargada la API: [https://video-games-shp9.onrender.com/](https://video-games-shp9.onrender.com/).

### Cómo usar la API?

1. Ingresa a [https://video-games-shp9.onrender.com/](https://video-games-shp9.onrender.com/).
2. Después de la dirección web, agrega el nombre de la función a utilizar. Por ejemplo, para `PlayTimeGenre`, la URL sería [https://video-games-shp9.onrender.com/PlayTimeGenre](https://video-games-shp9.onrender.com/PlayTimeGenre).
3. Después de la función, agrega una barra diagonal seguida del parámetro de la función. Por ejemplo, para el género 'Action', la URL completa sería [https://video-games-shp9.onrender.com/PlayTimeGenre/Action](https://video-games-shp9.onrender.com/PlayTimeGenre/Action).
4. Presiona Enter y se mostrará el resultado de tu consulta.
