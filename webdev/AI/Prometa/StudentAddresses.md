Create Python code to generate 10 random street addresses.

    import random

    streets = ["Main Street", "Oak Avenue", "Elm Street", "Maple Avenue", "Cedar Road", "Pine Street", "Willow Lane", "Birch Avenue", "Spruce Road", "Ash Street"]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]

    def generate_random_address():
        street_number = random.randint(1, 999)
        street_name = random.choice(streets)
        city = random.choice(cities)
        return f"{street_number} {street_name}, {city}"

    for _ in range(10):
        address = generate_random_address()
        print(address)
