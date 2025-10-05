from src.iss_service_data import get_location as get_location_data
from src.location_webservice import get_location as get_location_webservice

from src.iss_service_data import get_astronaut
from src.astronaut_names_webservice import get_astronauts_names


def output_location():
    location_data = get_location_data(get_location_webservice)
    return f"ISS location as {location_data['central_time']} CT flying over {location_data['place']}"

def output_astronaut_names():
    astronauts = get_astronaut(get_astronauts_names)
    
    formatted_astronauts = "\n".join(astronauts)
    return f"There are {len(astronauts)} people on ISS at this time:\n{formatted_astronauts}"

if __name__ == "__main__":
    print(output_location())
    print()
    print(output_astronaut_names())
