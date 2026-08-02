import sqlite3
import random
import matplotlib.pyplot as plt

#Creates a database
def create_database():

    #Creates and opens the database
    conn = sqlite3.connect("population_NB.db")
    cur = conn.cursor()

    #Ensures teh table has three columns
    cur.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    """)

    #Stores the cities with their population values
    cities_2023 = {
        "Miami": 449514,
        "Orlando": 316081,
        "Tampa": 409374,
        "Jacksonville": 971319,
        "St. Petersburg": 258308,
        "Hialeah": 220491,
        "Tallahassee": 204523,
        "Fort Lauderdale": 186208,
        "Cape Coral": 216992,
        "Sarasota": 57848
    }

    #Each entry is inserted into the database
    for city, pop in cities_2023.items():
        cur.execute("INSERT INTO population VALUES (?, ?, ?)", (city, 2023, pop))

    conn.commit()
    conn.close()


#Simulates growth/decline
def simulate_population():
    conn = sqlite3.connect("population_NB.db")
    cur = conn.cursor()

    #Gives a list of the city and population
    cur.execute("SELECT city, population FROM population WHERE year = 2023")
    rows = cur.fetchall()

    for city, pop in rows:
        current_pop = pop

        #Simulates 20 years of population growth/decline
        for year in range(2024, 2044):
            rate = random.uniform(-0.03, 0.05)
            current_pop = int(current_pop * (1 + rate))

            #Inserts each year's result
            cur.execute("INSERT INTO population VALUES (?, ?, ?)",
                        (city, year, current_pop))

    conn.commit()
    conn.close()

#Displays a graph for the selected city
def plot_city_population():
    conn = sqlite3.connect("population_NB.db")
    cur = conn.cursor()

    #Gets the list of the 10 cities
    cur.execute("SELECT DISTINCT city FROM population")
    cities = [row[0] for row in cur.fetchall()]

    #Allows the user to choose a city
    print("\nChoose a city to display population growth:\n")
    for i, city in enumerate(cities, 1):
        print(f"{i}. {city}")

    choice = int(input("\nEnter number: "))
    selected_city = cities[choice - 1]

    #Returns a list of the year and population
    cur.execute("SELECT year, population FROM population WHERE city = ? ORDER BY year",
                (selected_city,))
    data = cur.fetchall()

    years = [row[0] for row in data]
    pops = [row[1] for row in data]

    #Plots data
    plt.figure(figsize=(10, 5))
    plt.plot(years, pops, marker='o')
    plt.title(f"Population Growth for {selected_city}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.show()

    conn.close()



create_database()
simulate_population()
plot_city_population()