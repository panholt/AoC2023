class Range:

    def __init__(self, dst, src, size):
        self.source_start = src
        self.destination_start = dst
        self.size = size 

    def in_range(self, number):
        return number >= self.source_start and number <= self.source_start + self.size 
    
    def find_destination(self, number):
        return self.destination_start + (number - self.source_start)

    def __repr__(self):
        return f'Range(Source Start: {self.source_start}, Dest Start: {self.destination_start}, Size: {self.size})'


class Alamanac:

    def __init__(self):
        self.seeds = []
        self.seed_to_soil = []
        self.soil_to_fertilizer = []
        self.fertilizer_to_water = []
        self.water_to_light = []
        self.light_to_temperature = []
        self.temperature_to_humidity = []
        self.humidity_to_location = []
        self.process_input()

    
    def process_input(self):
         with open('inputs/day5.txt') as f:
            current_key = None
            for line in f.readlines():
                if line == '\n':
                    current_key = None
                elif 'seeds:' in line:
                    line = line.replace('seeds: ', '')
                    self.seeds = [int(x) for x in line.split()]
                elif 'map:' in line:
                    current_key = getattr(self, line.strip().
                                                replace(' map:', '').
                                                replace('-', '_'))
                else:
                    dst,src,size = [int(x) for x in line.split()]
                    current_key.append(Range(dst, src, size))

    def find_destination(self, maps, item):
        for r in maps:
            if r.in_range(item):
                result =  r.find_destination(item)
                return result
        return item

    def find_location_for_seed(self, seed):
        soil = self.find_destination(self.seed_to_soil, seed)
        fertilizer = self.find_destination(self.soil_to_fertilizer, soil)
        water = self.find_destination(self.fertilizer_to_water, fertilizer)
        light = self.find_destination(self.water_to_light, water)
        temperature = self.find_destination(self.light_to_temperature, light)
        humidity = self.find_destination(self.temperature_to_humidity, temperature)
        location = self.find_destination(self.humidity_to_location, humidity)
        return location

alamanac = Alamanac()
locations = []
for seed in alamanac.seeds:
    locations.append(alamanac.find_location_for_seed(seed))
print(min(locations))