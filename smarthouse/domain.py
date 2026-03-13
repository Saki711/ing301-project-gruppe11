class Measurement:
    """
    This class represents a measurement taken from a sensor.
    """

    def __init__(self, timestamp, value, unit):
        self.timestamp = timestamp
        self.value = value
        self.unit = unit



# TODO: Add your own classes here!


class Building:
    """
    Representerer selve bygningen som inneholder alle etasjer.
    """

    def __init__(self):
        """
        Oppretter en ny bygning med en tom liste over etasjer.
        """
        self.floors = []


class Floor:
    """
    Representerer en etasje i en bygning.
    """

    def __init__(self, level: int):
        """
        Oppretter en etasje med et spesifisert nivå (nummer) og en liste for rom.
        """
        self.level = level
        self.rooms = []


class Room:
    """
    Representerer et rom med et navn og et bestemt areal.
    """

    def __init__(self, floor: Floor, area: float, room_name: str = None):
        """
        Oppretter et rom tilknyttet en etasje, med størrelse og valgfritt navn.
        """
        self.floor = floor
        self.area = area
        self.room_name = room_name
        self.devices = [] # Liste over enheter i dette rommet


class Device:
    """
    Overordnet klasse for alle enheter i huset.
    """

    def __init__(self, device_id: str, supplier: str, model_name: str):
        """
        Oppretter et nytt rom med et spesifikt areal og navn.
        """
        self.id = device_id # Teknisk identifikator
        self.supplier = supplier # Produsentnavn
        self.model_name = model_name # Modellnavn
        self.room = None # Skal kobles til et rom senere


    def is_sensor(self):
        """
        Returnerer True hvis enheten er en sensor, ellers False.
        """
        return False


    def is_actuator(self):
        """
        Returnerer True hvis enheten er en aktuator, ellers False.
        """
        return False


    def get_device_type(self):
        """
        Returnerer en tekststreng som beskriver hvilken type enhet dette er.
        """
        return "Unknown Device"


class Sensor(Device):
    """
    Representerer en sensor som kan levere målinger.
    """

    def is_sensor(self):
        """
        Bekrefter at denne enheten er en sensor.
        """
        return True


    def last_measurement(self):
        """
        Returnerer det siste Measurement-objektet produsert av sensoren.
        """
        # Her vil du senere returnere et faktisk Measurement-objekt
        pass


class Actuator(Device):
    """
    Representerer en aktuator som kan utføre en handling.
    """

    def __init__(self, device_id: str, supplier: str, model_name: str):
        """
        Oppretter en aktuator og setter standardtilstanden til 'av'.
        """
        super().__init__(device_id, supplier, model_name)
        self.active = False
        self.target_value = None


    def is_actuator(self):
        """
        Bekrefter at denne enheten er en aktuator.
        """
        return True


    def turn_on(self, target_value = None):
        """
        Slår på enheten og setter eventuelt en ønsket målverdi.
        """
        self.active = True
        self.target_value = target_value


    def turn_off(self):
        """
        Slår av enheten.
        """
        self.active = False


    def is_active(self):
        """
        Sjekker om enheten for øyeblikket er slått på.
        """
        return self.active


class SmartHouse:
    """
    This class serves as the main entity and entry point for the SmartHouse system app.
    Do not delete this class nor its predefined methods since other parts of the
    application may depend on it (you are free to add as many new methods as you like, though).

    The SmartHouse class provides functionality to register rooms and floors (i.e. changing the 
    house's physical layout) as well as register and modify smart devices and their state.
    """

    def __init__(self):
        """
        Initialiserer et smarthus med en tom liste over etasjer.
        """
        self.floors = []


    def register_floor(self, level):
        """
        This method registers a new floor at the given level in the house
        and returns the respective floor object.
        """
        new_floor = Floor(level)
        self.floors.append(new_floor)
        return new_floor


    def register_room(self, floor, room_size, room_name = None):
        """
        This methods registers a new room with the given room areal size 
        at the given floor. Optionally the room may be assigned a mnemonic name.
        """
        new_room = Room(floor, room_size, room_name)
        floor.rooms.append(new_room)
        return new_room


    def get_floors(self):
        """
        This method returns the list of registered floors in the house.
        The list is ordered by the floor levels, e.g. if the house has 
        registered a basement (level=0), a ground floor (level=1) and a first floor 
        (leve=1), then the resulting list contains these three flors in the above order.
        """
        return sorted(self.floors, key = lambda f: f.level)


    def get_rooms(self):
        """
        This methods returns the list of all registered rooms in the house.
        The resulting list has no particular order.
        """
        all_rooms = []
        for floor in self.floors:
            all_rooms.extend(floor.rooms)
        return all_rooms


    def get_area(self):
        """
        This methods return the total area size of the house, i.e. the sum of the area sizes of each room in the house.
        """

        total_area = 0
        for room in self.get_rooms():
            total_area += room.area
        return total_area


    def register_device(self, room, device):
        """
        This methods registers a given device in a given room.
        """
        new_room = Room(floor, room_size, room_name)
        floor.rooms.append(new_room)
        return new_room

    
    def get_device(self, device_id):
        """
        This method retrieves a device object via its id.
        """

        for room in self.get_rooms():
            for device in room.devices:
                if device.id == device_id:
                    return device
        return None




