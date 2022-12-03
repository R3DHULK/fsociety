import csv
from faker import Faker
import datetime
import os
os.system("clear")
print('''
 ****************************************************
 *  _        _   _      ___     _         ___ _     *
 * | |   ___| |_( )___ | __|_ _| |_____  |_ _| |_   *
 * | |__/ -_)  _|/(_-< | _/ _` | / / -_)  | ||  _|  *
 * |____\___|\__| /__/ |_|\__,_|_\_\___| |___|\__|  *
 *                                                  *
 *        File Faking Tool                          *
 *       (this support any file format)             *                           
 *       https://github.com/R3DHULK                 *
 *                                                  *
 ****************************************************
''')
try :
	def datagenerate(records, headers):
		fake = Faker('en_US')
		fake1 = Faker('en_GB')   # To generate phone numbers
		with open(input(" [+] ENTER FILE NAME TO STORE OUTPUT : "), 'wt') as csvFile:
			print("\n [+] Data is faking....\n [*] Please Wait...\n")
			writer = csv.DictWriter(csvFile, fieldnames=headers)
			writer.writeheader()
			for i in range(records):
				full_name = fake.name()
				FLname = full_name.split(" ")
				Fname = FLname[0]
				Lname = FLname[1]
				domain_name = "@gmail.com"
				userId = Fname +"."+ Lname + domain_name
            
				writer.writerow({
						"Email Id" : userId,
						"Prefix" : fake.prefix(),
						"Name": fake.name(),
						"Birth Date" : fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1,1)),
						"Phone Number" : fake1.phone_number(),
						"Additional Email Id": fake.email(),
						"Address" : fake.address(),
						"Zip Code" : fake.zipcode(),
						"City" : fake.city(),
						"State" : fake.state(),
						"Country" : fake.country(),
						"Year":fake.year(),
						"Time": fake.time(),
						"Link": fake.url(),
						"Text": fake.word(),
						})
    
	if __name__ == '__main__':
		records = 10000
		headers = ["Email Id", "Prefix", "Name", "Birth Date", "Phone Number", "Additional Email Id",
				"Address", "Zip Code", "City","State", "Country", "Year", "Time", "Link", "Text"]
		datagenerate(records, headers)
		print("\n [*] fake data generation is completed ! \n")
	else :
		print(" [!] Unsuccessful to generate ! ")
except KeyboardInterrupt:
	print("\n [-] Ctrl + C Detected.........Exiting\n")
input(" Enter To Exit ")
os.system("clear")
