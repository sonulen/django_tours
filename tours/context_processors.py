from tours.data import departures

def menu_departures_list(request):
    return {"departures": departures}