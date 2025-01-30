class Route:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    @property
    def total_distance_km(self):
        return self._total_distance_km
    
    @total_distance_km.setter
    def total_distance_km(self, value):
        if not value:
            raise ValueError("Distance KMcannot be empty")
        if not isinstance(value, (int, float)):
            raise ValueError("Distance KM must be a number")
        self._total_distance_km = value

    @property
    def total_distance_miles(self):
        return self.total_distance_miles
    
    @total_distance_miles.setter
    def total_distance_miles(self, value):
        if not value:
            raise ValueError("Distance miles cannot be empty")
        if not isinstance(value, (int, float)):
            raise ValueError("Distance miles must be a number")
        self._total_distance_miles = value

    @property
    def slochd_point_km(self):
        return self._slochd_point_km
    
    @slochd_point_km.setter
    def slochd_point_km(self, value):
        if not value:
            raise ValueError("Slochd point KM cannot be empty")
        if not isinstance(value, (int, float)):
            raise ValueError("Slochd point must be a number")
        self._slochd_point_km = value

    @property
    def slochd_point_miles(self):
        return self._slochd_point_miles
    
    @slochd_point_miles.setter
    def slochd_point_miles(self, value):
        if not value:
            raise ValueError("Slochd point miles cannot be empty")
        if not isinstance(value, (int, float)):
            raise ValueError("Slochd point must be a number")
        self._slochd_point_miles = value