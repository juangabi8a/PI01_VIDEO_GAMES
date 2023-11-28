import numpy as np
import pandas as pd

muestra_items=pd.read_csv('data_funcion_1y2.csv')
data_review=pd.read_csv('data_funcion_3y4.csv')

# Funcion 1

def PlayTimeGenre( genero : str ):
    filto_genero=muestra_items[muestra_items['genres_games']==genero]
    anio_max_horas=int(filto_genero.groupby('year')['playtime_forever'].sum().idxmax())
    
    resul= {'Año de lanzamiento con más horas jugadas para {}'.format(genero):anio_max_horas}
    return resul



# Funcion 2

def UserForGenre( genero : str ):
    filto_genero=muestra_items[muestra_items['genres_games']== genero]
    user_max_hora=filto_genero.groupby('user_id')['playtime_forever'].sum().idxmax()
    
    anio_2010= (muestra_items[(muestra_items['user_id'] ==user_max_hora) & (muestra_items['genres_games'] == genero) & (muestra_items['year']==2010)]['playtime_forever'].sum())/60
    anio_2011= (muestra_items[(muestra_items['user_id'] ==user_max_hora) & (muestra_items['genres_games'] == genero) & (muestra_items['year']==2011)]['playtime_forever'].sum())/60
    anio_2012= (muestra_items[(muestra_items['user_id'] ==user_max_hora) & (muestra_items['genres_games'] == genero) & (muestra_items['year']==2012)]['playtime_forever'].sum())/60
    anio_2013= (muestra_items[(muestra_items['user_id'] ==user_max_hora) & (muestra_items['genres_games'] == genero) & (muestra_items['year']==2013)]['playtime_forever'].sum())/60
    anio_2014= (muestra_items[(muestra_items['user_id'] ==user_max_hora) & (muestra_items['genres_games'] == genero) & (muestra_items['year']==2014)]['playtime_forever'].sum())/60
    anio_2015= (muestra_items[(muestra_items['user_id'] ==user_max_hora ) & (muestra_items['genres_games'] == genero) & (muestra_items['year']==2015)]['playtime_forever'].sum())/60
    
    resultado = {
    'usuario': user_max_hora,
    'año 2010': anio_2010,
    'año 2011': anio_2011,
    'año 2012': anio_2012,
    'año 2013': anio_2013,
    'año 2014': anio_2014,
    'año 2015': anio_2015
}
    return resultado

    



# Funcion 3

## variable año
def UsersRecommend( año : int ): 
    recomendado = data_review[(data_review['year']==año) & (data_review['recommend_True']==1) & ((data_review['sentiment_analysis']==1) | (data_review['sentiment_analysis']==2))]

    recomendado=recomendado.groupby(['item_id', 'title'])['sentiment_analysis'].sum().reset_index().sort_values(by='sentiment_analysis', ascending=False).head(3)

    result = recomendado['title']

    result= pd.DataFrame(result)

    puesto_1 = result.iloc[0]['title']
    puesto_2 = result.iloc[1]['title']
    puesto_3 = result.iloc[2]['title']

    resultado = {
        'PUESTO 1': puesto_1,
        'PUESTO 2': puesto_2,
        'PUESTO 3': puesto_3
    }

    return resultado



# Funcion 4

def UsersWorstDeveloper( año : int ): 
    no_recomendado = data_review[(data_review['year'] == año) & (data_review['recommend_False'] == 1) & (data_review['sentiment_analysis'] == 0)]

    result= no_recomendado.groupby(['developer']).size().reset_index(name='count').sort_values(by='count', ascending=False).head(3)

    puesto_1 = result.iloc[0]['developer']
    puesto_2 = result.iloc[1]['developer']
    puesto_3 = result.iloc[2]['developer']

    resultado = {
        'PUESTO 1': puesto_1,
        'PUESTO 2': puesto_2,
        'PUESTO 3': puesto_3
    }

    return resultado











