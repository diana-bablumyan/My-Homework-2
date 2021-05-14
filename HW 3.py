class Hotel:

    def __init__(self, name, place, rooms_mid, mid_room_price, rooms_lux, lux_room_price):

        self.name = name
        self.place = place
        self.rooms_mid = rooms_mid
        self.mid_room_price = mid_room_price
        self.rooms_lux = rooms_lux
        self.lux_room_price = lux_room_price


    def booking(self):
        
        option = input("We have two types of room.What type do you want to book (Mid/Lux)? ")
        if option.lower() == 'mid':
            answer = input(f"Okey. Our free rooms are {self.available_list_mid()}.Which number of room do you want to book (1,2,3): ")
            self.rooms_mid['room' + str(answer)] = "busy"

            return f"Thank you. You book room N{answer}.We will wait you!"

        if option.lower() == 'lux':
            answer = input(f"Okey. Our free rooms are {self.available_list_lux()}. which number of room do you want to book (1,2,3): ")
            self.rooms_lux['room'+ str(answer)] = "busy"

            return f"Thank you. You book room N{answer}.We will wait you!"

    def available_list_mid(self):
        number_avail_mid = []
        for i in self.rooms_mid.keys():
            if self.rooms_mid[i] == 'free':
                number_avail_mid.append(i)
        return number_avail_mid

    def available_list_lux(self):
        number_avail_lux = []
        for i in self.rooms_lux.keys():
            if self.rooms_lux[i] == 'free':
                number_avail_lux.append(i)
        return number_avail_lux         
 
    def available_room_check(self):

        answer1 = input("Hi.We have two types of room.What type do you want to check (Mid/Lux)? ")
        answer2 = input("Okey.Which number of room (1/2/3)? ")
        if answer1.lower() == 'mid':
            if self.rooms_mid['room'+ str(answer2)] == "free":
                return "Great. It's free. You can book it if you want!"
            else:
                return "Sorry. It's busy"
        elif answer1.lower() == 'lux':
            if self.rooms_lux['room'+ str(answer2)] == "free":
                return "Great. It's free. You can book it if you want!"
            else:
                return "Sorry. It's busy"
        else:
            return "Sorry. We have only two types of room"

    def discount_rooms(self, disc_room_price):
        self.disc_room_price = disc_room_price
        answer3 = input("What type of room did you choose (Mid/Lux). We can offer you discount as a special client? ")
        if answer3.lower() == 'mid':
            return f"Your discount room price worth: {self.mid_room_price * (1-(self.disc_room_price/100))}"
        elif answer3.lower() == 'lux':
            return f"Your discount room price worth: {self.lux_room_price * (1-(self.disc_room_price/100))}"
        else:
            return "Sorry.We can't discount your room"

    def presentation_hotel(self):


        return f"Hotel name: {self.name}\nHotel place: {self.place}\nMid rooms list and availability: {self.rooms_mid}\nMid rooms price: {self.mid_room_price}\nLux rooms list and availability: {self.rooms_lux}\nLux rooms price: {self.lux_room_price}"


    
hotel1 = Hotel("Apaga resort", "Tavush", dict(room1 = 'free', room2 = 'free', room3 = 'free'), 30000, dict( room1 = 'free', room2 = 'free', room3 = 'free'), 50000)

###Cheks for Hotel class###

# print(hotel1.booking())
# print(hotel1.available_list_mid())
# print(hotel1.available_list_lux())
# print(hotel1.available_room_check())
# print(hotel1.discount_rooms(5))
# print(hotel1.presentation_hotel())



class Taxi:

    def __init__(self, car_types, price_for_tour):
        self.car_types = car_types
        self.price_for_tour = price_for_tour

    def discount_taxi(self, disc_rate):
        self.disc_rate = disc_rate
        
        return f"Price for tour worth {self.price_for_tour}. But we can discoint price for tour and its will worth {self.price_for_tour * (1-(self.disc_rate/100))}"

    def presentation_taxi(self):

        return f"Car's type: {self.car_types}\nPrice for tour: {self.price_for_tour}\nDiscount price for tour {self.price_for_tour * (1-(self.disc_rate/100))}"

    

taxi1 = Taxi("BMW", 5000)

###Checks for Taxi class

# print(taxi1.discount_taxi(10))
# print(taxi1.presentation_taxi())

class Tour(Hotel, Taxi):

    def __init__(self, name, place, rooms_mid, mid_room_price, rooms_lux, lux_room_price, car_types, price_for_tour):
        self.name = name
        
        Hotel.__init__(self, name, place, rooms_mid, mid_room_price, rooms_lux, lux_room_price)
        Taxi.__init__(self, car_types, price_for_tour)
        
    def presentation(self):
        
        price_for_one_person_lux = self.lux_room_price + self.price_for_tour
        price_for_one_person_mid = self.mid_room_price + self.price_for_tour

        return f"Hi. I will present you our tour company's offers:\nHotel {self.name} located in {self.place}.There we have two types of rooms Mid and Lux, now from mid rooms are available: {self.available_list_mid()} and lux: {self.available_list_lux()} which prices are {self.mid_room_price} and {self.lux_room_price}. Without that you can take {self.car_types} taxi which price is {self.price_for_tour}. Lux tour for one person worth {price_for_one_person_lux} and mid tour: {price_for_one_person_mid}.We will be happy to host you here!!"

tour1 = Tour("Apaga resort", "Tavush", dict(room1 = 'free', room2 = 'free', room3 = 'free'), 30000, dict( room1 = 'free', room2 = 'free', room3 = 'free'), 50000, "BMW", 15000)

# print(tour1.presentation())
# print(tour1.booking())
# print(tour1.available_room_check())
# print(tour1.discount_rooms(10))
