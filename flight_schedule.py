import sys
try:
    from FlightRadar24 import FlightRadar24API
except ImportError:
    print("FlightRadarAPI module not found. Please run: pip install FlightRadarAPI")
    sys.exit(1)

def get_flight_schedule(airport_query):
    fr_api = FlightRadar24API()
    
    print(f"Searching for airport: {airport_query}...")
    airports = fr_api.get_airports()
    
    # Simple search for airport matching the query (Name or ICAO/IATA)
    target_airport = None
    for airport in airports:
        if (airport_query.upper() == airport['iata'] or 
            airport_query.upper() == airport['icao'] or 
            airport_query.lower() in airport['name'].lower()):
            target_airport = airport
            break
            
    if not target_airport:
        print(f"Error: Airport '{airport_query}' not found.")
        return

    print(f"Found airport: {target_airport['name']} ({target_airport['iata']}/{target_airport['icao']})")
    print("Fetching departure flights...")
    
    try:
        # Note: The library methods might vary, using standard approach to get airport details including flights
        # Ideally, we want real-time bounds or specific dashboard data.
        # But fr_api.get_flights() gets airborne flights.
        # To get schedule, we might need airport details which sometimes contains schedules or approximate it by departures from zone.
        
        # FlightRadarAPI's get_flights returns a list of flight objects.
        # We can filter by origin airport ICAO.
        flights = fr_api.get_flights(origin=target_airport['icao'])
        
        if not flights:
            print("No active flights found departing from this airport at the moment.")
            return

        print(f"\nActive Flights departing from {target_airport['name']}:")
        print(f"{'Flight':<10} | {'Destination':<20} | {'Aircraft':<10} | {'Status'}")
        print("-" * 60)
        
        for flight in flights:
            flight_num = flight.callsign or flight.number or "N/A"
            dest = flight.destination_airport_iata or "Unknown"
            aircraft = flight.aircraft_code or "Unknown"
            # Status isn't always detailed in simple get_flights, usually it's "Live" if it appears here
            
            print(f"{flight_num:<10} | {dest:<20} | {aircraft:<10} | Live")
            
    except Exception as e:
        print(f"An error occurred while fetching flights: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = input("Enter airport name or code (e.g., Incheon, ICN): ")
    
    get_flight_schedule(query)
