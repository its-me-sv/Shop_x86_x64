import socket 
from os import path, makedirs
import csv
from datetime import datetime
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from random import randint

def Initialise():
    if not path.exists("C:\\Projects\\Python\\Shopping\\Customers"):
        makedirs("C:\\Projects\\Python\\Shopping\\Customers")
    if not path.exists("C:\\Projects\\Python\\Shopping\\Customers\\customer_usernames.txt"):
        file = open("C:\\Projects\\Python\\Shopping\\Customers\\customer_usernames.txt", "w")
        file.write("USERNAMES\n")
        file.close()
    if not path.exists("C:\\Projects\\Python\\Shopping\\Customers\\customer_emails.txt"):
        file = open("C:\\Projects\\Python\\Shopping\\Customers\\customer_emails.txt", "w")
        file.write("EMAILS\n")
        file.close()
    if not path.exists("C:\\Projects\\Python\\Shopping\\Customers\\customer_passwords.txt"):
        file = open("C:\\Projects\\Python\\Shopping\\Customers\\customer_passwords.txt", "w")
        file.write("PASSWORDS\n")
        file.close()
    if not path.exists("C:\\Projects\\Python\\Shopping\\Customers\\Cart"):
    	makedirs("C:\\Projects\\Python\\Shopping\\Customers\\Cart")

    if not path.exists("C:\\Projects\\Python\\Shopping\\Sellers"):
        makedirs("C:\\Projects\\Python\\Shopping\\Sellers")
    if not path.exists("C:\\Projects\\Python\\Shopping\\Sellers\\seller_shop_names.txt"):
        file = open("C:\\Projects\\Python\\Shopping\\Sellers\\seller_shop_names.txt", "w")
        file.write("SHOP_NAMES\n")
        file.close()
    if not path.exists("C:\\Projects\\Python\\Shopping\\Sellers\\seller_emails.txt"):
        file = open("C:\\Projects\\Python\\Shopping\\Sellers\\seller_emails.txt", "w")
        file.write("EMAILS\n")
        file.close()
    if not path.exists("C:\\Projects\\Python\\Shopping\\Sellers\\seller_passwords.txt"):
        file = open("C:\\Projects\\Python\\Shopping\\Sellers\\seller_passwords.txt", "w")
        file.write("PASSWORDS\n")
        file.close()

    if not path.exists("C:\\Projects\\Python\\Shopping\\Warehouse"):
        makedirs("C:\\Projects\\Python\\Shopping\\Warehouse")
    if not path.exists("C:\\Projects\\Python\\Shopping\\Warehouse\\categories.txt"):
        file = open("C:\\Projects\\Python\\Shopping\\Warehouse\\categories.txt", "w")
        category_list = ["All_Departments", "Arts_And_Crafts", "Automotive", "Baby", "Beauty_And_Personal", "Books", "Computers", "Electronics", "Women's_Fashion", "Men's_Fashion"]
        category_list2 = ["Girls_Fashion", "Boy's Fashion", "Health_And_Household", "Home_And_Kitchen", "Idustrial_And_Scientific", "Luggage", "Pet_Supplies", "Sports", "Tools", "Toys"]
        fields = ["PNAME", "PPRICE", "PDESC", "SELLN"]
        loc = "C:\\Projects\\Python\\Shopping\\Warehouse\\"
        for c in category_list:
            file.write(c+"\n")
            with open(loc+c+".csv", 'a', newline = '') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(fields)
        for d in category_list2:
            file.write(d+"\n")
            with open(loc+d+".csv", 'a', newline = '') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(fields)
        file.close()

def Internet_Available():
    ip_address = socket.gethostbyname(socket.gethostname())
    if ip_address == "127.0.0.1":
        return False
    return True

class Customer_Details():
	def __init__(self):
		self.username = ""
		self.email = ""
		self.password = ""

	def From_File_Username(self, USERNAME):
		file = open("C:\\Projects\\Python\\Shopping\\Customers\\customer_usernames.txt")
		to_return = False
		for line in file.readlines():
			if line.rstrip() == USERNAME:
				to_return = True
				break
		file.close()
		return to_return

	def From_File_Email(self, EMAIL):
		file = open("C:\\Projects\\Python\\Shopping\\Customers\\customer_emails.txt")
		to_return = False
		for line in file.readlines():
			if line.rstrip() == EMAIL:
				to_return = True
				break
		file.close()
		return to_return

	def From_File_Password(self, PASSWORD):
		file = open("C:\\Projects\\Python\\Shopping\\Customers\\customer_passwords.txt")
		to_return = False
		for line in file.readlines():
			if line.rstrip() == PASSWORD:
				to_return = True
				break
		file.close()
		return to_return

	def Assign(self, USERNAME, EMAIL, PASSWORD):
		self.username = USERNAME[:]
		self.email = EMAIL[:]
		self.password = PASSWORD[:]

	def File_Write_All(self):
		file = open("C:\\Projects\\Python\\Shopping\\Customers\\customer_usernames.txt", "a+")
		file.write(self.username+"\n")
		file.close()
		del file

		file = open("C:\\Projects\\Python\\Shopping\\Customers\\customer_emails.txt", "a+")
		file.write(self.email+"\n")
		file.close()
		del file

		file = open("C:\\Projects\\Python\\Shopping\\Customers\\customer_passwords.txt", "a+")
		file.write(self.password+"\n")
		file.close()
		del file

class Seller_Details():
	def __init__(self):
		self.shop_name = ""
		self.email = ""
		self.password = ""

	def From_File_SHOP_NAME(self, SHOP_NAME):
		file = open("C:\\Projects\\Python\\Shopping\\Sellers\\seller_shop_names.txt")
		to_return = False
		for line in file.readlines():
			if line.rstrip() == SHOP_NAME:
				to_return = True
				break
		file.close()
		return to_return

	def From_File_Email(self, EMAIL):
		file = open("C:\\Projects\\Python\\Shopping\\Sellers\\seller_emails.txt")
		to_return = False
		for line in file.readlines():
			if line.rstrip() == EMAIL:
				to_return = True
				break
		file.close()
		return to_return

	def From_File_Password(self, PASSWORD):
		file = open("C:\\Projects\\Python\\Shopping\\Sellers\\seller_passwords.txt")
		to_return = False
		for line in file.readlines():
			if line.rstrip() == PASSWORD:
				to_return = True
				break
		file.close()
		return to_return

	def Assign(self, SHOP_NAME, EMAIL, PASSWORD):
		self.shop_name = SHOP_NAME[:]
		self.email = EMAIL[:]
		self.password = PASSWORD[:]

	def File_Write_All(self):
		file = open("C:\\Projects\\Python\\Shopping\\Sellers\\seller_shop_names.txt", "a+")
		file.write(self.shop_name+"\n")
		file.close()
		del file

		file = open("C:\\Projects\\Python\\Shopping\\Sellers\\seller_emails.txt", "a+")
		file.write(self.email+"\n")
		file.close()
		del file

		file = open("C:\\Projects\\Python\\Shopping\\Sellers\\seller_passwords.txt", "a+")
		file.write(self.password+"\n")
		file.close()
		del file

class Invalid_Username(Exception):
	'''This Exception Is Raised When The User Enter's
	Invalid Username.'''
	pass

class Username_Taken(Exception):
	'''This Exception Is Raised When The Username Is 
	Already Taken.'''
	pass

class Email_Taken(Exception):
	'''This Exception Is Raised When The Email Is
	Already Taken.'''
	pass

class Password_Not_Match(Exception):
	'''This Exception Is Raised When The Passwords Did Not
	Match With Each Other.'''
	pass

class Invalid_Email(Exception):
	'''This Exception Is Raised When The Email Is Not
	An Valid Email.'''
	pass

def Current_Time_Date():
	return datetime.now().strftime("%A %B %d, %I:%M %p, %Y")

def First_Write(Info, t = 0):
	if t == 0:
		loc = "C:\\Projects\\Python\\Shopping\\Customers\\all_customers.csv"
	else:
		loc = "C:\\Projects\\Python\\Shopping\\Sellers\\all_sellers.csv"
	
	with open(loc, 'a', newline = '') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(Info)

def Customer_Registration_Mail(to_send, name):
	sender_email = "YOUR EMAIL"
	receiver_email = to_send[:]

	message = MIMEMultipart()

	message["From"] = sender_email
	message["To"] = receiver_email
	message["Subject"] = "Registration At Shop"
	body = "Dear {},\n Your Account At Shop As Customer Has Been Created Successfully.\nRegards,\nThe Shop Customer Team".format(name)
	message.attach(MIMEText(body,'plain'))

	my_message = message.as_string()

	context = ssl.create_default_context()
	with smtplib.SMTP("smtp.gmail.com", 587) as server:
	    server.ehlo()  # Can be omitted
	    server.starttls(context=context)
	    server.ehlo()  # Can be omitted
	    server.login(sender_email, "YOUR PASSWORD")
	    server.sendmail(sender_email, receiver_email, my_message)

def Seller_Registration_Mail(to_send, name, shopp):
	sender_email = "YOUR EMAIL"
	receiver_email = to_send[:]

	message = MIMEMultipart()

	message["From"] = sender_email
	message["To"] = receiver_email
	message["Subject"] = "Registration At Shop"
	body = "Dear {},\n Your Account At Shop As Seller Has Been Created Successfully.\n{} Is Now A Part Of The Shop.\nRegards,\nThe Shop Seller Team".format(name, shopp)
	message.attach(MIMEText(body,'plain'))

	my_message = message.as_string()

	context = ssl.create_default_context()
	with smtplib.SMTP("smtp.gmail.com", 587) as server:
	    server.ehlo()  # Can be omitted
	    server.starttls(context=context)
	    server.ehlo()  # Can be omitted
	    server.login(sender_email, "YOUR PASSWORD")
	    server.sendmail(sender_email, receiver_email, my_message)

def Customer_Seller_Log_In_Checking(uname_email, password, cs):
	if not cs:
		file = open("C:\\Projects\\Python\\Shopping\\Customers\\all_customers.csv")
	else:
		file = open("C:\\Projects\\Python\\Shopping\\Sellers\\all_sellers.csv")
	all_customers_details = list(csv.reader(file))[:]
	file.close()

	for user_profile in all_customers_details:
		if uname_email == user_profile[1] or uname_email == user_profile[2]:
			if password == user_profile[-1]:
				return 1
	return 0

def Generate_Validation_Key():
	return "".join([chr(randint(65, 90)) for x in range(14)])

def Send_Validation_Email(mail_to_send, key_to_send):
	sender_email = "YOUR EMAIL"
	receiver_email = mail_to_send[:]

	message = MIMEMultipart()

	message["From"] = sender_email
	message["To"] = receiver_email
	message["Subject"] = "Password Reset At Shop"
	body = "{} Is Your Validation Key To Reset Password.\nThe Key Is Case Sensitive.\nRegards,\nThe Shop Team".format(key_to_send)

	message.attach(MIMEText(body,'plain'))

	my_message = message.as_string()

	context = ssl.create_default_context()
	with smtplib.SMTP("smtp.gmail.com", 587) as server:
		server.ehlo()
		server.starttls(context = context)
		server.ehlo()
		server.login(sender_email, "YOUR PASSWORD")
		server.sendmail(sender_email, receiver_email, my_message)

class Wrong_Validation_Key(Exception):
	'''This Exception Is Raised When The User Enter's
	Wrong Validation Key'''
	pass

def Setting_New_Password(new_password, changer_email, code):
	if not code:
		file = open("C:\\Projects\\Python\\Shopping\\Customers\\all_customers.csv")
	else:
		file = open("C:\\Projects\\Python\\Shopping\\Sellers\\all_sellers.csv")
	all_customers_details = list(csv.reader(file))[:]
	file.close()

	for user_profile in all_customers_details:
		if changer_email == user_profile[2]:
			user_profile[-1] = new_password[:]

	if not code:
		file_name = "C:\\Projects\\Python\\Shopping\\Customers\\all_customers.csv"
	else:
		file_name = "C:\\Projects\\Python\\Shopping\\Sellers\\all_sellers.csv"

	file_to_clear = open(file_name, "w+")
	file_to_clear.close()

	with open(file_name, 'a', newline = '') as csvfile:
		csvwriter = csv.writer(csvfile)
		for contents in all_customers_details:
			csvwriter.writerow(contents)
	
class No_Internet(Exception):
	'''This Exception Is Raised When The User Is Not 
	Connected To The Internet'''
	pass

def Retrieve_User_Details(info, code):
	if not code:
		file_loc = "C:\\Projects\\Python\\Shopping\\Customers\\all_customers.csv"
	else:
		file_loc = "C:\\Projects\\Python\\Shopping\\Sellers\\all_sellers.csv"

	file = open(file_loc)
	all_details = list(csv.reader(file))
	file.close()

	for detail in all_details:
		if info == detail[1] or info == detail[2]:
			return detail

def Retrieve_User_Pos(user_email, code):
	if not code:
		loc = "C:\\Projects\\Python\\Shopping\\Customers\\all_customers.csv"
	else:
		loc = "C:\\Projects\\Python\\Shopping\\Sellers\\all_sellers.csv"
	file = open(loc)
	all_details = list(csv.reader(file))
	file.close()
	pos = 0

	for detail in all_details:
		if user_email == detail[2] or user_email == detail[1]:
			return pos
		pos += 1

def Remove_Old_Replace_New(code, old_value, new_value):
	if not code:
		file_loc = "C:\\Projects\\Python\\Shopping\\Customers\\customer_usernames.txt"
	elif code == 1:
		file_loc = "C:\\Projects\\Python\\Shopping\\Customers\\customer_emails.txt"
	elif code == 2:
		file_loc = "C:\\Projects\\Python\\Shopping\\Sellers\\seller_shop_names.txt"
	elif code == 3:
		file_loc = "C:\\Projects\\Python\\Shopping\\Sellers\\seller_emails.txt"
	file = open(file_loc)
	contents = list()
	for line in file.readlines():
		contents.append(line.rstrip())
	file.close()
	file = open(file_loc, "w+")
	for i in range(len(contents)):
		if contents[i] == old_value:
			contents[i] = new_value
		file.write(contents[i]+"\n")
	file.close()

def Change_The_Detail_In_File(code, user_pos, utility_no, value):
	if not code:
		loc = "C:\\Projects\\Python\\Shopping\\Customers\\all_customers.csv"
	else:
		loc = "C:\\Projects\\Python\\Shopping\\Sellers\\all_sellers.csv"
	file = open(loc)
	all_details = list(csv.reader(file))
	file.close()
	file=open(loc, "w+")
	file.close()
	if not utility_no:
		all_details[user_pos][0] = value
	elif utility_no == 1:
		all_details[user_pos][1] = value
	elif utility_no == 2:
		all_details[user_pos][2] = value
	elif utility_no == -1:
		all_details[user_pos][-1] = value
	elif utility_no == 3:
		all_details[user_pos][3] = value
	with open(loc, 'a', newline ='') as csvfile:
		csvwriter = csv.writer(csvfile)
		for contents in all_details:
			csvwriter.writerow(contents)

def Content_To_Write_In_Passbook(code, amount):
	text_to_return = ""
	if code == 1:
		text_to_return = "Deposited Rs " + amount
	elif code == 2:
		text_to_return = "Purchased For Rs " + amount
	elif code == 3:
		text_to_return = "Recieved Rs " + amount
	elif code == 4:
		text_to_return = "Withdrawn Rs " + amount
	return text_to_return + " On " + Current_Time_Date()

def Transaction_Mail(code, guy_name, his_balance, trans_amount, mail_to_send):
	sender_email = "YOUR EMAIL"
	receiver_email = mail_to_send[:]

	message = MIMEMultipart()

	message["From"] = sender_email
	message["To"] = receiver_email
	message["Subject"] = "Transaction Successfully Done At Shop"
	if code == 1:
		body = "Dear {},\nYou Have Deposited Rs {} To Your Wallet.\nYour Account Balance Is Rs {}.\nRegards,\nThe Shop Customer Team.".format(guy_name, trans_amount, his_balance)
	elif code == 2:
		body = "Dear {},\nYou Have Purchased For Rs {} in The Shop.\nYour Account Balance Is Rs {}.\nRegards,\nThe Shop Customer Team.".format(guy_name, trans_amount, his_balance)
	elif code == 3:
		body = "Dear {},\nYou Have Recieved Rs {} From An Customer.\nYour Account Balance Is Rs {}.\nRegards,\nThe Shop Seller Team.".format(guy_name, trans_amount, his_balance)
	elif code == 4:
		body = "Dear {},\nYou Have Withdrawn Rs {} From Your Wallet.\nYour Account Balance Is Rs {}.\nRegards,\nThe Shop Seller Team".format(guy_name, trans_amount, his_balance)

	message.attach(MIMEText(body,'plain'))

	my_message = message.as_string()

	context = ssl.create_default_context()
	with smtplib.SMTP("smtp.gmail.com", 587) as server:
		server.ehlo()
		server.starttls(context = context)
		server.ehlo()
		server.login(sender_email, "YOUR PASSWORD")
		server.sendmail(sender_email, receiver_email, my_message)

def Get_Category(sell_pos, product_name):
	seller_file = "C:\\Projects\\Python\\Shopping\\Warehouse\\"+str(sell_pos)+".csv"
	file = open(seller_file)
	csvfile = list(csv.reader(file))
	file.close()
	for products in csvfile:
		if products[0] == product_name:
			return products[3]

def Remove_Product(location, product_name):
	file = open(location)
	contents = list(csv.reader(file))
	file.close()
	product_pos = 0
	for i in range(len(contents)):
		if contents[i][0] == product_name:
			product_pos = i
			break
	del contents[product_pos]
	file = open(location, "w", newline='')
	csvfile = csv.writer(file)
	for products in contents:
		csvfile.writerow(products)
	file.close()

def Retreive_Products(category_name):
	file_location = "C:\\Projects\\Python\\Shopping\\Warehouse\\"+category_name+".csv"
	file = open(file_location)
	contents = list(csv.reader(file))
	file.close()
	return contents

def Retreive_User_USE(utype, pos, wtr):
	if not utype:
		file_loc = "C:\\Projects\\Python\\Shopping\\Customers\\all_customers.csv"
	else:
		file_loc = "C:\\Projects\\Python\\Shopping\\Sellers\\all_sellers.csv"
	file = open(file_loc)
	file_contents = list(csv.reader(file))
	file.close()
	if not wtr:
		return file_contents[pos][1]
	else:
		return file_contents[pos][2]

def Cart_Products(pos):
	file_loc = "C:\\Projects\\Python\\Shopping\\Customers\\Cart\\"+str(pos)+".csv"
	count = int()
	if not path.exists(file_loc):
		count = 0
	else:
		file = open(file_loc)
		count = sum([1 for contents in csv.reader(file)])
		file.close()
	return count

def Write_To_Cart(pos, prod_details):
	file_loc = "C:\\Projects\\Python\\Shopping\\Customers\\Cart\\"+str(pos)+".csv"
	file = open(file_loc, 'a', newline = '')
	csvwriter = csv.writer(file)
	csvwriter.writerow(prod_details)
	file.close()

def Split_Money_Among_Sellers(price_seller_list):
	file_loc = "C:\\Projects\\Python\\Shopping\\Sellers\\all_sellers.csv"
	file = open(file_loc)
	all_sellers_details = list(csv.reader(file))
	file.close()
	for prod in price_seller_list:
		all_sellers_details[int(prod[-1])][3] = str(int(all_sellers_details[int(prod[-1])][3]) + int(prod[0]))
		Transaction_Mail(3, all_sellers_details[int(prod[-1])][0], all_sellers_details[int(prod[-1])][3], int(prod[0]),all_sellers_details[int(prod[-1])][2])
		passbook_file = "C:\\Projects\\Python\\Shopping\\Sellers\\"
		passbook_file += str(Retrieve_User_Pos(all_sellers_details[int(prod[-1])][2], 1))
		passbook_file += ".txt"
		file2 = open(passbook_file, "a")
		to_write = Content_To_Write_In_Passbook(3, prod[0])
		file2.write(to_write+"\n")
		file2.close()
		Change_The_Detail_In_File(1, int(prod[-1]), 3, all_sellers_details[int(prod[-1])][3])

#