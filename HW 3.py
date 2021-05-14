class Hotel:

    def __init__(self, name, place, rooms_mid, mid_room_price, rooms_lux, lux_room_price):

        self.name = name
        self.place = place
        self.rooms_mid = rooms_mid
        self.mid_room_price = mid_room_price
        self.rooms_lux = rooms_lux
        self.lux_room_price = lux_room_price


    def booking(self):
        
        option = input("What type of rooms do you want to book? mid/lux ")
        if option == 'mid':
            answer = input(f"Which room do you want to book:\n{self.rooms_mid} 1/2/3 ")
            self.rooms_mid['room' + str(answer)] = "busy"

            return self.rooms_mid

        if option == 'lux':
            answer = input(f"Which room do you want to book:\n{self.rooms_lux} 1/2/3 ")
            self.rooms_lux['room'+ str(answer)] = "busy"

            return self.rooms_lux

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

        answer1 = input("Hi.What type of room do you want to check? mid/lux ")
        print(self.rooms_mid)
        answer2 = input("Which number of room? 1/2/3 ")
        if answer1 == 'mid':
            if self.rooms_mid['room'+ str(answer2)] == "free":
                return "Great. It's free"
            else:
                return "Sorry. It's busy"
        elif answer1 == 'lux':
            if self.rooms_lux['room'+ str(answer2)] == "free":
                return "Great. It's free"
            else:
                return "Sorry. It's busy"
        else:
            return "We don't have that types of room"

    def discount(self, disc_room_price):
        self.disc_room_price = disc_room_price
        answer3 = input("What type of room did you choose? mid/lux ")
        if answer3 == 'mid':
            return f"You discount price of room for mid: {self.mid_room_price * (1-(self.disc_room_price/100))}"
        elif answer3 == 'lux':
            return f"You discount price of room for lux: {self.lux_room_price * (1-(self.disc_room_price/100))}"
        else:
            return "We can't discount your room"


    def representation_hotel(self):


        return f"Hotel name: {self.name}\nHotel place: {self.place}\nMid room availability: {self.rooms_mid}\nMid rooms price: {self.mid_room_price}\nLux room availability: {self.rooms_lux}\nLux rooms price: {self.lux_room_price}"


    
hotel1 = Hotel("Apaga resort", "Tavush", dict(room1 = 'free', room2 = 'free', room3 = 'free'), 30000, dict( room1 = 'free', room2 = 'free', room3 = 'free'), 50000)
# print(hotel1.booking())
# print(hotel1.available_room_check())
# print(hotel1.discount(5))
# print(hotel1.representation_hotel())
# print(hotel1.available_list_mid())
# print(hotel1.available_list_lux())


class Taxi:

    def __init__(self, car_types, price_for_tour):
        self.car_types = car_types
        self.price_for_tour = price_for_tour


    def discount_taxi(self, disc_rate):
        self.disc_rate = disc_rate
        
        return f"Discoint price for tour: {self.price_for_tour * (1-(self.disc_rate/100))}"

    def representation_taxi(self):

        return f"Car types: {self.car_types}\nPrice for tour: {self.price_for_tour}"

    

taxi1 = Taxi("BMW", 5000)
# print(taxi1.discount(10))
# print(taxi1.representation_taxi())

class Tour(Hotel, Taxi):

    def __init__(self, name, place, rooms_mid, mid_room_price, rooms_lux, lux_room_price, car_types, price_for_tour):
        self.name = name
        
        Hotel.__init__(self, name, place, rooms_mid, mid_room_price, rooms_lux, lux_room_price)
        Taxi.__init__(self, car_types, price_for_tour)

        
    def representation(self):
        
        price_for_one_person_lux = self.lux_room_price + self.price_for_tour
        price_for_one_person_mid = self.mid_room_price + self.price_for_tour

        return f"Out tour company's offers:\nHotel {self.name} located in {self.place}.We have two types of rooms mid and lux, now from mid rooms are available: {self.available_list_mid()} and lux: {self.available_list_lux()} which prices are {self.mid_room_price} and {self.lux_room_price}. Without that you can take {self.car_types} taxi which price is {self.price_for_tour}. Lux tour for one person {price_for_one_person_lux} and mid tour: {price_for_one_person_mid}"

tour1 = Tour("Apaga resort", "Tavush", dict(room1 = 'free', room2 = 'free', room3 = 'free'), 30000, dict( room1 = 'free', room2 = 'free', room3 = 'free'), 50000, "BMW", 15000)
print(tour1.representation())
