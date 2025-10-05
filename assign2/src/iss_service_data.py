def get_location(iss_location_service):
    try:
        return iss_location_service()
    except Exception as e:
        return str(e)

def get_astronaut(iss_astronaut_service):
    def key_for_sort(name):
        *first_name, last_name = name.split()
        
        return (last_name, ' '.join(first_name))

    try:
        return sorted(iss_astronaut_service(), key=key_for_sort)
    except Exception as e:
        return str(e)
