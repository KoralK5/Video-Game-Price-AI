import pandas
from sklearn import linear_model

#pricecharting.com

df = pandas.read_csv("stats.csv")
x = df[['Timeline', 'Loose_Price1', 'Loose_Price2', 'Loose_Price3','Loose_Price4','Loose_Price5', 'Age']]
y = df['Loose_Price']
z = []

regr = linear_model.LinearRegression()
regr.fit(x, y)

print("PREDICT AN ANTIQUE VIDEO GAME'S COST IN THE FUTURE!")
print("")
print("Respond to each statement to get a cost prediction in the set date.")
print("Make sure the prices are equally apart in date, 5 being the nearest.")
print("")
print("")

Current_Year = float(input("Current Year: "))
Desired_Year = float(input("Future Year: "))
Release_Year = float(input("Release Year: "))
Loose_Price5 = float(input("Price 5: "))
Loose_Price4 = float(input("Price 4: "))
Loose_Price3 = float(input("Price 3: "))
Loose_Price2 = float(input("Price 2: "))
Loose_Price1 = float(input("Price 1: "))
Timeline = Desired_Year - Current_Year
Age = Current_Year - Release_Year
print("")

z.append(Timeline)
z.append(Loose_Price1)
z.append(Loose_Price2)
z.append(Loose_Price3)
z.append(Loose_Price4)
z.append(Loose_Price5)
z.append(Age)

Loose_Price = (regr.predict([z]))

if Loose_Price[0] < Loose_Price5:
	complete_color = "🔽 🔴 🔽"
elif Loose_Price[0] > Loose_Price5:
	complete_color = "🔼 🟢 🔼"
else:
	complete_color = "⏹️ 🟡 ⏹️"

print("")
print("Price Change: {}".format(Loose_Price - Loose_Price5))
print("")
print("Price: {} {}{}".format(complete_color,Loose_Price,complete_color))
print("")
print("")

respc = float(input("Please provide the 'pricecharting.com' complete price: "))

if respc != ():
	with open('stats.csv','a') as file:
		file.write("\n{},".format(respc))
		file.write("{},".format(Timeline))
		file.write("{},".format(Loose_Price1))
		file.write("{},".format(Loose_Price2))
		file.write("{},".format(Loose_Price3))
		file.write("{},".format(Loose_Price4))
		file.write("{},".format(Loose_Price5))
		file.write("{}".format(Age))

print("")
print("Thank You!")
