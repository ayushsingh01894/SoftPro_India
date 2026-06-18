class AutoRide:
    def __init__(self, distance_km):
        self.distance_km = distance_km

    def fare(self):
        return 30 + 12 * self.distance_km
    
    def summary(self):
        return f"{self.distance_km} km ride: Rs {self.fare()}"

ride = AutoRide(5)
print(ride.summary())


import statistics

scores = [42, 88, 15, 73, 96, 50]

print("Highest:", max(scores))
print("Lowest:", min(scores))
print("Average:", statistics.mean(scores))

def read_age(text):
    try:
        age = int(text)
        if age < 0:
            return "invalid"
            return age
    except ValueError:
        return "invalid"

print(read_age("21"))
print(read_age("abc"))
print(read_age("-5"))


        

        
