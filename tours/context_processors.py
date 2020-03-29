from tours.data import departures, title

def menu_data(request):
    return {"departures": departures, "title" : title}