import requests
from datetime import datetime, timedelta, timezone
from geopy import geocoders
import us

def get_response():
    return requests.get('http://api.open-notify.org/iss-now.json').json()

def parse_response(data):
    POSITION = 'iss_position'
    TIMESTAMP = 'timestamp'

    return { 'latitude': data[POSITION]['latitude'], 'longitude': data[POSITION]['longitude'], 'timestamp': data[TIMESTAMP] }

def get_location():
    CENTRAL_TIME_OFFSET = 6
    
    def get_central_time(timestamp):
        return (datetime.fromtimestamp(timestamp, tz=timezone.utc) - timedelta(hours=CENTRAL_TIME_OFFSET)).strftime('%I:%M %p')

    def get_place(latitude, longitude):
        geolocator = geocoders.Nominatim(user_agent="iss_location_app")
        location = geolocator.reverse((latitude, longitude), language='en')
        
        if location:
            address = location.raw.get('address', {})
            city, state, country = address.get('city'), address.get('state'), address.get('country')
            state_abbreviation = us.states.lookup(state).abbr if us.states.lookup(state) else state
            return f"{city}, {state_abbreviation}" if city and state_abbreviation else city or state_abbreviation or country
    
        return "Unknown Location"

    data = parse_response(get_response())
    data['central_time'] = get_central_time(data['timestamp'])
    data.pop('timestamp')

    place = get_place(data['latitude'], data['longitude'])
    data['place'] = place

    data.pop('latitude')
    data.pop('longitude')

    return data
