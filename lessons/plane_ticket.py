from __future__ import annotations

class PlaneTicket:

    departure_city: str
    arrival_city: str
    departure_time: int
    ticket_cost: float

    def __init__(self, city_a: str, city_b: str, depart: int, cost: float):
        """Initialize plane class."""
        self.departure_city = city_a
        self.arrival_city = city_b
        self.departure_time = depart
        self.ticket_cost = cost

    def __str__(self) -> str:
        my_ticket_str: str = f"Depart from {self.departure_city} at {self.departure_time}. "
        my_ticket_str += f"Arrive at {self.arrival_city}. It cost ${self.ticket_cost}."
        return my_ticket_str

    def delay(self, delay_hours: int) -> None:
        """Delay departure time by delay hours."""
        self.departure_time += (delay_hours * 100)
        self.departure_time %= 2400
    
    def discount(self, discount: float) -> None:
        """Discount ticket cost by discount %."""
        assert discount < 1
        self.ticket_cost *= (1 - discount)
    

def compare_prices(ticket1: PlaneTicket, ticket2: PlaneTicket) -> PlaneTicket:
    """Compare the cost of the two plane tickets and returns the cheapest."""
    if ticket1.ticket_cost < ticket2.ticket_cost:
        return ticket1
    else:
        return ticket2


#my_ticket: PlaneTicket = PlaneTicket("Atlanta", "NYC", 2300, 25.00)
#print(my_ticket)
#my_ticket.delay(2)
#print(my_ticket)
#my_ticket.discount(0.15)
#print(my_ticket)

east: PlaneTicket = PlaneTicket("Raleigh", "New Orleans", 1000, 85.25)
print(east)
east.delay(2)
east.discount(0.10)
west: PlaneTicket = PlaneTicket("Orlando", "San Fransisco", 1100, 100.50)
print(west)
cheaper_ticket: PlaneTicket = compare_prices(east, west)
print(cheaper_ticket)