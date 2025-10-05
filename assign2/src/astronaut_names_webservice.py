import requests

def get_response():
    return requests.get('http://api.open-notify.org/astros.json').json()

def parse_response(data):
    CRAFT = 'ISS'

    return [astronaut['name'] for astronaut in data['people'] if astronaut['craft'] == CRAFT]
    
def get_astronauts_names():
    return parse_response(get_response())
