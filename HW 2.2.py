class Country:

	def __init__(self, name, cont):

		self.name = name
		self.continent = cont

	def present(self):
		
		return f"Country: {self.name}\nContinent: {self.continent}"

class Brand:

	def __init__(self, brand_name, start_date):

		self.brand_name = brand_name
		self.start_date = start_date

	def present(self):

		return f"Brand name: {self.brand_name}\nStarted date: {self.start_date}"

class Season:

	def __init__(self, season_name, aver_temp):

		self.season_name = season_name
		self.aver_temp = aver_temp

	def present(self):

		return f"The season: {self.season_name}\nAverage temperature: {aver_temp}"

class Product(Country, Brand, Season):

	def __init__(self, name, cont, brand_name, start_date, season_name, aver_temp, prod_name, prod_type, prod_price, prod_quant):
		
		self.product_name = prod_name
		self.product_type = prod_type
		self.product_price = prod_price
		self.product_quantity = prod_quant
		Country.__init__(self, name, cont)
		Brand.__init__(self, brand_name, start_date)
		Season.__init__(self, season_name, aver_temp)

	def present(self):

		return f"The main info about product\n{Country.present(self)}\n{Brand.present(self)}\nProduct name: {self.product_name}\nProduct type: {self.product_type}\nProduct price ($): {self.product_price}\nProduct quantity: {self.product_quantity}\nTotal price:{self.product_price * self.product_quantity}"

	def discount_product(self, disc_rate):

		self.disc_rate = disc_rate
		self.disc_price = self.product_price * (1-self.disc_rate/100)

		return f"Price:{self.product_price}\nDiscount rate: {self.disc_rate}\nPrice after discount: {self.disc_price}\nTotal price after discount: {self.disc_price * self.product_quantity}"

	def increase_quantity(self, increase_quant):

		self.product_quantity += increase_quant

		return f"Your quantity is increase by {increase_quant}\nNow your total quantity: {self.product_quantity}\nTotal price after discount: {self.disc_price * self.product_quantity}"

	def decrease_quantity(self, decrease_quant):

		self.product_quantity -= decrease_quant

		return f"Your quantity is decrease by {decrease_quant}\nNow your total quantity: {self.product_quantity}\nTotal price after discount: {self.disc_price * self.product_quantity}"


print("Present product")
product_1 = Product("Spain","Europe","Zara", 1974 , "summer", 20, "T-shirts", "clotes", 50, 2)
print(product_1.present())
print("-----------")
print("Discount price")
product_1.disc_rate = 5
print(product_1.discount_product(5))
print("-----------") 
print("Increase quantity")
print(product_1.increase_quantity(3))
print("-----------")
print("Decrease quantity")
print(product_1.decrease_quantity(1))