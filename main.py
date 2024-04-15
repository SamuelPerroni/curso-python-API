import requests
from fastapi import FastAPI, Query

from config.constantes import URL_API_RESTAURANTES

app = FastAPI()

@app.get('/api/hello')
def  hello_world():
    '''
    Endpoint que exibe uma mensagem incrível do mundo da programação
    '''
    return {'Hello':'world'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Enfpoint para ver os cardápios dos restaurantes
    '''
    response = requests.get(URL_API_RESTAURANTES)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}
        
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante: 
                dados_restaurante.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })
                
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}       

    else:
        return {'Erro': f'{response.status_code} - {response.text}'}