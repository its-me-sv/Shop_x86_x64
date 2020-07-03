from PyQt5 import QtCore, QtGui, QtWidgets
import sys 
import resources_rc
from dependencies import *
from os import path
import csv

def Display_Message(code):
    msg=QtWidgets.QMessageBox()
    if code < 3:
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        if code == 1:
            msg.setText("You Didn't Agree To The Terms And Conditions Yet.")
        else:
            msg.setText("You Are Not Connected To The Internet.")
    else:
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Account Created Successfully")
    msg.setWindowTitle(" ")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()


def Display_Message2(code):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    if code == 1:
        msg.setText("You Have Entered An Invalid Username.")
    elif code == 2:
        msg.setText("The Confirmation Password Didn't Match With The Password.")
    elif code == 3:
        msg.setText("The Username Is Already In Use.")
    elif code == 4:
        msg.setText("The Email Is Already In Use.")
    elif code == 5:
        msg.setText("Invalid Email Address")
    elif code == 6:
        msg.setText("You Have Entered An Invalid Shop Name.")
    elif code == 7:
        msg.setText("The Shop Name Is Already In Use.")
    elif code == 8:
        msg.setText("Enter Your Registered Email Id In The Username/Email And Then Proceed To Reset Password.")
    elif code == 9:
        msg.setText("There Is No Account Associated With This Email.")
    elif code == 10:
        msg.setText("Incorrect Validation Key")
    elif code == 11:
        msg.setText("Invalid Amount")
    elif code == 12:
        msg.setText("Insufficient Balance")
    elif code == 13:
        msg.setText("Product Name Not Allowed")
    elif code == 14:
        msg.setText("Invalid Price")
    elif code == 15:
        msg.setText("Give The Product Some Good Descreption")
    elif code == 16:
        msg.setText("Select Atmost One Product.")
    elif code == 17:
        msg.setText("You Don't Have Any Products In Your Warehouse")
    elif code == 18:
        msg.setText("Currently There Are No Products")
    elif code == 19:
        msg.setText("You Don't Have Any Products In Your Cart")
    elif code == 20:
        msg.setText("You Have Insufficient Amount In Your Vallet To Make This Purchase.")
    msg.setWindowTitle(" ")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()


def Display_Message3(code):
    msg = QtWidgets.QMessageBox()
    if not code:
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("Invalid Login Credentials")
    else:
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Log In Successfull")
    if code == 300:
        msg.setText("Password Reset Successfull")
    if code == 303:
        msg.setText("Name Has Been Updated Successfully")
    if code == 306:
        msg.setText("Username Has Been Updated Successfully")
    if code == 309:
        msg.setText("Email Has Been Updated Successfully")
    if code == 312:
        msg.setText("Shop Name Updated Successfully")
    if code == 67:
        msg.setText("Log Out Successfull")
    if code == 315:
        msg.setText("Money Has Been Deposited Successfully")
    if code == 318:
        msg.setText("Money Has Been Withdrawn Successfully")
    if code == 321:
        msg.setText("Product Has Been Added To Your Warehouse Successfully")
    if code == 324:
        msg.setText("Product Has Been Removed From Your Warehouse Successfully")
    if code == 327:
        msg.setText("Product Has Been Added To Your Cart Successfully")
    if code == 330:
        msg.setText("Your Cart Has Been Cleared Successfully")
    if code == 333:
        msg.setText("Product Has Been Removed From Your Cart Successfully")
    if code == 336:
        msg.setText("Product Purchase Successfull")
    if code == 339:
        msg.setText("Working On Transaction. Wait For An While. The Time Depends Upon Your Internet Connection.")
    msg.setWindowTitle(" ")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()


validating_key = ""
changer_email = ""
user_details = ["", "", "", "", "", ""]
default_products = []
current_product = []

class Ui_Product_Details(object):
    global current_product
    def setupUi(self, Product_Details):
        Product_Details.setObjectName("Product_Details")
        Product_Details.resize(600, 600)
        Product_Details.setMinimumSize(QtCore.QSize(600, 600))
        Product_Details.setMaximumSize(QtCore.QSize(600, 600))
        Product_Details.setBaseSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Product_Details.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Product_Details)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setMinimumSize(QtCore.QSize(600, 600))
        self.background.setMaximumSize(QtCore.QSize(600, 600))
        self.background.setBaseSize(QtCore.QSize(600, 600))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 221, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 130, 71, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 180, 141, 31))
        self.label_4.setObjectName("label_4")
        
        self.Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(260, 80, 291, 31))
        self.Name.setClearButtonEnabled(False)
        self.Name.setObjectName("Name")
        self.Name.setText(current_product[0])
        self.Name.setReadOnly(True)
        
        self.Price = QtWidgets.QLineEdit(self.centralwidget)
        self.Price.setGeometry(QtCore.QRect(260, 130, 291, 31))
        self.Price.setClearButtonEnabled(False)
        self.Price.setObjectName("Price")
        self.Price.setText(str(current_product[1])+" Rs")
        self.Price.setReadOnly(True)
        
        self.Descreption = QtWidgets.QTextEdit(self.centralwidget)
        self.Descreption.setGeometry(QtCore.QRect(260, 190, 291, 111))
        self.Descreption.setObjectName("Descreption")
        self.Descreption.setText(current_product[2])
        self.Descreption.setReadOnly(True)
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 310, 111, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 370, 151, 41))
        self.label_6.setObjectName("label_6")
        
        self.SellerName = QtWidgets.QLineEdit(self.centralwidget)
        self.SellerName.setGeometry(QtCore.QRect(260, 370, 291, 31))
        self.SellerName.setClearButtonEnabled(False)
        self.SellerName.setObjectName("SellerName")
        self.SellerName.setText(Retreive_User_USE(1, int(current_product[-1]), 0))
        self.SellerName.setReadOnly(True)
        
        self.OkButton = QtWidgets.QPushButton(self.centralwidget)
        self.OkButton.setGeometry(QtCore.QRect(210, 470, 171, 41))
        self.OkButton.setObjectName("OkButton")
        
        self.Category = QtWidgets.QLineEdit(self.centralwidget)
        self.Category.setGeometry(QtCore.QRect(260, 320, 291, 31))
        self.Category.setClearButtonEnabled(False)
        self.Category.setObjectName("Category")
        self.Category.setText(current_product[3])
        self.Category.setReadOnly(True)
        
        Product_Details.setCentralWidget(self.centralwidget)

        self.retranslateUi(Product_Details)
        QtCore.QMetaObject.connectSlotsByName(Product_Details)
        self.OkButton.clicked.connect(self.Close_Details)

    def Close_Details(self):
        Product_Details.hide()

    def retranslateUi(self, Product_Details):
        _translate = QtCore.QCoreApplication.translate
        Product_Details.setWindowTitle(_translate("Product_Details", "Shop - Customer - Product Details"))
        self.label.setText(_translate("Product_Details", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Product Details</span></p></body></html>"))
        self.label_2.setText(_translate("Product_Details", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">Name</span></p></body></html>"))
        self.label_3.setText(_translate("Product_Details", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Price</span></p></body></html>"))
        self.label_4.setText(_translate("Product_Details", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">Description</span></p></body></html>"))
        self.Name.setPlaceholderText(_translate("Product_Details", "Product Name"))
        self.Price.setPlaceholderText(_translate("Product_Details", "Product Price"))
        self.Descreption.setPlaceholderText(_translate("Product_Details", "Product Descreption"))
        self.label_5.setText(_translate("Product_Details", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">Category</span></p></body></html>"))
        self.label_6.setText(_translate("Product_Details", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">Seller Name</span></p></body></html>"))
        self.SellerName.setPlaceholderText(_translate("Product_Details", "Seller Name"))
        self.OkButton.setText(_translate("Product_Details", "Ok"))
        self.Category.setPlaceholderText(_translate("Product_Details", "Category"))


class Ui_Customer_Cart(object):
    global user_details
    def __init__(self):
        self.cart_total = int()
    def setupUi(self, Customer_Cart):
        Customer_Cart.setObjectName("Customer_Cart")
        Customer_Cart.resize(600, 600)
        Customer_Cart.setMinimumSize(QtCore.QSize(600, 600))
        Customer_Cart.setMaximumSize(QtCore.QSize(600, 600))
        Customer_Cart.setBaseSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Customer_Cart.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Customer_Cart)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 191, 31))
        self.label_2.setObjectName("label_2")
        self.BackShoppingButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.BackShoppingButton.setGeometry(QtCore.QRect(0, 0, 191, 31))
        self.BackShoppingButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackShoppingButton.setIcon(icon1)
        self.BackShoppingButton.setObjectName("BackShoppingButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 100, 101, 71))
        self.label.setObjectName("label")
        
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(40, 200, 511, 241))
        self.listWidget.setObjectName("listWidget")
        file_loc = "C:\\Projects\\Python\\Shopping\\Customers\\Cart\\"
        file_loc += str(Retrieve_User_Pos(user_details[1], 0))
        file_loc += ".csv"
        self.cart_total = 0
        if not path.exists(file_loc):
            pass
        else:
            file = open(file_loc)
            csvreader = list(csv.reader(file))
            file.close()
            for line in csvreader:
                self.listWidget.addItem(line[0]+"\t"+line[1]+" Rs")
                self.cart_total += int(line[1])
        if not self.listWidget.count():
            Display_Message2(19)

        self.CheckoutButton = QtWidgets.QPushButton(self.centralwidget)
        self.CheckoutButton.setGeometry(QtCore.QRect(220, 530, 161, 31))
        self.CheckoutButton.setObjectName("CheckoutButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 450, 111, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 460, 131, 21))
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        Customer_Cart.setCentralWidget(self.centralwidget)
        self.lineEdit.setText(str(self.cart_total)+" Rs")
        self.lineEdit.setReadOnly(True)

        self.RemoveProduct = QtWidgets.QPushButton(self.centralwidget)
        self.RemoveProduct.setGeometry(QtCore.QRect(380, 450, 171, 31))
        self.RemoveProduct.setObjectName("RemoveProduct")
        self.ClearCart = QtWidgets.QPushButton(self.centralwidget)
        self.ClearCart.setGeometry(QtCore.QRect(380, 490, 171, 31))
        self.ClearCart.setObjectName("ClearCart")

        self.retranslateUi(Customer_Cart)
        QtCore.QMetaObject.connectSlotsByName(Customer_Cart)
        self.BackShoppingButton.clicked.connect(self.Back_To_Shopping)

        if not self.cart_total:
            self.CheckoutButton.setEnabled(False)
        else:
            self.CheckoutButton.setEnabled(True)
        self.ClearCart.clicked.connect(self.Cart_Clearence)
        self.RemoveProduct.clicked.connect(self.Product_Removal)
        self.CheckoutButton.clicked.connect(self.Checking_Out)

    def Checking_Out(self):
        if not Internet_Available():
            Display_Message(2)
        if self.cart_total > int(user_details[3]):
            Display_Message2(20)
        else:
            Display_Message3(339)
            self.CheckoutButton.setEnabled(False)
            file_loc = "C:\\Projects\\Python\\Shopping\\Customers\\Cart\\"
            file_loc += str(Retrieve_User_Pos(user_details[1], 0))
            file_loc += ".csv"
            price_and_seller = list()
            file = open(file_loc)
            all_products = list(csv.reader(file))
            file.close()
            for product in all_products:
                price_and_seller.append([product[1], product[-1]])
            Split_Money_Among_Sellers(price_and_seller)
            passbook_loc = "C:\\Projects\\Python\\Shopping\\Customers\\"
            passbook_loc += str(Retrieve_User_Pos(user_details[1], 0))
            passbook_loc += ".txt"
            user_details[3] = int(user_details[3]) - self.cart_total
            content_to_write = Content_To_Write_In_Passbook(2, str(self.cart_total))
            file = open(passbook_loc, 'a')
            file.write(content_to_write+"\n")
            file.close()
            Change_The_Detail_In_File(0, Retrieve_User_Pos(user_details[1], 0), 3, user_details[3])
            Transaction_Mail(2, user_details[0], user_details[3], self.cart_total, user_details[2])
            Display_Message3(336)
            file_loc = "C:\\Projects\\Python\\Shopping\\Customers\\Cart\\"
            file_loc += str(Retrieve_User_Pos(user_details[1], 0))
            file_loc += ".csv"
            file = open(file_loc, 'w+')
            file.close()
            self.listWidget.clear()
            Display_Message3(330)
            global ui19
            ui19.setupUi(Customer_Shopping)
            Customer_Shopping.show()
            Customer_Cart.hide()

    def Product_Removal(self):
        removed_product = self.listWidget.takeItem(self.listWidget.currentRow())
        try:
            product_name = removed_product.text()
            product_name = product_name.split("\t")[0]
        except AttributeError:
            Display_Message2(16)
        else:
            file_loc = "C:\\Projects\\Python\\Shopping\\Customers\\Cart\\"
            file_loc += str(Retrieve_User_Pos(user_details[1], 0))
            file_loc += ".csv"
            Remove_Product(file_loc, product_name)
            Display_Message3(333)
            global ui19
            ui19.setupUi(Customer_Shopping)
            Customer_Shopping.show()
            Customer_Cart.hide()

    def Cart_Clearence(self):
        if not self.listWidget.count():
            Display_Message2(19)
        else:
            file_loc = "C:\\Projects\\Python\\Shopping\\Customers\\Cart\\"
            file_loc += str(Retrieve_User_Pos(user_details[1], 0))
            file_loc += ".csv"
            file = open(file_loc, 'w+')
            file.close()
            self.listWidget.clear()
            Display_Message3(330)
            global ui19
            ui19.setupUi(Customer_Shopping)
            Customer_Shopping.show()
            Customer_Cart.hide()

    def Back_To_Shopping(self):
        global ui19
        ui19.setupUi(Customer_Shopping)
        Customer_Shopping.show()
        Customer_Cart.hide()

    def retranslateUi(self, Customer_Cart):
        _translate = QtCore.QCoreApplication.translate
        Customer_Cart.setWindowTitle(_translate("Customer_Cart", "Shop - Customer - Cart"))
        self.label_2.setText(_translate("Customer_Cart", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Back To Shopping</span></p></body></html>"))
        self.label.setText(_translate("Customer_Cart", "<html><head/><body><p><span style=\" font-size:36pt; color:#ffffff;\">Cart</span></p></body></html>"))
        self.CheckoutButton.setText(_translate("Customer_Cart", "Check Out"))
        self.label_3.setText(_translate("Customer_Cart", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Cart Total</span></p></body></html>"))
        self.RemoveProduct.setText(_translate("Customer_Cart", "Remove Product"))
        self.ClearCart.setText(_translate("Customer_Cart", "Clear Cart"))


class Ui_Customer_Shopping(object):
    global default_products, current_product
    def setupUi(self, Customer_Shopping):
        Customer_Shopping.setObjectName("Customer_Shopping")
        Customer_Shopping.resize(600, 600)
        Customer_Shopping.setMinimumSize(QtCore.QSize(600, 600))
        Customer_Shopping.setMaximumSize(QtCore.QSize(600, 600))
        Customer_Shopping.setBaseSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Customer_Shopping.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Customer_Shopping)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 221, 31))
        self.label_2.setObjectName("label_2")
        
        self.BackHomeButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.BackHomeButton.setGeometry(QtCore.QRect(0, 0, 221, 31))
        self.BackHomeButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackHomeButton.setIcon(icon1)
        self.BackHomeButton.setObjectName("BackHomeButton")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 50, 201, 71))
        self.label.setObjectName("label")
        
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(40, 200, 511, 241))
        self.listWidget.setObjectName("listWidget")
        default_products = Retreive_Products("All_Departments")
        for i in range(1, len(default_products)):
            self.listWidget.addItem(default_products[i][0]+"\t"+default_products[i][1]+" Rs")
        if not self.listWidget.count():
            Display_Message2(18)

        self.AddToCart = QtWidgets.QPushButton(self.centralwidget)
        self.AddToCart.setGeometry(QtCore.QRect(40, 470, 161, 31))
        self.AddToCart.setObjectName("AddToCart")
        
        self.ProductDetailsButton = QtWidgets.QPushButton(self.centralwidget)
        self.ProductDetailsButton.setGeometry(QtCore.QRect(390, 470, 161, 31))
        self.ProductDetailsButton.setObjectName("ProductDetailsButton")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 171, 41))
        self.label_3.setObjectName("label_3")
        
        self.Categories = QtWidgets.QComboBox(self.centralwidget)
        self.Categories.setGeometry(QtCore.QRect(40, 140, 161, 21))
        self.Categories.setObjectName("Categories")
        file = open("C:\\Projects\\Python\\Shopping\\Warehouse\\categories.txt")
        for line in file.readlines():
            self.Categories.addItem(line.rstrip())
        file.close()

        self.ApplyButton = QtWidgets.QPushButton(self.centralwidget)
        self.ApplyButton.setGeometry(QtCore.QRect(80, 170, 75, 23))
        self.ApplyButton.setObjectName("ApplyButton")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 10, 51, 31))
        self.label_4.setObjectName("label_4")
        
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(520, 10, 71, 31))
        self.lcdNumber.setProperty("value", str(Cart_Products(Retrieve_User_Pos(user_details[1], 0))))
        self.lcdNumber.setObjectName("lcdNumber")
        
        self.CartButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.CartButton.setGeometry(QtCore.QRect(450, 10, 141, 31))
        self.CartButton.setText("")
        self.CartButton.setIcon(icon1)
        self.CartButton.setObjectName("CartButton")
        Customer_Shopping.setCentralWidget(self.centralwidget)

        self.retranslateUi(Customer_Shopping)
        QtCore.QMetaObject.connectSlotsByName(Customer_Shopping)
        self.CartButton.clicked.connect(self.Go_To_Cart)
        self.BackHomeButton.clicked.connect(self.Back_To_Home)
        self.ApplyButton.clicked.connect(self.Apply_Button_Clicked)
        self.ProductDetailsButton.clicked.connect(self.Show_Details)
        self.AddToCart.clicked.connect(self.Product_To_Cart)

    def Apply_Button_Clicked(self):
        global default_products
        self.listWidget.clear()
        default_products = Retreive_Products(self.Categories.currentText())
        for i in range(1, len(default_products)):
            self.listWidget.addItem(default_products[i][0]+"\t"+default_products[i][1]+"Rs")
        if not self.listWidget.count():
            Display_Message2(18)

    def Product_To_Cart(self):
        global current_product
        try:
            current_product_name = self.listWidget.currentItem().text().split("\t")[0]
        except:
            Display_Message2(16)
        else:
            for prods in Retreive_Products(self.Categories.currentText()):
                if prods[0] == current_product_name:
                    current_product = prods[:]
            Write_To_Cart(Retrieve_User_Pos(user_details[1], 0), current_product)
            Display_Message3(327)
            CustomerHP.show()
            Customer_Shopping.hide()

    def Show_Details(self):
        global current_product
        try:
            current_product_name = self.listWidget.currentItem().text().split("\t")[0]
        except:
            Display_Message2(16)
        else:
            for prods in Retreive_Products(self.Categories.currentText()):
                if prods[0] == current_product_name:
                    current_product = prods[:]
            global ui21
            ui21.setupUi(Product_Details)
            Product_Details.show()

    def Go_To_Cart(self):
        global ui20
        ui20.setupUi(Customer_Cart)
        Customer_Cart.show()
        Customer_Shopping.hide()

    def Back_To_Home(self):
        CustomerHP.show()
        Customer_Shopping.hide()

    def retranslateUi(self, Customer_Shopping):
        _translate = QtCore.QCoreApplication.translate
        Customer_Shopping.setWindowTitle(_translate("Customer_Shopping", "Shop - Customer - Shopping"))
        self.label_2.setText(_translate("Customer_Shopping", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Back To Home Page</span></p></body></html>"))
        self.label.setText(_translate("Customer_Shopping", "<html><head/><body><p><span style=\" font-size:36pt; color:#ffffff;\">Shopping</span></p></body></html>"))
        self.AddToCart.setText(_translate("Customer_Shopping", "Add To Cart"))
        self.ProductDetailsButton.setText(_translate("Customer_Shopping", "View Product Details"))
        self.label_3.setText(_translate("Customer_Shopping", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Select Category</span></p></body></html>"))
        self.ApplyButton.setText(_translate("Customer_Shopping", "Apply"))
        self.label_4.setText(_translate("Customer_Shopping", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Cart</span></p></body></html>"))


class Ui_AddItem(object):
    global user_details
    def setupUi(self, AddItem):
        AddItem.setObjectName("AddItem")
        AddItem.resize(600, 600)
        AddItem.setMinimumSize(QtCore.QSize(600, 600))
        AddItem.setMaximumSize(QtCore.QSize(600, 600))
        AddItem.setBaseSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddItem.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(AddItem)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setMinimumSize(QtCore.QSize(600, 600))
        self.background.setMaximumSize(QtCore.QSize(600, 600))
        self.background.setBaseSize(QtCore.QSize(600, 600))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 221, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 130, 71, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 180, 141, 31))
        self.label_4.setObjectName("label_4")
        
        self.Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(260, 80, 291, 31))
        self.Name.setClearButtonEnabled(True)
        self.Name.setObjectName("Name")
        
        self.Price = QtWidgets.QLineEdit(self.centralwidget)
        self.Price.setGeometry(QtCore.QRect(260, 130, 291, 31))
        self.Price.setClearButtonEnabled(True)
        self.Price.setObjectName("Price")
        self.Price.setText("0")
        self.onlyInt = QtGui.QIntValidator()
        self.Price.setValidator(self.onlyInt)
        
        self.Descreption = QtWidgets.QTextEdit(self.centralwidget)
        self.Descreption.setGeometry(QtCore.QRect(260, 190, 291, 111))
        self.Descreption.setObjectName("Descreption")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 310, 111, 41))
        self.label_5.setObjectName("label_5")
        
        self.Category = QtWidgets.QComboBox(self.centralwidget)
        self.Category.setGeometry(QtCore.QRect(260, 320, 291, 31))
        self.Category.setEditable(False)
        self.Category.setCurrentText("")
        self.Category.setObjectName("Category")
        loc = "C:\\Projects\\Python\\Shopping\\Warehouse\\categories.txt"
        file = open(loc)
        for line in file.readlines():
            self.Category.addItem(line.rstrip())
        file.close()

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 370, 151, 41))
        self.label_6.setObjectName("label_6")
        
        self.SellerName = QtWidgets.QLineEdit(self.centralwidget)
        self.SellerName.setGeometry(QtCore.QRect(260, 370, 291, 31))
        self.SellerName.setText(user_details[1])
        self.SellerName.setObjectName("SellerName")
        self.SellerName.setReadOnly(True)
        
        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setGeometry(QtCore.QRect(340, 470, 171, 41))
        self.AddButton.setObjectName("AddButton")
        
        self.CancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.CancelButton.setGeometry(QtCore.QRect(70, 470, 171, 41))
        self.CancelButton.setObjectName("CancelButton")
        AddItem.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddItem)
        QtCore.QMetaObject.connectSlotsByName(AddItem)
        self.CancelButton.clicked.connect(self.Go_Warehouse)
        self.AddButton.clicked.connect(self.Going_To_Add)

    def Going_To_Add(self):
        if self.Name.text() == "":
            Display_Message2(13)
        elif int(self.Price.text()) < 1:
            Display_Message2(14)
        elif self.Descreption.toPlainText() == "":
            Display_Message2(15)
        else:
            product_details = list()
            product_details.append(self.Name.text())
            product_details.append(self.Price.text())
            product_details.append(self.Descreption.toPlainText())
            product_details.append(self.Category.currentText())
            product_details.append(Retrieve_User_Pos(user_details[1], 1))
            file_loc = "C:\\Projects\\Python\\Shopping\\Warehouse\\"
            file_loc += str(Retrieve_User_Pos(user_details[1], 1))
            file_loc += ".csv"
            file = open(file_loc, 'a', newline = '')
            csvwriter = csv.writer(file)
            csvwriter.writerow(product_details)
            file.close()
            file_category_loc = "C:\\Projects\\Python\\Shopping\\Warehouse\\"
            file_category_loc += product_details[3]
            file_category_loc += ".csv"
            file1 = open(file_category_loc, 'a', newline = '')
            csvwriter = csv.writer(file1)
            csvwriter.writerow(product_details)
            file1.close()
            if product_details[3] != "All_Departments":
                filel = open("C:\\Projects\\Python\\Shopping\\Warehouse\\All_Departments.csv", 'a', newline = '')
                filewriter = csv.writer(filel)
                filewriter.writerow(product_details)
                file1.close()
            self.Name.clear()
            self.Price.clear()
            Display_Message3(321)
            global ui17
            ui17.setupUi(SellerWarehouse)
            SellerWarehouse.show()
            AddItem.hide()

    def Go_Warehouse(self):
        global ui17
        ui17.setupUi(SellerWarehouse)
        SellerWarehouse.show()
        AddItem.hide()

    def retranslateUi(self, AddItem):
        _translate = QtCore.QCoreApplication.translate
        AddItem.setWindowTitle(_translate("AddItem", "Shop - Seller - Add Product"))
        self.label.setText(_translate("AddItem", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Product Details</span></p></body></html>"))
        self.label_2.setText(_translate("AddItem", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">Name</span></p></body></html>"))
        self.label_3.setText(_translate("AddItem", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Price</span></p></body></html>"))
        self.label_4.setText(_translate("AddItem", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">Description</span></p></body></html>"))
        self.Name.setPlaceholderText(_translate("AddItem", "Product Name"))
        self.Price.setPlaceholderText(_translate("AddItem", "Product Price"))
        self.Descreption.setPlaceholderText(_translate("AddItem", "Product Descreption"))
        self.label_5.setText(_translate("AddItem", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">Category</span></p></body></html>"))
        self.label_6.setText(_translate("AddItem", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">Seller Name</span></p></body></html>"))
        self.SellerName.setPlaceholderText(_translate("AddItem", "Seller Name"))
        self.AddButton.setText(_translate("AddItem", "Add Product"))
        self.CancelButton.setText(_translate("AddItem", "Cancel"))


class Ui_SellerWarehouse(object):
    global user_details
    def setupUi(self, SellerWarehouse):
        SellerWarehouse.setObjectName("SellerWarehouse")
        SellerWarehouse.resize(600, 600)
        SellerWarehouse.setMinimumSize(QtCore.QSize(600, 600))
        SellerWarehouse.setMaximumSize(QtCore.QSize(600, 600))
        SellerWarehouse.setBaseSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SellerWarehouse.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(SellerWarehouse)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setMinimumSize(QtCore.QSize(600, 600))
        self.background.setMaximumSize(QtCore.QSize(600, 600))
        self.background.setBaseSize(QtCore.QSize(600, 600))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 60, 241, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 221, 31))
        self.label_2.setObjectName("label_2")
        
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(0, 0, 221, 31))
        self.commandLinkButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton.setObjectName("commandLinkButton")
        
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(40, 170, 511, 241))
        self.listWidget.setObjectName("listWidget")
        file_loc = "C:\\Projects\\Python\\Shopping\\Warehouse\\"
        file_loc += str(Retrieve_User_Pos(user_details[1], 1))
        file_loc += ".csv"
        if not path.exists(file_loc):
            pass
        else:
            file = open(file_loc)
            csvfile = csv.reader(file)
            for product in csvfile:
                self.listWidget.addItem(product[0] + "\t" + product[1] + " Rs\t" +product[3])
            file.close()
        if not self.listWidget.count(): 
            Display_Message2(17)
        self.AddPButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddPButton.setGeometry(QtCore.QRect(40, 450, 161, 31))
        self.AddPButton.setObjectName("AddPButton")
        
        self.RemovePButton = QtWidgets.QPushButton(self.centralwidget)
        self.RemovePButton.setGeometry(QtCore.QRect(360, 450, 161, 31))
        self.RemovePButton.setObjectName("RemovePButton")
        SellerWarehouse.setCentralWidget(self.centralwidget)

        self.retranslateUi(SellerWarehouse)
        QtCore.QMetaObject.connectSlotsByName(SellerWarehouse)
        self.commandLinkButton.clicked.connect(self.Back_To_Home)
        self.AddPButton.clicked.connect(self.Adding_Product)
        self.RemovePButton.clicked.connect(self.Remove_Product)

    def Remove_Product(self):
        removed_product = self.listWidget.takeItem(self.listWidget.currentRow())
        try:
            product_name = removed_product.text()
            if product_name == "You Don't Have Any Products In Your Warehouse":
                raise AttributeError
            product_name = product_name.split("\t")[0]
        except AttributeError:
            Display_Message2(16)
        else:
            product_category = Get_Category(Retrieve_User_Pos(user_details[1], 1), product_name)
            default_loc = "C:\\Projects\\Python\\Shopping\\Warehouse\\"
            seller_file = default_loc+str(Retrieve_User_Pos(user_details[1], 1))+".csv"
            category_file = default_loc+product_category+".csv"
            Remove_Product(seller_file, product_name)
            Remove_Product(category_file, product_name)
            if product_category != "All_Departments":
                Remove_Product("C:\\Projects\\Python\\Shopping\\Warehouse\\All_Departments.csv", product_name)
            Display_Message3(324)
            SellerHP.show()
            SellerWarehouse.hide()

    def Adding_Product(self):
        global ui18
        ui18.setupUi(AddItem)
        AddItem.show()
        SellerWarehouse.hide()

    def Back_To_Home(self):
        SellerHP.show()
        SellerWarehouse.hide()

    def retranslateUi(self, SellerWarehouse):
        _translate = QtCore.QCoreApplication.translate
        SellerWarehouse.setWindowTitle(_translate("SellerWarehouse", "Shop - Seller - Warehouse"))
        self.label.setText(_translate("SellerWarehouse", "<html><head/><body><p><span style=\" font-size:36pt; color:#ffffff;\">Warehouse</span></p></body></html>"))
        self.label_2.setText(_translate("SellerWarehouse", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Back To Home Page</span></p></body></html>"))
        self.AddPButton.setText(_translate("SellerWarehouse", "Add Product"))
        self.RemovePButton.setText(_translate("SellerWarehouse", "Remove Product"))


class Ui_SellerPayments(object):
    global user_details
    def setupUi(self, SellerPayments):
        SellerPayments.setObjectName("SellerPayments")
        SellerPayments.resize(500, 500)
        SellerPayments.setMinimumSize(QtCore.QSize(500, 500))
        SellerPayments.setMaximumSize(QtCore.QSize(500, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SellerPayments.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(SellerPayments)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.background.setMinimumSize(QtCore.QSize(500, 500))
        self.background.setMaximumSize(QtCore.QSize(500, 500))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 191, 31))
        self.label.setObjectName("label")
        
        self.HomePageButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.HomePageButton.setGeometry(QtCore.QRect(0, 0, 191, 31))
        self.HomePageButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HomePageButton.setIcon(icon1)
        self.HomePageButton.setObjectName("HomePageButton")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 0, 91, 31))
        self.label_2.setObjectName("label_2")
        
        self.LEBalance = QtWidgets.QLineEdit(self.centralwidget)
        self.LEBalance.setGeometry(QtCore.QRect(380, 30, 113, 20))
        self.LEBalance.setObjectName("LEBalance")
        
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(40, 130, 431, 211))
        self.listWidget.setObjectName("listWidget")
        passbook_loc = "C:\\Projects\\Python\\Shopping\\Sellers\\"
        passbook_loc += str(Retrieve_User_Pos(user_details[1], 1))
        passbook_loc += ".txt"
        if not path.exists(passbook_loc):
            self.listWidget.addItem("You Have Not Made Any Transactions Yet")
        else:
            file = open(passbook_loc)
            for line in file.readlines():
                self.listWidget.addItem(line.rstrip())
            file.close()

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 90, 211, 31))
        self.label_3.setObjectName("label_3")
        
        self.DepositButton = QtWidgets.QPushButton(self.centralwidget)
        self.DepositButton.setEnabled(False)
        self.DepositButton.setGeometry(QtCore.QRect(50, 430, 111, 31))
        self.DepositButton.setObjectName("DepositButton")
        
        self.WithdrawButton = QtWidgets.QPushButton(self.centralwidget)
        self.WithdrawButton.setEnabled(True)
        self.WithdrawButton.setGeometry(QtCore.QRect(360, 430, 111, 31))
        self.WithdrawButton.setObjectName("WithdrawButton")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 350, 151, 31))
        self.label_4.setObjectName("label_4")
        
        self.Amount = QtWidgets.QLineEdit(self.centralwidget)
        self.Amount.setGeometry(QtCore.QRect(170, 380, 161, 21))
        self.Amount.setObjectName("Amount")
        self.Amount.setText("0")
        self.onlyInt = QtGui.QIntValidator()
        self.Amount.setValidator(self.onlyInt)
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 470, 331, 21))
        self.label_5.setObjectName("label_5")
        SellerPayments.setCentralWidget(self.centralwidget)

        self.retranslateUi(SellerPayments)
        QtCore.QMetaObject.connectSlotsByName(SellerPayments)
        self.HomePageButton.clicked.connect(self.Back_To_Home)
        self.LEBalance.setText(str(user_details[3])+" Rs")
        self.LEBalance.setReadOnly(True)
        self.WithdrawButton.clicked.connect(self.Withdraw_Money)

    def Withdraw_Money(self):
        if not Internet_Available():
            Display_Message(2)
        elif int(self.Amount.text()) < 1:
            Display_Message2(11)
        elif int(self.Amount.text()) > int(user_details[3]):
            Display_Message2(12)
        else:
            passbook_loc = "C:\\Projects\\Python\\Shopping\\Sellers\\"
            passbook_loc += str(Retrieve_User_Pos(user_details[1], 1))
            passbook_loc += ".txt"
            user_details[3] = int(user_details[3]) - abs(int(self.Amount.text()))
            content_to_write = Content_To_Write_In_Passbook(4, self.Amount.text())
            file = open(passbook_loc, 'a')
            file.write(content_to_write+"\n")
            file.close()
            Change_The_Detail_In_File(1, Retrieve_User_Pos(user_details[1], 1), 3, user_details[3])
            Transaction_Mail(4, user_details[0], user_details[3], self.Amount.text(), user_details[2])
            self.Amount.clear()
            self.listWidget.clear()
            Display_Message3(318)
            SellerHP.show()
            SellerPayments.hide()

    def Back_To_Home(self):
        SellerHP.show()
        SellerPayments.hide()

    def retranslateUi(self, SellerPayments):
        _translate = QtCore.QCoreApplication.translate
        SellerPayments.setWindowTitle(_translate("SellerPayments", "Shop - Seller - Payments"))
        self.label.setText(_translate("SellerPayments", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Back To Home Page</span></p></body></html>"))
        self.label_2.setText(_translate("SellerPayments", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Balance</span></p></body></html>"))
        self.label_3.setText(_translate("SellerPayments", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Transaction History</span></p></body></html>"))
        self.DepositButton.setText(_translate("SellerPayments", "Deposit"))
        self.WithdrawButton.setText(_translate("SellerPayments", "Withdraw"))
        self.label_4.setText(_translate("SellerPayments", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Enter Amount</span></p></body></html>"))
        self.Amount.setPlaceholderText(_translate("SellerPayments", "Enter Amount (RS) To Withdraw"))
        self.label_5.setText(_translate("SellerPayments", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">*As An Seller You Can Only Withdraw*</span></p></body></html>"))


class Ui_CustomerPayments(object):
    global user_details
    def setupUi(self, CustomerPayments):
        CustomerPayments.setObjectName("CustomerPayments")
        CustomerPayments.resize(500, 500)
        CustomerPayments.setMinimumSize(QtCore.QSize(500, 500))
        CustomerPayments.setMaximumSize(QtCore.QSize(500, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CustomerPayments.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(CustomerPayments)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.background.setMinimumSize(QtCore.QSize(500, 500))
        self.background.setMaximumSize(QtCore.QSize(500, 500))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 191, 31))
        self.label.setObjectName("label")
        
        self.HomePageButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.HomePageButton.setGeometry(QtCore.QRect(0, 0, 191, 31))
        self.HomePageButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HomePageButton.setIcon(icon1)
        self.HomePageButton.setObjectName("HomePageButton")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 0, 91, 31))
        self.label_2.setObjectName("label_2")
        
        self.LEBalance = QtWidgets.QLineEdit(self.centralwidget)
        self.LEBalance.setGeometry(QtCore.QRect(380, 30, 113, 20))
        self.LEBalance.setObjectName("LEBalance")
        
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(40, 130, 431, 211))
        self.listWidget.setObjectName("listWidget")
        passbook_loc = "C:\\Projects\\Python\\Shopping\\Customers\\"
        passbook_loc += str(Retrieve_User_Pos(user_details[1], 0))
        passbook_loc += ".txt"
        if not path.exists(passbook_loc):
            self.listWidget.addItem("You Have Not Made Any Transactions Yet")
        else:
            file = open(passbook_loc)
            for line in file.readlines():
                self.listWidget.addItem(line.rstrip())
            file.close()
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 90, 211, 31))
        self.label_3.setObjectName("label_3")
        
        self.DepositButton = QtWidgets.QPushButton(self.centralwidget)
        self.DepositButton.setGeometry(QtCore.QRect(50, 430, 111, 31))
        self.DepositButton.setObjectName("DepositButton")
        
        self.WithdrawButton = QtWidgets.QPushButton(self.centralwidget)
        self.WithdrawButton.setEnabled(False)
        self.WithdrawButton.setGeometry(QtCore.QRect(360, 430, 111, 31))
        self.WithdrawButton.setObjectName("WithdrawButton")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 350, 151, 31))
        self.label_4.setObjectName("label_4")
        
        self.Amount = QtWidgets.QLineEdit(self.centralwidget)
        self.Amount.setGeometry(QtCore.QRect(170, 380, 151, 21))
        self.Amount.setObjectName("Amount")
        self.Amount.setText("0")
        self.onlyInt = QtGui.QIntValidator()
        self.Amount.setValidator(self.onlyInt)
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 470, 341, 21))
        self.label_5.setObjectName("label_5")
        CustomerPayments.setCentralWidget(self.centralwidget)

        self.retranslateUi(CustomerPayments)
        QtCore.QMetaObject.connectSlotsByName(CustomerPayments)
        self.HomePageButton.clicked.connect(self.Back_To_Home)
        self.LEBalance.setText(str(user_details[3])+" Rs")
        self.LEBalance.setReadOnly(True)
        self.DepositButton.clicked.connect(self.Add_Money)

    def Add_Money(self):
        if not Internet_Available():
            Display_Message(2)
        if int(self.Amount.text()) < 1:
            Display_Message2(11)
        else:
            passbook_loc = "C:\\Projects\\Python\\Shopping\\Customers\\"
            passbook_loc += str(Retrieve_User_Pos(user_details[1], 0))
            passbook_loc += ".txt"
            user_details[3] = int(user_details[3]) + int(self.Amount.text())
            content_to_write = Content_To_Write_In_Passbook(1, self.Amount.text())
            file = open(passbook_loc, 'a')
            file.write(content_to_write+"\n")
            file.close()
            Change_The_Detail_In_File(0, Retrieve_User_Pos(user_details[1], 0), 3, user_details[3])
            Transaction_Mail(1, user_details[0], user_details[3], self.Amount.text(), user_details[2])
            self.Amount.clear()
            self.listWidget.clear()
            Display_Message3(315)
            CustomerHP.show()
            CustomerPayments.hide()

    def Back_To_Home(self):
        CustomerHP.show()
        CustomerPayments.hide()

    def retranslateUi(self, CustomerPayments):
        _translate = QtCore.QCoreApplication.translate
        CustomerPayments.setWindowTitle(_translate("CustomerPayments", "Shop - Customer - Payments"))
        self.label.setText(_translate("CustomerPayments", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Back To Home Page</span></p></body></html>"))
        self.label_2.setText(_translate("CustomerPayments", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Balance</span></p></body></html>"))
        self.label_3.setText(_translate("CustomerPayments", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Transaction History</span></p></body></html>"))
        self.DepositButton.setText(_translate("CustomerPayments", "Deposit"))
        self.WithdrawButton.setText(_translate("CustomerPayments", "Withdraw"))
        self.label_4.setText(_translate("CustomerPayments", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Enter Amount</span></p></body></html>"))
        self.Amount.setPlaceholderText(_translate("CustomerPayments", "Enter Amount (RS) To Deposit"))
        self.label_5.setText(_translate("CustomerPayments", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">*As An Customer You Can Only Deposit*</span></p></body></html>"))


class Ui_SellerProfile(object):
    def setupUi(self, SellerProfile):
        global user_details
        SellerProfile.setObjectName("SellerProfile")
        SellerProfile.resize(600, 600)
        SellerProfile.setMinimumSize(QtCore.QSize(600, 600))
        SellerProfile.setMaximumSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SellerProfile.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(SellerProfile)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 40, 131, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 110, 91, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 170, 151, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 230, 81, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 280, 241, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 330, 231, 51))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(180, 450, 241, 41))
        self.label_7.setObjectName("label_7")
        self.BSButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.BSButton.setGeometry(QtCore.QRect(180, 450, 241, 41))
        self.BSButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BSButton.setIcon(icon1)
        self.BSButton.setObjectName("BSButton")
        self.LEName = QtWidgets.QLineEdit(self.centralwidget)
        self.LEName.setGeometry(QtCore.QRect(320, 120, 221, 31))
        self.LEName.setObjectName("LEName")
        self.LEShopname = QtWidgets.QLineEdit(self.centralwidget)
        self.LEShopname.setGeometry(QtCore.QRect(320, 180, 221, 31))
        self.LEShopname.setObjectName("LEShopname")
        self.LEEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.LEEmail.setGeometry(QtCore.QRect(320, 230, 221, 31))
        self.LEEmail.setObjectName("LEEmail")
        self.LEBalance = QtWidgets.QLineEdit(self.centralwidget)
        self.LEBalance.setGeometry(QtCore.QRect(320, 290, 221, 31))
        self.LEBalance.setObjectName("LEBalance")
        self.LEAccDate = QtWidgets.QLineEdit(self.centralwidget)
        self.LEAccDate.setGeometry(QtCore.QRect(320, 340, 221, 31))
        self.LEAccDate.setObjectName("LEAccDate")
        SellerProfile.setCentralWidget(self.centralwidget)

        self.LEName.setText(user_details[0])
        self.LEShopname.setText(user_details[1])
        self.LEEmail.setText(user_details[2])
        self.LEBalance.setText(user_details[3] + " RS")
        self.LEAccDate.setText(user_details[4])

        self.LEName.setReadOnly(True)
        self.LEShopname.setReadOnly(True)
        self.LEEmail.setReadOnly(True)
        self.LEBalance.setReadOnly(True)
        self.LEAccDate.setReadOnly(True)

        self.retranslateUi(SellerProfile)
        QtCore.QMetaObject.connectSlotsByName(SellerProfile)

        self.BSButton.clicked.connect(self.Back_To_Settings)

    def Back_To_Settings(self):
        SellerSettings.show()
        SellerProfile.hide()

    def retranslateUi(self, SellerProfile):
        _translate = QtCore.QCoreApplication.translate
        SellerProfile.setWindowTitle(_translate("SellerProfile", "Shop - Seller - Profile"))
        self.label.setText(_translate("SellerProfile", "<html><head/><body><p><span style=\" font-size:36pt; color:#ffffff;\">Profile</span></p></body></html>"))
        self.label_2.setText(_translate("SellerProfile", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Name</span></p></body></html>"))
        self.label_3.setText(_translate("SellerProfile", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Shopname</span></p></body></html>"))
        self.label_4.setText(_translate("SellerProfile", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Email</span></p></body></html>"))
        self.label_5.setText(_translate("SellerProfile", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Account Balance</span></p></body></html>"))
        self.label_6.setText(_translate("SellerProfile", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Member Since</span></p></body></html>"))
        self.label_7.setText(_translate("SellerProfile", "<html><head/><body><p><span style=\" font-size:24pt; color:#00ff7f;\">Back To Settings</span></p></body></html>"))


class Ui_CustomerProfile(object):
    def setupUi(self, CustomerProfile):
        global user_details
        CustomerProfile.setObjectName("CustomerProfile")
        CustomerProfile.resize(600, 600)
        CustomerProfile.setMinimumSize(QtCore.QSize(600, 600))
        CustomerProfile.setMaximumSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CustomerProfile.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(CustomerProfile)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 40, 131, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 110, 91, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 170, 151, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 230, 81, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 280, 241, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 330, 231, 51))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(180, 450, 241, 41))
        self.label_7.setObjectName("label_7")
        self.BSButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.BSButton.setGeometry(QtCore.QRect(180, 450, 241, 41))
        self.BSButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BSButton.setIcon(icon1)
        self.BSButton.setObjectName("BSButton")
        self.LEName = QtWidgets.QLineEdit(self.centralwidget)
        self.LEName.setGeometry(QtCore.QRect(320, 120, 221, 31))
        self.LEName.setObjectName("LEName")
        self.LEUsername = QtWidgets.QLineEdit(self.centralwidget)
        self.LEUsername.setGeometry(QtCore.QRect(320, 180, 221, 31))
        self.LEUsername.setObjectName("LEUsername")
        self.LEEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.LEEmail.setGeometry(QtCore.QRect(320, 230, 221, 31))
        self.LEEmail.setObjectName("LEEmail")
        self.LEBalance = QtWidgets.QLineEdit(self.centralwidget)
        self.LEBalance.setGeometry(QtCore.QRect(320, 290, 221, 31))
        self.LEBalance.setObjectName("LEBalance")
        self.LEAccDate = QtWidgets.QLineEdit(self.centralwidget)
        self.LEAccDate.setGeometry(QtCore.QRect(320, 340, 221, 31))
        self.LEAccDate.setObjectName("LEAccDate")
        CustomerProfile.setCentralWidget(self.centralwidget)

        self.LEName.setText(user_details[0])
        self.LEUsername.setText(user_details[1])
        self.LEEmail.setText(user_details[2])
        try:
            self.LEBalance.setText(user_details[3] + " RS")
        except TypeError:
            user_details[3] = str(user_details[3])
            self.LEBalance.setText(user_details[3]+" RS")
        self.LEAccDate.setText(user_details[4])

        self.LEName.setReadOnly(True)
        self.LEUsername.setReadOnly(True)
        self.LEEmail.setReadOnly(True)
        self.LEBalance.setReadOnly(True)
        self.LEAccDate.setReadOnly(True)

        self.retranslateUi(CustomerProfile)
        QtCore.QMetaObject.connectSlotsByName(CustomerProfile)

        self.BSButton.clicked.connect(self.Back_To_Settings)

    def Back_To_Settings(self):
        CustomerSettings.show()
        CustomerProfile.hide()

    def retranslateUi(self, CustomerProfile):
        _translate = QtCore.QCoreApplication.translate
        CustomerProfile.setWindowTitle(_translate("CustomerProfile", "Shop - Customer - Profile"))
        self.label.setText(_translate("CustomerProfile", "<html><head/><body><p><span style=\" font-size:36pt; color:#ffffff;\">Profile</span></p></body></html>"))
        self.label_2.setText(_translate("CustomerProfile", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Name</span></p></body></html>"))
        self.label_3.setText(_translate("CustomerProfile", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Username</span></p></body></html>"))
        self.label_4.setText(_translate("CustomerProfile", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Email</span></p></body></html>"))
        self.label_5.setText(_translate("CustomerProfile", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Account Balance</span></p></body></html>"))
        self.label_6.setText(_translate("CustomerProfile", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Member Since</span></p></body></html>"))
        self.label_7.setText(_translate("CustomerProfile", "<html><head/><body><p><span style=\" font-size:24pt; color:#00ff7f;\">Back To Settings</span></p></body></html>"))


class Ui_SellerSettings(object):
    global user_details
    def setupUi(self, SellerSettings):
        SellerSettings.setObjectName("SellerSettings")
        SellerSettings.resize(600, 600)
        SellerSettings.setMinimumSize(QtCore.QSize(600, 600))
        SellerSettings.setMaximumSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SellerSettings.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(SellerSettings)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setMinimumSize(QtCore.QSize(600, 600))
        self.background.setMaximumSize(QtCore.QSize(600, 600))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 470, 211, 31))
        self.label.setObjectName("label")
        self.MenuButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.MenuButton.setGeometry(QtCore.QRect(190, 470, 211, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MenuButton.setIcon(icon1)
        self.MenuButton.setObjectName("MenuButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(520, 10, 71, 31))
        self.label_2.setObjectName("label_2")
        self.ProfileButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.ProfileButton.setGeometry(QtCore.QRect(520, 10, 71, 31))
        self.ProfileButton.setText("")
        self.ProfileButton.setIcon(icon1)
        self.ProfileButton.setObjectName("ProfileButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 60, 171, 71))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 170, 81, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 230, 141, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 290, 81, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 350, 121, 31))
        self.label_7.setObjectName("label_7")
        
        self.Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(270, 179, 181, 31))
        self.Name.setObjectName("Name")
        self.Name.setText(user_details[0])
        self.Name.textChanged.connect(self.Name_Change)

        self.Username = QtWidgets.QLineEdit(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(270, 230, 181, 31))
        self.Username.setObjectName("Username")
        self.Username.setText(user_details[1])
        self.Username.textChanged.connect(self.Username_Change)


        self.Email = QtWidgets.QLineEdit(self.centralwidget)
        self.Email.setGeometry(QtCore.QRect(270, 290, 181, 31))
        self.Email.setObjectName("Email")
        self.Email.setText(user_details[2])
        self.Email.textChanged.connect(self.Email_Change)


        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(270, 350, 181, 31))
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.Password.setText(user_details[-1])
        self.Password.textChanged.connect(self.Password_Change)

        self.NameChangeButton = QtWidgets.QPushButton(self.centralwidget)
        self.NameChangeButton.setGeometry(QtCore.QRect(490, 180, 75, 23))
        self.NameChangeButton.setObjectName("NameChangeButton")
        self.NameChangeButton.setEnabled(False)
        self.NameChangeButton.clicked.connect(self.Change_Name)

        self.ShopNameChangeButton = QtWidgets.QPushButton(self.centralwidget)
        self.ShopNameChangeButton.setGeometry(QtCore.QRect(490, 230, 75, 23))
        self.ShopNameChangeButton.setObjectName("ShopNameChangeButton")
        self.ShopNameChangeButton.setEnabled(False)
        self.ShopNameChangeButton.clicked.connect(self.Change_Username)

        self.EmailChangeButton = QtWidgets.QPushButton(self.centralwidget)
        self.EmailChangeButton.setGeometry(QtCore.QRect(490, 290, 75, 23))
        self.EmailChangeButton.setObjectName("EmailChangeButton")
        self.EmailChangeButton.setEnabled(False)
        self.EmailChangeButton.clicked.connect(self.Change_Email)

        self.PasswordChangeButton = QtWidgets.QPushButton(self.centralwidget)
        self.PasswordChangeButton.setGeometry(QtCore.QRect(490, 350, 75, 23))
        self.PasswordChangeButton.setObjectName("PasswordChangeButton")
        self.PasswordChangeButton.setEnabled(False)
        self.PasswordChangeButton.clicked.connect(self.Change_Password)

        SellerSettings.setCentralWidget(self.centralwidget)

        self.retranslateUi(SellerSettings)
        QtCore.QMetaObject.connectSlotsByName(SellerSettings)

        self.MenuButton.clicked.connect(self.Back_To_Home)
        self.ProfileButton.clicked.connect(self.View_Profile)

    def Name_Change(self):
        if self.Name.text() != user_details[0]:
            self.NameChangeButton.setEnabled(True)
        else:
            self.NameChangeButton.setEnabled(False)

    def Change_Name(self):
        user_details[0] = self.Name.text()
        Change_The_Detail_In_File(0, Retrieve_User_Pos(user_details[1], 1), 0, user_details[0])
        Display_Message3(303)
        self.NameChangeButton.setEnabled(False)

    def Username_Change(self):
        if self.Username.text() != user_details[1]:
            self.ShopNameChangeButton.setEnabled(True)
        else:
            self.ShopNameChangeButton.setEnabled(False)

    def Change_Username(self):
        obj = Seller_Details()
        if obj.From_File_SHOP_NAME(self.Username.text()):
            Display_Message2(7)
            self.Username.setText(user_details[1])
        else:
            Remove_Old_Replace_New(2, user_details[1], self.Username.text())
            user_details[1] = self.Username.text()
            Change_The_Detail_In_File(1, Retrieve_User_Pos(user_details[2], 1), 1, user_details[1])
            Display_Message3(312)
            self.ShopNameChangeButton.setEnabled(False)

    def Email_Change(self):
        if self.Email.text() != user_details[2]:
            self.EmailChangeButton.setEnabled(True)
        else:
            self.EmailChangeButton.setEnabled(False)

    def Change_Email(self):
        obj = Seller_Details()
        if obj.From_File_Email(self.Email.text()):
            Display_Message2(4)
            self.Email.setText(user_details[2])
        else:
            Remove_Old_Replace_New(3, user_details[2], self.Email.text())
            user_details[2] = self.Email.text()
            Change_The_Detail_In_File(1, Retrieve_User_Pos(user_details[1], 1), 2, user_details[2])
            Display_Message3(309)
            self.EmailChangeButton.setEnabled(False)

    def Password_Change(self):
        if self.Password.text() != user_details[-1]:
            self.PasswordChangeButton.setEnabled(True)
        else:
            self.PasswordChangeButton.setEnabled(False)

    def Change_Password(self):
        user_details[-1] = self.Password.text()
        Change_The_Detail_In_File(1, Retrieve_User_Pos(user_details[1], 1), -1, user_details[-1])
        Display_Message3(300)
        self.PasswordChangeButton.setEnabled(False)

    def View_Profile(self):
        global ui14
        ui14.setupUi(SellerProfile)
        SellerProfile.show()
        SellerSettings.hide()

    def Back_To_Home(self):
        global ui10
        ui10.setupUi(SellerHP)
        SellerHP.show()
        SellerSettings.hide()

    def retranslateUi(self, SellerSettings):
        _translate = QtCore.QCoreApplication.translate
        SellerSettings.setWindowTitle(_translate("SellerSettings", "Shop - Seller Settings"))
        self.label.setText(_translate("SellerSettings", "<html><head/><body><p><span style=\" font-size:18pt; color:#00aa00;\">Back To Main Menu</span></p></body></html>"))
        self.label_2.setText(_translate("SellerSettings", "<html><head/><body><p><span style=\" font-size:18pt; color:#0000ff;\">Profile</span></p></body></html>"))
        self.label_3.setText(_translate("SellerSettings", "<html><head/><body><p><span style=\" font-size:36pt; color:#ffffff;\">Settings</span></p></body></html>"))
        self.label_4.setText(_translate("SellerSettings", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">Name</span></p></body></html>"))
        self.label_5.setText(_translate("SellerSettings", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">Shopname</span></p></body></html>"))
        self.label_6.setText(_translate("SellerSettings", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">Email</span></p></body></html>"))
        self.label_7.setText(_translate("SellerSettings", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">Password</span></p></body></html>"))
        self.Name.setPlaceholderText(_translate("SellerSettings", "Your Name"))
        self.Username.setPlaceholderText(_translate("SellerSettings", "Your Shopname"))
        self.Email.setPlaceholderText(_translate("SellerSettings", "Your Email"))
        self.Password.setPlaceholderText(_translate("SellerSettings", "Your Password"))
        self.NameChangeButton.setText(_translate("SellerSettings", "Change"))
        self.ShopNameChangeButton.setText(_translate("SellerSettings", "Change"))
        self.EmailChangeButton.setText(_translate("SellerSettings", "Change"))
        self.PasswordChangeButton.setText(_translate("SellerSettings", "Change"))


class Ui_CustomerSettings(object):
    global user_details
    def setupUi(self, CustomerSettings):
        CustomerSettings.setObjectName("CustomerSettings")
        CustomerSettings.resize(600, 600)
        CustomerSettings.setMinimumSize(QtCore.QSize(600, 600))
        CustomerSettings.setMaximumSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CustomerSettings.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(CustomerSettings)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setMinimumSize(QtCore.QSize(600, 600))
        self.background.setMaximumSize(QtCore.QSize(600, 600))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 470, 211, 31))
        self.label.setObjectName("label")
        self.MenuButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.MenuButton.setGeometry(QtCore.QRect(190, 470, 211, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MenuButton.setIcon(icon1)
        self.MenuButton.setObjectName("MenuButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(520, 10, 71, 31))
        self.label_2.setObjectName("label_2")
        self.ProfileButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.ProfileButton.setGeometry(QtCore.QRect(520, 10, 71, 31))
        self.ProfileButton.setText("")
        self.ProfileButton.setIcon(icon1)
        self.ProfileButton.setObjectName("ProfileButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 60, 171, 71))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 170, 81, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 230, 131, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 290, 81, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 350, 121, 31))
        self.label_7.setObjectName("label_7")
        self.Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(270, 179, 181, 31))
        self.Name.setObjectName("Name")
        self.Name.setText(user_details[0])
        self.Name.textChanged.connect(self.Name_Change)

        self.Username = QtWidgets.QLineEdit(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(270, 230, 181, 31))
        self.Username.setObjectName("Username")
        self.Username.setText(user_details[1])
        self.Username.textChanged.connect(self.Username_Change)

        self.Email = QtWidgets.QLineEdit(self.centralwidget)
        self.Email.setGeometry(QtCore.QRect(270, 290, 181, 31))
        self.Email.setObjectName("Email")
        self.Email.setText(user_details[2])
        self.Email.textChanged.connect(self.Email_Change)

        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(270, 350, 181, 31))
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.Password.setText(user_details[-1])
        self.Password.textChanged.connect(self.Password_Change)

        self.NameChangeButton = QtWidgets.QPushButton(self.centralwidget)
        self.NameChangeButton.setGeometry(QtCore.QRect(490, 180, 75, 23))
        self.NameChangeButton.setObjectName("NameChangeButton")
        self.NameChangeButton.setEnabled(False)
        self.NameChangeButton.clicked.connect(self.Change_Name)
        
        self.UserNameChangeButton = QtWidgets.QPushButton(self.centralwidget)
        self.UserNameChangeButton.setGeometry(QtCore.QRect(490, 230, 75, 23))
        self.UserNameChangeButton.setObjectName("UserNameChangeButton")
        self.UserNameChangeButton.setEnabled(False)
        self.UserNameChangeButton.clicked.connect(self.Change_Username)
        
        self.EmailChangeButton = QtWidgets.QPushButton(self.centralwidget)
        self.EmailChangeButton.setGeometry(QtCore.QRect(490, 290, 75, 23))
        self.EmailChangeButton.setObjectName("EmailChangeButton")
        self.EmailChangeButton.setEnabled(False)
        self.EmailChangeButton.clicked.connect(self.Change_Email)
        
        self.PasswordChangeButton = QtWidgets.QPushButton(self.centralwidget)
        self.PasswordChangeButton.setGeometry(QtCore.QRect(490, 350, 75, 23))
        self.PasswordChangeButton.setObjectName("PasswordChangeButton")
        self.PasswordChangeButton.setEnabled(False)
        self.PasswordChangeButton.clicked.connect(self.Change_Password)
        
        CustomerSettings.setCentralWidget(self.centralwidget)

        self.retranslateUi(CustomerSettings)
        QtCore.QMetaObject.connectSlotsByName(CustomerSettings)

        self.MenuButton.clicked.connect(self.Back_To_Home)
        self.ProfileButton.clicked.connect(self.View_Profile)

    def Name_Change(self):
        if self.Name.text() != user_details[0]:
            self.NameChangeButton.setEnabled(True)
        else:
            self.NameChangeButton.setEnabled(False)

    def Change_Name(self):
        user_details[0] = self.Name.text()
        Change_The_Detail_In_File(0, Retrieve_User_Pos(user_details[1], 0), 0, user_details[0])
        Display_Message3(303)
        self.NameChangeButton.setEnabled(False)

    def Username_Change(self):
        if self.Username.text() != user_details[1]:
            self.UserNameChangeButton.setEnabled(True)
        else:
            self.UserNameChangeButton.setEnabled(False)

    def Change_Username(self):
        obj = Customer_Details()
        if obj.From_File_Username(self.Username.text()):
            Display_Message2(3)
            self.Username.setText(user_details[1])
        else:
            Remove_Old_Replace_New(0, user_details[1], self.Username.text())
            user_details[1] = self.Username.text()
            Change_The_Detail_In_File(0, Retrieve_User_Pos(user_details[2], 0), 1, user_details[1])
            Display_Message3(306)
            self.UserNameChangeButton.setEnabled(False)

    def Email_Change(self):
        if self.Email.text() != user_details[2]:
            self.EmailChangeButton.setEnabled(True)
        else:
            self.EmailChangeButton.setEnabled(False)

    def Change_Email(self):
        obj = Customer_Details()
        if obj.From_File_Email(self.Email.text()):
            Display_Message2(4)
            self.Email.setText(user_details[2])
        else:
            Remove_Old_Replace_New(1, user_details[2], self.Email.text())
            user_details[2] = self.Email.text()
            Change_The_Detail_In_File(0, Retrieve_User_Pos(user_details[1], 0), 2, user_details[2])
            Display_Message3(309)
            self.EmailChangeButton.setEnabled(False)

    def Password_Change(self):
        if self.Password.text() != user_details[-1]:
            self.PasswordChangeButton.setEnabled(True)
        else:
            self.PasswordChangeButton.setEnabled(False)

    def Change_Password(self):
        user_details[-1] = self.Password.text()
        Change_The_Detail_In_File(0, Retrieve_User_Pos(user_details[1], 0), -1, user_details[-1])
        Display_Message3(300)
        self.PasswordChangeButton.setEnabled(False)

    def View_Profile(self):
        global ui13
        ui13.setupUi(CustomerProfile)
        CustomerProfile.show()
        CustomerSettings.hide()

    def Back_To_Home(self):
        global ui9
        ui9.setupUi(CustomerHP)
        CustomerHP.show()
        CustomerSettings.hide()

    def retranslateUi(self, CustomerSettings):
        _translate = QtCore.QCoreApplication.translate
        CustomerSettings.setWindowTitle(_translate("CustomerSettings", "Shop - Customer Settings"))
        self.label.setText(_translate("CustomerSettings", "<html><head/><body><p><span style=\" font-size:18pt; color:#00aa00;\">Back To Main Menu</span></p></body></html>"))
        self.label_2.setText(_translate("CustomerSettings", "<html><head/><body><p><span style=\" font-size:18pt; color:#0000ff;\">Profile</span></p></body></html>"))
        self.label_3.setText(_translate("CustomerSettings", "<html><head/><body><p><span style=\" font-size:36pt; color:#ffffff;\">Settings</span></p></body></html>"))
        self.label_4.setText(_translate("CustomerSettings", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">Name</span></p></body></html>"))
        self.label_5.setText(_translate("CustomerSettings", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">Username</span></p></body></html>"))
        self.label_6.setText(_translate("CustomerSettings", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">Email</span></p></body></html>"))
        self.label_7.setText(_translate("CustomerSettings", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">Password</span></p></body></html>"))
        self.Name.setPlaceholderText(_translate("CustomerSettings", "Your Name"))
        self.Username.setPlaceholderText(_translate("CustomerSettings", "Your Username"))
        self.Email.setPlaceholderText(_translate("CustomerSettings", "Your Email"))
        self.Password.setPlaceholderText(_translate("CustomerSettings", "Your Password"))
        self.NameChangeButton.setText(_translate("CustomerSettings", "Change"))
        self.UserNameChangeButton.setText(_translate("CustomerSettings", "Change"))
        self.EmailChangeButton.setText(_translate("CustomerSettings", "Change"))
        self.PasswordChangeButton.setText(_translate("CustomerSettings", "Change"))


class Ui_SellerHP(object):
    def setupUi(self, SellerHP):
        SellerHP.setObjectName("SellerHP")
        SellerHP.resize(600, 600)
        SellerHP.setMinimumSize(QtCore.QSize(600, 600))
        SellerHP.setMaximumSize(QtCore.QSize(600, 600))
        SellerHP.setBaseSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SellerHP.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(SellerHP)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setMinimumSize(QtCore.QSize(600, 600))
        self.background.setMaximumSize(QtCore.QSize(600, 600))
        self.background.setBaseSize(QtCore.QSize(600, 600))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.Seller_Logo = QtWidgets.QLabel(self.centralwidget)
        self.Seller_Logo.setGeometry(QtCore.QRect(90, -60, 411, 321))
        self.Seller_Logo.setText("")
        self.Seller_Logo.setPixmap(QtGui.QPixmap(":/newPrefix/sell_logo.png"))
        self.Seller_Logo.setScaledContents(True)
        self.Seller_Logo.setObjectName("Seller_Logo")
        self.SettingsButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.SettingsButton.setGeometry(QtCore.QRect(200, 170, 181, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SettingsButton.setIcon(icon1)
        self.SettingsButton.setObjectName("SettingsButton")
        self.PaymentsButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.PaymentsButton.setGeometry(QtCore.QRect(200, 250, 181, 51))
        self.PaymentsButton.setIcon(icon1)
        self.PaymentsButton.setObjectName("PaymentsButton")
        self.Warehouse_Button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Warehouse_Button.setGeometry(QtCore.QRect(200, 330, 181, 51))
        self.Warehouse_Button.setIcon(icon1)
        self.Warehouse_Button.setObjectName("Warehouse_Button")
        self.LogOutButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.LogOutButton.setGeometry(QtCore.QRect(200, 410, 181, 51))
        self.LogOutButton.setIcon(icon1)
        self.LogOutButton.setObjectName("LogOutButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 170, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 250, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 330, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 410, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(220, 210, 141, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(220, 290, 141, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(220, 370, 141, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(220, 450, 141, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.background.raise_()
        self.Seller_Logo.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.LogOutButton.raise_()
        self.PaymentsButton.raise_()
        self.SettingsButton.raise_()
        self.Warehouse_Button.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        SellerHP.setCentralWidget(self.centralwidget)

        self.retranslateUi(SellerHP)
        QtCore.QMetaObject.connectSlotsByName(SellerHP)

        self.LogOutButton.clicked.connect(self.Log_Out_Clicked)
        self.SettingsButton.clicked.connect(self.Settings)
        self.PaymentsButton.clicked.connect(self.Payments)
        self.Warehouse_Button.clicked.connect(self.Warehouse)

    def Settings(self):
        global ui12
        ui12.setupUi(SellerSettings)
        SellerSettings.show()
        SellerHP.hide()

    def Warehouse(self):
        global ui17
        ui17.setupUi(SellerWarehouse)
        SellerWarehouse.show()
        SellerHP.hide()

    def Payments(self):
        global ui16
        ui16.setupUi(SellerPayments)
        SellerPayments.show()
        SellerHP.hide()

    def Log_Out_Clicked(self):
        Display_Message3(67)
        After_Splash.show()
        SellerHP.hide()

    def retranslateUi(self, SellerHP):
        _translate = QtCore.QCoreApplication.translate
        SellerHP.setWindowTitle(_translate("SellerHP", "Shop - Seller"))
        self.label.setText(_translate("SellerHP", "<html><head/><body><p><span style=\" font-size:18pt; color:#ff0000;\">Settings</span></p></body></html>"))
        self.label_2.setText(_translate("SellerHP", "<html><head/><body><p><span style=\" font-size:18pt; color:#5500ff;\">Payments</span></p></body></html>"))
        self.label_3.setText(_translate("SellerHP", "<html><head/><body><p><span style=\" font-size:18pt; color:#ff0000;\">Warehouse</span></p></body></html>"))
        self.label_4.setText(_translate("SellerHP", "<html><head/><body><p><span style=\" font-size:18pt; color:#0000ff;\">Log Out</span></p></body></html>"))


class Ui_CustomerHP(object):
    def setupUi(self, CustomerHP):
        CustomerHP.setObjectName("CustomerHP")
        CustomerHP.resize(600, 600)
        CustomerHP.setMinimumSize(QtCore.QSize(600, 600))
        CustomerHP.setMaximumSize(QtCore.QSize(600, 600))
        CustomerHP.setBaseSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CustomerHP.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(CustomerHP)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setMinimumSize(QtCore.QSize(600, 600))
        self.background.setMaximumSize(QtCore.QSize(600, 600))
        self.background.setBaseSize(QtCore.QSize(600, 600))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.Customer_Logo = QtWidgets.QLabel(self.centralwidget)
        self.Customer_Logo.setGeometry(QtCore.QRect(90, -60, 411, 321))
        self.Customer_Logo.setText("")
        self.Customer_Logo.setPixmap(QtGui.QPixmap(":/newPrefix/cust_logo.png"))
        self.Customer_Logo.setScaledContents(True)
        self.Customer_Logo.setObjectName("Customer_Logo")
        self.SettingsButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.SettingsButton.setGeometry(QtCore.QRect(200, 170, 181, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SettingsButton.setIcon(icon1)
        self.SettingsButton.setObjectName("SettingsButton")
        self.PaymentsButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.PaymentsButton.setGeometry(QtCore.QRect(200, 250, 181, 51))
        self.PaymentsButton.setIcon(icon1)
        self.PaymentsButton.setObjectName("PaymentsButton")
        self.Shopping_Button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Shopping_Button.setGeometry(QtCore.QRect(200, 330, 181, 51))
        self.Shopping_Button.setIcon(icon1)
        self.Shopping_Button.setObjectName("Shopping_Button")
        self.LogOutButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.LogOutButton.setGeometry(QtCore.QRect(200, 410, 181, 51))
        self.LogOutButton.setIcon(icon1)
        self.LogOutButton.setObjectName("LogOutButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 170, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 250, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 330, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 410, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(210, 210, 161, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(210, 290, 161, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(210, 370, 161, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(210, 450, 161, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.background.raise_()
        self.Customer_Logo.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.LogOutButton.raise_()
        self.PaymentsButton.raise_()
        self.SettingsButton.raise_()
        self.Shopping_Button.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        CustomerHP.setCentralWidget(self.centralwidget)

        self.retranslateUi(CustomerHP)
        QtCore.QMetaObject.connectSlotsByName(CustomerHP)
        self.LogOutButton.clicked.connect(self.Log_Out_Clicked)
        self.SettingsButton.clicked.connect(self.Settings)
        self.PaymentsButton.clicked.connect(self.Payments)
        self.Shopping_Button.clicked.connect(self.Shopping)

    def Shopping(self):
        global ui19
        ui19.setupUi(Customer_Shopping)
        Customer_Shopping.show()
        CustomerHP.hide()

    def Settings(self):
        global ui11
        ui11.setupUi(CustomerSettings)
        CustomerSettings.show()
        CustomerHP.hide()

    def Payments(self):
        global ui15
        ui15.setupUi(CustomerPayments)
        CustomerPayments.show()
        CustomerHP.hide()

    def Log_Out_Clicked(self):
        Display_Message3(67)
        After_Splash.show()
        CustomerHP.hide()

    def retranslateUi(self, CustomerHP):
        _translate = QtCore.QCoreApplication.translate
        CustomerHP.setWindowTitle(_translate("CustomerHP", "Shop - Customer"))
        self.label.setText(_translate("CustomerHP", "<html><head/><body><p><span style=\" font-size:18pt; color:#ff0000;\">Settings</span></p></body></html>"))
        self.label_2.setText(_translate("CustomerHP", "<html><head/><body><p><span style=\" font-size:18pt; color:#5500ff;\">Payments</span></p></body></html>"))
        self.label_3.setText(_translate("CustomerHP", "<html><head/><body><p><span style=\" font-size:18pt; color:#ff0000;\">Store</span></p></body></html>"))
        self.label_4.setText(_translate("CustomerHP", "<html><head/><body><p><span style=\" font-size:18pt; color:#0000ff;\">Log Out</span></p></body></html>"))


class Ui_Cust_Forgot(object):
    def setupUi(self, Cust_Forgot):
        Cust_Forgot.setObjectName("Cust_Forgot")
        Cust_Forgot.resize(440, 292)
        Cust_Forgot.setMinimumSize(QtCore.QSize(440, 292))
        Cust_Forgot.setMaximumSize(QtCore.QSize(440, 292))
        Cust_Forgot.setBaseSize(QtCore.QSize(440, 292))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Cust_Forgot.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Cust_Forgot)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 440, 320))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(120, 20, 191, 31))
        self.Title.setObjectName("Title")
        self.LVal = QtWidgets.QLabel(self.centralwidget)
        self.LVal.setGeometry(QtCore.QRect(20, 80, 141, 31))
        self.LVal.setObjectName("LVal")
        self.LNP = QtWidgets.QLabel(self.centralwidget)
        self.LNP.setGeometry(QtCore.QRect(20, 120, 141, 31))
        self.LNP.setObjectName("LNP")
        self.LNP_2 = QtWidgets.QLabel(self.centralwidget)
        self.LNP_2.setGeometry(QtCore.QRect(20, 160, 171, 31))
        self.LNP_2.setObjectName("LNP_2")
        self.ValKey = QtWidgets.QLineEdit(self.centralwidget)
        self.ValKey.setGeometry(QtCore.QRect(210, 90, 181, 21))
        self.ValKey.setObjectName("ValKey")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(210, 130, 181, 21))
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.Password2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Password2.setGeometry(QtCore.QRect(210, 170, 181, 21))
        self.Password2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password2.setObjectName("Password2")
        self.ResetButton = QtWidgets.QPushButton(self.centralwidget)
        self.ResetButton.setGeometry(QtCore.QRect(150, 220, 131, 31))
        self.ResetButton.setObjectName("ResetButton")
        Cust_Forgot.setCentralWidget(self.centralwidget)

        self.retranslateUi(Cust_Forgot)
        QtCore.QMetaObject.connectSlotsByName(Cust_Forgot)
        self.ResetButton.clicked.connect(self.Changing_Password)

    def Changing_Password(self):
        global validating_key, changer_email
        try:
            if self.ValKey.text() != validating_key:
                raise Wrong_Validation_Key
            if self.Password.text() != self.Password2.text():
                raise Password_Not_Match
        except Wrong_Validation_Key:
            Display_Message2(10)
            self.ValKey.clear()
        except Password_Not_Match:
            Display_Message2(2)
            self.Password.clear()
            self.Password2.clear()
        else:
            Setting_New_Password(self.Password2.text()[:], changer_email[:], 0)
            Display_Message3(300)
            self.ValKey.clear()
            self.Password.clear()
            self.Password2.clear()
            Cust_Forgot.hide()

    def retranslateUi(self, Cust_Forgot):
        _translate = QtCore.QCoreApplication.translate
        Cust_Forgot.setWindowTitle(_translate("Cust_Forgot", "Customer Password Reset"))
        self.Title.setText(_translate("Cust_Forgot", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">Password Reset</span></p></body></html>"))
        self.LVal.setText(_translate("Cust_Forgot", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Validation Key</span></p></body></html>"))
        self.LNP.setText(_translate("Cust_Forgot", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">New Password</span></p></body></html>"))
        self.LNP_2.setText(_translate("Cust_Forgot", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Confirm Password</span></p></body></html>"))
        self.ValKey.setPlaceholderText(_translate("Cust_Forgot", "Check Your Email For Validation Key"))
        self.Password.setPlaceholderText(_translate("Cust_Forgot", "New Password"))
        self.Password2.setPlaceholderText(_translate("Cust_Forgot", "Confirm New Password"))
        self.ResetButton.setText(_translate("Cust_Forgot", "Reset"))


class Ui_Sell_Forgot(object):
    def setupUi(self, Sell_Forgot):
        Sell_Forgot.setObjectName("Sell_Forgot")
        Sell_Forgot.resize(440, 292)
        Sell_Forgot.setMinimumSize(QtCore.QSize(440, 292))
        Sell_Forgot.setMaximumSize(QtCore.QSize(440, 292))
        Sell_Forgot.setBaseSize(QtCore.QSize(440, 292))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Sell_Forgot.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Sell_Forgot)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 440, 320))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(120, 20, 191, 31))
        self.Title.setObjectName("Title")
        self.LVal = QtWidgets.QLabel(self.centralwidget)
        self.LVal.setGeometry(QtCore.QRect(20, 80, 141, 31))
        self.LVal.setObjectName("LVal")
        self.LNP = QtWidgets.QLabel(self.centralwidget)
        self.LNP.setGeometry(QtCore.QRect(20, 120, 141, 31))
        self.LNP.setObjectName("LNP")
        self.LNP_2 = QtWidgets.QLabel(self.centralwidget)
        self.LNP_2.setGeometry(QtCore.QRect(20, 160, 171, 31))
        self.LNP_2.setObjectName("LNP_2")
        self.ValKey = QtWidgets.QLineEdit(self.centralwidget)
        self.ValKey.setGeometry(QtCore.QRect(210, 90, 181, 21))
        self.ValKey.setObjectName("ValKey")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(210, 130, 181, 21))
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.Password2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Password2.setGeometry(QtCore.QRect(210, 170, 181, 21))
        self.Password2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password2.setObjectName("Password2")
        self.ResetButton = QtWidgets.QPushButton(self.centralwidget)
        self.ResetButton.setGeometry(QtCore.QRect(150, 220, 131, 31))
        self.ResetButton.setObjectName("ResetButton")
        Sell_Forgot.setCentralWidget(self.centralwidget)

        self.retranslateUi(Sell_Forgot)
        QtCore.QMetaObject.connectSlotsByName(Sell_Forgot)
        self.ResetButton.clicked.connect(self.Changing_Password)

    def Changing_Password(self):
        global validating_key, changer_email
        try:
            if self.ValKey.text() != validating_key:
                raise Wrong_Validation_Key
            if self.Password.text() != self.Password2.text():
                raise Password_Not_Match
        except Wrong_Validation_Key:
            Display_Message2(10)
            self.ValKey.clear()
        except Password_Not_Match:
            Display_Message2(2)
            self.Password.clear()
            self.Password2.clear()
        else:
            Setting_New_Password(self.Password2.text()[:], changer_email[:], 1)
            Display_Message3(300)
            self.ValKey.clear()
            self.Password.clear()
            self.Password2.clear()
            Sell_Forgot.hide()

    def retranslateUi(self, Sell_Forgot):
        _translate = QtCore.QCoreApplication.translate
        Sell_Forgot.setWindowTitle(_translate("Sell_Forgot", "Seller Password Reset"))
        self.Title.setText(_translate("Sell_Forgot", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">Password Reset</span></p></body></html>"))
        self.LVal.setText(_translate("Sell_Forgot", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Validation Key</span></p></body></html>"))
        self.LNP.setText(_translate("Sell_Forgot", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">New Password</span></p></body></html>"))
        self.LNP_2.setText(_translate("Sell_Forgot", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Confirm Password</span></p></body></html>"))
        self.ValKey.setPlaceholderText(_translate("Sell_Forgot", "Check Your Email For Validation Key"))
        self.Password.setPlaceholderText(_translate("Sell_Forgot", "New Password"))
        self.Password2.setPlaceholderText(_translate("Sell_Forgot", "Confirm New Password"))
        self.ResetButton.setText(_translate("Sell_Forgot", "Reset"))


class Ui_SellerLogin(object):
    def setupUi(self, SellerLogin):
        SellerLogin.setObjectName("SellerLogin")
        SellerLogin.resize(440, 320)
        SellerLogin.setMinimumSize(440, 320)
        SellerLogin.setMaximumSize(440, 320)
        SellerLogin.setBaseSize(440, 320)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SellerLogin.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(SellerLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 441, 321))
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.Background.setObjectName("Background")
        self.LTitle = QtWidgets.QLabel(self.centralwidget)
        self.LTitle.setGeometry(QtCore.QRect(150, 20, 191, 51))
        self.LTitle.setObjectName("LTitle")
        self.LSorE = QtWidgets.QLabel(self.centralwidget)
        self.LSorE.setGeometry(QtCore.QRect(10, 90, 191, 31))
        self.LSorE.setObjectName("LSorE")
        self.LP = QtWidgets.QLabel(self.centralwidget)
        self.LP.setGeometry(QtCore.QRect(10, 140, 181, 31))
        self.LP.setObjectName("LP")
        self.Shopname_Email = QtWidgets.QLineEdit(self.centralwidget)
        self.Shopname_Email.setGeometry(QtCore.QRect(220, 90, 191, 31))
        self.Shopname_Email.setClearButtonEnabled(False)
        self.Shopname_Email.setObjectName("Shopname_Email")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(220, 140, 191, 31))
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setClearButtonEnabled(False)
        self.Password.setObjectName("Password")
        self.LogCheck = QtWidgets.QRadioButton(self.centralwidget)
        self.LogCheck.setGeometry(QtCore.QRect(30, 190, 16, 17))
        self.LogCheck.setText("")
        self.LogCheck.setObjectName("LogCheck")
        self.LogButton = QtWidgets.QLabel(self.centralwidget)
        self.LogButton.setGeometry(QtCore.QRect(50, 180, 191, 31))
        self.LogButton.setObjectName("LogButton")
        self.Forgot_Click = QtWidgets.QLabel(self.centralwidget)
        self.Forgot_Click.setGeometry(QtCore.QRect(100, 290, 241, 20))
        self.Forgot_Click.setObjectName("Forgot_Click")
        self.Forgot_Button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Forgot_Button.setGeometry(QtCore.QRect(100, 291, 241, 20))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Forgot_Button.setIcon(icon1)
        self.Forgot_Button.setObjectName("Forgot_Button")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 230, 131, 41))
        self.pushButton.setObjectName("pushButton")
        SellerLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(SellerLogin)
        QtCore.QMetaObject.connectSlotsByName(SellerLogin)
        self.Forgot_Button.clicked.connect(self.Option_Reset_Clicked)
        self.pushButton.clicked.connect(self.Checking_Correct)

    def Option_Reset_Clicked(self):
        global validating_key, changer_email
        try:
            if self.Shopname_Email.text() == "" or "@" not in self.Shopname_Email.text():
                raise Invalid_Email
            oo = Seller_Details()
            if not oo.From_File_Email(self.Shopname_Email.text()):
                raise Email_Taken
            if not Internet_Available():
                raise No_Internet
        except Invalid_Email:
            Display_Message2(8)
        except Email_Taken:
            Display_Message2(9)
        except No_Internet:
            Display_Message(2)
        else:
            validating_key = Generate_Validation_Key()[:]
            changer_email = self.Shopname_Email.text()[:]
            Send_Validation_Email(self.Shopname_Email.text(), validating_key[:])
            Sell_Forgot.show()
            self.Shopname_Email.clear()
            self.Password.clear()
            SellerLogin.hide()

    def Checking_Correct(self):
        global user_details, ui14, ui10
        try:
            if not Customer_Seller_Log_In_Checking(self.Shopname_Email.text()[:], self.Password.text()[:], 1):
                raise Invalid_Username
        except Invalid_Username:
            Display_Message3(0)
        else:
            Display_Message3(1)
            user_details = Retrieve_User_Details(self.Shopname_Email.text()[:], 1)[:]
            ui14.setupUi(SellerProfile)
            ui10.setupUi(SellerHP)
            SellerHP.show()
            SellerLogin.hide()
            After_Splash.hide()
            if not self.LogCheck.isChecked():
                self.Shopname_Email.clear()
                self.Password.clear()

    def retranslateUi(self, SellerLogin):
        _translate = QtCore.QCoreApplication.translate
        SellerLogin.setWindowTitle(_translate("SellerLogin", "Seller Login"))
        self.LTitle.setText(_translate("SellerLogin", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">Seller Login</span></p></body></html>"))
        self.LSorE.setText(_translate("SellerLogin", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Shop Name/Email</span></p></body></html>"))
        self.LP.setText(_translate("SellerLogin", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Password</span></p></body></html>"))
        self.Shopname_Email.setPlaceholderText(_translate("SellerLogin", "Shop Name Or Email"))
        self.Password.setPlaceholderText(_translate("SellerLogin", "Password"))
        self.LogButton.setText(_translate("SellerLogin", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Keep Me Logged In</span></p></body></html>"))
        self.Forgot_Click.setText(_translate("SellerLogin", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Forgot Password ? Click Here</span></p></body></html>"))
        self.Forgot_Button.setText(_translate("SellerLogin", " "))
        self.pushButton.setText(_translate("SellerLogin", "Log In"))



class Ui_CustomerLogin(object):
    def setupUi(self, CustomerLogin):
        CustomerLogin.setObjectName("CustomerLogin")
        CustomerLogin.resize(440, 320)
        CustomerLogin.setMinimumSize(440, 320)
        CustomerLogin.setMaximumSize(440, 320)
        CustomerLogin.setBaseSize(440, 320)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CustomerLogin.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(CustomerLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 441, 321))
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.Background.setObjectName("Background")
        self.LTitle = QtWidgets.QLabel(self.centralwidget)
        self.LTitle.setGeometry(QtCore.QRect(120, 20, 191, 51))
        self.LTitle.setObjectName("LTitle")
        self.LUorE = QtWidgets.QLabel(self.centralwidget)
        self.LUorE.setGeometry(QtCore.QRect(10, 90, 181, 31))
        self.LUorE.setObjectName("LUorE")
        self.LP = QtWidgets.QLabel(self.centralwidget)
        self.LP.setGeometry(QtCore.QRect(10, 140, 181, 31))
        self.LP.setObjectName("LP")
        
        self.Username_Email = QtWidgets.QLineEdit(self.centralwidget)
        self.Username_Email.setGeometry(QtCore.QRect(220, 90, 191, 31))
        self.Username_Email.setClearButtonEnabled(False)
        self.Username_Email.setObjectName("Username_Email")
        
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(220, 140, 191, 31))
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setClearButtonEnabled(False)
        self.Password.setObjectName("Password")
        
        self.LogCheck = QtWidgets.QRadioButton(self.centralwidget)
        self.LogCheck.setGeometry(QtCore.QRect(30, 190, 16, 17))
        self.LogCheck.setText("")
        self.LogCheck.setObjectName("LogCheck")
        
        self.LogButton = QtWidgets.QLabel(self.centralwidget)
        self.LogButton.setGeometry(QtCore.QRect(50, 180, 191, 31))
        self.LogButton.setObjectName("LogButton")
        
        self.Forgot_Click = QtWidgets.QLabel(self.centralwidget)
        self.Forgot_Click.setGeometry(QtCore.QRect(100, 290, 241, 20))
        self.Forgot_Click.setObjectName("Forgot_Click")
        
        self.Forgot_Button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Forgot_Button.setGeometry(QtCore.QRect(100, 291, 241, 20))
        self.Forgot_Button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Forgot_Button.setIcon(icon1)
        self.Forgot_Button.setObjectName("Forgot_Button")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 230, 131, 41))
        self.pushButton.setObjectName("pushButton")
        
        CustomerLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(CustomerLogin)
        QtCore.QMetaObject.connectSlotsByName(CustomerLogin)
        self.Forgot_Button.clicked.connect(self.Resetting)
        self.pushButton.clicked.connect(self.Checking_Correct)

    def Resetting(self):
        global validating_key, changer_email
        try:
            if self.Username_Email.text() == "" or "@" not in self.Username_Email.text():
                raise Invalid_Email
            oo = Customer_Details()
            if not oo.From_File_Email(self.Username_Email.text()):
                raise Email_Taken
            if not Internet_Available():
                raise No_Internet
        except Invalid_Email:
            Display_Message2(8)
        except Email_Taken:
            Display_Message2(9)
        except No_Internet:
            Display_Message(2)
        else:
            validating_key = Generate_Validation_Key()[:]
            changer_email = self.Username_Email.text()[:]
            Send_Validation_Email(self.Username_Email.text(), validating_key[:])
            Cust_Forgot.show()
            self.Username_Email.clear()
            self.Password.clear()
            CustomerLogin.hide()

    def Checking_Correct(self):
        global user_details, ui13, ui9
        try:
            if not Customer_Seller_Log_In_Checking(self.Username_Email.text()[:], self.Password.text()[:], 0):
                raise Invalid_Username
        except Invalid_Username:
            Display_Message3(0)
        else:
            Display_Message3(1)
            user_details = Retrieve_User_Details(self.Username_Email.text()[:], 0)[:]
            ui13.setupUi(CustomerProfile)
            ui9.setupUi(CustomerHP)
            CustomerHP.show()
            CustomerLogin.hide()
            After_Splash.hide()
            if not self.LogCheck.isChecked():
                self.Username_Email.clear()
                self.Password.clear()

    def retranslateUi(self, CustomerLogin):
        _translate = QtCore.QCoreApplication.translate
        CustomerLogin.setWindowTitle(_translate("CustomerLogin", "Customer Login"))
        self.LTitle.setText(_translate("CustomerLogin", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">Customer Login</span></p></body></html>"))
        self.LUorE.setText(_translate("CustomerLogin", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Username/Email</span></p></body></html>"))
        self.LP.setText(_translate("CustomerLogin", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Password</span></p></body></html>"))
        self.Username_Email.setPlaceholderText(_translate("CustomerLogin", "Username Or Email"))
        self.Password.setPlaceholderText(_translate("CustomerLogin", "Password"))
        self.LogButton.setText(_translate("CustomerLogin", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Keep Me Logged In</span></p></body></html>"))
        self.Forgot_Click.setText(_translate("CustomerLogin", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Forgot Password ? Click Here</span></p></body></html>"))
        self.pushButton.setText(_translate("CustomerLogin", "Log In"))


class Ui_SellerRegistration(object):
    
    def Registration_Click(self):
        
        if not self.Agree_Button.isChecked():
            Display_Message(1)
            return
        if not Internet_Available():
            Display_Message(2)
            return 
        try:
            if self.ShopName.text() == "":
                raise Invalid_Username
            if self.Password.text() != self.Password2.text():
                raise Password_Not_Match
            obj = Seller_Details()
            if obj.From_File_SHOP_NAME(self.ShopName.text()):
                raise Username_Taken
            if obj.From_File_Email(self.Email.text()):
                raise Email_Taken
            if "@" not in self.Email.text():
                raise Invalid_Email
        except Invalid_Username:
            Display_Message2(6)
            self.ShopName.clear()
            return
        except Password_Not_Match:
            Display_Message2(2)
            self.Password.clear()
            self.Password2.clear()
            return 
        except Username_Taken:
            Display_Message2(7)
            self.ShopName.clear()
            return
        except Email_Taken:
            Display_Message2(4)
            self.Email.clear()
            return
        except Invalid_Email:
            Display_Message2(5)
            self.Email.clear()
            return
        else:
            To_Write_List = []
            To_Write_List.append(self.Name.text())
            To_Write_List.append(self.ShopName.text())
            To_Write_List.append(self.Email.text())
            To_Write_List.append("0")
            To_Write_List.append(Current_Time_Date())
            To_Write_List.append(self.Password.text())
            obj.Assign(self.ShopName.text()[:], self.Email.text()[:], self.Password.text()[:])
            obj.File_Write_All()
            del obj
            First_Write(To_Write_List[:], 1)
            try:
                Seller_Registration_Mail(self.Email.text(), self.Name.text(), self.ShopName.text())
            except:
                pass
            self.Name.clear()
            self.ShopName.clear()
            self.Email.clear()
            self.Password.clear()
            self.Password2.clear()
            Display_Message(3)
            SellerRegistration.hide()

    def setupUi(self, SellerRegistration):
        SellerRegistration.setObjectName("SellerRegistration")
        SellerRegistration.resize(420, 600)
        SellerRegistration.setMinimumSize(QtCore.QSize(420, 600))
        SellerRegistration.setMaximumSize(QtCore.QSize(420, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SellerRegistration.setWindowIcon(icon)
        SellerRegistration.setIconSize(QtCore.QSize(42, 42))
        self.centralwidget = QtWidgets.QWidget(SellerRegistration)
        self.centralwidget.setObjectName("centralwidget")
        self.background_3 = QtWidgets.QLabel(self.centralwidget)
        self.background_3.setGeometry(QtCore.QRect(0, 0, 420, 600))
        self.background_3.setMinimumSize(QtCore.QSize(420, 600))
        self.background_3.setMaximumSize(QtCore.QSize(420, 600))
        self.background_3.setBaseSize(QtCore.QSize(420, 600))
        self.background_3.setText("")
        self.background_3.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background_3.setObjectName("background_3")
        self.Upper_Logo = QtWidgets.QLabel(self.centralwidget)
        self.Upper_Logo.setGeometry(QtCore.QRect(70, 10, 371, 101))
        self.Upper_Logo.setScaledContents(True)
        self.Upper_Logo.setObjectName("Upper_Logo")
        
        self.Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(180, 139, 161, 31))
        self.Name.setObjectName("Name")
        
        self.ShopName = QtWidgets.QLineEdit(self.centralwidget)
        self.ShopName.setGeometry(QtCore.QRect(180, 189, 161, 31))
        self.ShopName.setClearButtonEnabled(False)
        self.ShopName.setObjectName("ShopName")
        
        self.Email = QtWidgets.QLineEdit(self.centralwidget)
        self.Email.setGeometry(QtCore.QRect(180, 240, 161, 31))
        self.Email.setObjectName("Email")
        
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(180, 290, 161, 31))
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        
        self.Password2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Password2.setGeometry(QtCore.QRect(180, 340, 161, 31))
        self.Password2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password2.setObjectName("Password2")
        
        self.Register_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Register_Button.setGeometry(QtCore.QRect(110, 470, 151, 41))
        self.Register_Button.setCheckable(False)
        self.Register_Button.setObjectName("Register_Button")
        
        self.Agree_Button = QtWidgets.QCheckBox(self.centralwidget)
        self.Agree_Button.setGeometry(QtCore.QRect(50, 410, 21, 20))
        self.Agree_Button.setChecked(True)
        self.Agree_Button.setTristate(False)
        self.Agree_Button.setObjectName("Agree_Button")
        
        self.AgreeText = QtWidgets.QLabel(self.centralwidget)
        self.AgreeText.setGeometry(QtCore.QRect(70, 400, 361, 31))
        self.AgreeText.setObjectName("AgreeText")
        
        self.LName = QtWidgets.QLabel(self.centralwidget)
        self.LName.setGeometry(QtCore.QRect(10, 140, 81, 31))
        self.LName.setObjectName("LName")
        self.LShopName = QtWidgets.QLabel(self.centralwidget)
        self.LShopName.setGeometry(QtCore.QRect(10, 190, 131, 31))
        self.LShopName.setObjectName("LShopName")
        self.LPassword = QtWidgets.QLabel(self.centralwidget)
        self.LPassword.setGeometry(QtCore.QRect(10, 310, 101, 31))
        self.LPassword.setObjectName("LPassword")
        self.LEmail = QtWidgets.QLabel(self.centralwidget)
        self.LEmail.setGeometry(QtCore.QRect(10, 240, 61, 31))
        self.LEmail.setObjectName("LEmail")
        SellerRegistration.setCentralWidget(self.centralwidget)

        self.retranslateUi(SellerRegistration)
        QtCore.QMetaObject.connectSlotsByName(SellerRegistration)

        self.Register_Button.clicked.connect(self.Registration_Click)

    def retranslateUi(self, SellerRegistration):
        _translate = QtCore.QCoreApplication.translate
        SellerRegistration.setWindowTitle(_translate("SellerRegistration", "Seller Registration"))
        self.Upper_Logo.setText(_translate("SellerRegistration", "<html><head/><body><p><span style=\" font-size:28pt; color:#ffffff;\">Seller Registration</span></p></body></html>"))
        self.Name.setPlaceholderText(_translate("SellerRegistration", "Name"))
        self.ShopName.setPlaceholderText(_translate("SellerRegistration", "Shop Name"))
        self.Email.setPlaceholderText(_translate("SellerRegistration", "Email Address"))
        self.Password.setPlaceholderText(_translate("SellerRegistration", "Password"))
        self.Password2.setPlaceholderText(_translate("SellerRegistration", "Confirm Password"))
        self.Register_Button.setText(_translate("SellerRegistration", "Register"))
        self.AgreeText.setText(_translate("SellerRegistration", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">I Agree To The Terms And Conditions</span></p></body></html>"))
        self.LName.setText(_translate("SellerRegistration", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">Name</span></p></body></html>"))
        self.LShopName.setText(_translate("SellerRegistration", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Shop Name</span></p></body></html>"))
        self.LPassword.setText(_translate("SellerRegistration", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Password</span></p></body></html>"))
        self.LEmail.setText(_translate("SellerRegistration", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Email</span></p></body></html>"))


class Ui_CustomerRegistration(object):

    def Registration_Check(self):
        if not self.Agree_Button.isChecked():
            Display_Message(1)
            return
        if not Internet_Available():
            Display_Message(2)
            return 
        try:
            if self.Username.text() == "":
                raise Invalid_Username
            if self.Password.text() != self.Password2.text():
                raise Password_Not_Match
            obj = Customer_Details()
            if obj.From_File_Username(self.Username.text()):
                raise Username_Taken
            if obj.From_File_Email(self.Email.text()):
                raise Email_Taken
            if "@" not in self.Email.text():
                raise Invalid_Email
        except Invalid_Username:
            Display_Message2(1)
            self.Username.clear()
            return
        except Password_Not_Match:
            Display_Message2(2)
            self.Password.clear()
            self.Password2.clear()
            return 
        except Username_Taken:
            Display_Message2(3)
            self.Username.clear()
            return
        except Email_Taken:
            Display_Message2(4)
            self.Email.clear()
            return
        except Invalid_Email:
            Display_Message2(5)
            self.Email.clear()
            return
        else:
            To_Write_List = []
            To_Write_List.append(self.Name.text())
            To_Write_List.append(self.Username.text())
            To_Write_List.append(self.Email.text())
            To_Write_List.append("0")
            To_Write_List.append(Current_Time_Date())
            To_Write_List.append(self.Password.text())
            obj.Assign(self.Username.text()[:], self.Email.text()[:], self.Password.text()[:])
            obj.File_Write_All()
            del obj
            First_Write(To_Write_List[:])
            try:
                Customer_Registration_Mail(self.Email.text(), self.Name.text())
            except:
                pass
            self.Name.clear()
            self.Username.clear()
            self.Email.clear()
            self.Password.clear()
            self.Password2.clear()
            Display_Message(3)
            CustomerRegistration.hide()


    def setupUi(self, CustomerRegistration):
        CustomerRegistration.setObjectName("CustomerRegistration")
        CustomerRegistration.resize(420, 600)
        CustomerRegistration.setMinimumSize(QtCore.QSize(420, 600))
        CustomerRegistration.setMaximumSize(QtCore.QSize(420, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CustomerRegistration.setWindowIcon(icon)
        CustomerRegistration.setIconSize(QtCore.QSize(42, 42))
        self.centralwidget = QtWidgets.QWidget(CustomerRegistration)
        self.centralwidget.setObjectName("centralwidget")
        self.background_3 = QtWidgets.QLabel(self.centralwidget)
        self.background_3.setGeometry(QtCore.QRect(0, 0, 420, 600))
        self.background_3.setMinimumSize(QtCore.QSize(420, 600))
        self.background_3.setMaximumSize(QtCore.QSize(420, 600))
        self.background_3.setBaseSize(QtCore.QSize(420, 600))
        self.background_3.setText("")
        self.background_3.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background_3.setObjectName("background_3")
        self.Upper_Logo = QtWidgets.QLabel(self.centralwidget)
        self.Upper_Logo.setGeometry(QtCore.QRect(30, 10, 371, 101))
        self.Upper_Logo.setScaledContents(True)
        self.Upper_Logo.setObjectName("Upper_Logo")
        
        self.Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(180, 139, 161, 31))
        self.Name.setObjectName("Name")
        
        self.Username = QtWidgets.QLineEdit(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(180, 189, 161, 31))
        self.Username.setObjectName("Username")
        
        self.Email = QtWidgets.QLineEdit(self.centralwidget)
        self.Email.setGeometry(QtCore.QRect(180, 240, 161, 31))
        self.Email.setObjectName("Email")
        
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(180, 290, 161, 31))
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        
        self.Password2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Password2.setGeometry(QtCore.QRect(180, 340, 161, 31))
        self.Password2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password2.setObjectName("Password2")
        
        self.Register_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Register_Button.setGeometry(QtCore.QRect(110, 470, 151, 41))
        self.Register_Button.setCheckable(False)
        self.Register_Button.setObjectName("Register_Button")
        
        
        self.Agree_Button = QtWidgets.QCheckBox(self.centralwidget)
        self.Agree_Button.setGeometry(QtCore.QRect(50, 410, 21, 20))
        self.Agree_Button.setChecked(True)
        self.Agree_Button.setTristate(False)
        self.Agree_Button.setObjectName("Agree_Button")
        
        self.AgreeText = QtWidgets.QLabel(self.centralwidget)
        self.AgreeText.setGeometry(QtCore.QRect(70, 400, 361, 31))
        self.AgreeText.setObjectName("AgreeText")
        self.LName = QtWidgets.QLabel(self.centralwidget)
        self.LName.setGeometry(QtCore.QRect(10, 140, 81, 31))
        self.LName.setObjectName("LName")
        self.LUsername = QtWidgets.QLabel(self.centralwidget)
        self.LUsername.setGeometry(QtCore.QRect(10, 190, 111, 31))
        self.LUsername.setObjectName("LUsername")
        self.LPassword = QtWidgets.QLabel(self.centralwidget)
        self.LPassword.setGeometry(QtCore.QRect(10, 310, 101, 31))
        self.LPassword.setObjectName("LPassword")
        self.LEmail = QtWidgets.QLabel(self.centralwidget)
        self.LEmail.setGeometry(QtCore.QRect(10, 240, 61, 31))
        self.LEmail.setObjectName("LEmail")
        CustomerRegistration.setCentralWidget(self.centralwidget)

        self.retranslateUi(CustomerRegistration)
        QtCore.QMetaObject.connectSlotsByName(CustomerRegistration)

        self.Register_Button.clicked.connect(self.Registration_Check)

    def retranslateUi(self, CustomerRegistration):
        _translate = QtCore.QCoreApplication.translate
        CustomerRegistration.setWindowTitle(_translate("CustomerRegistration", "Customer Registration"))
        self.Upper_Logo.setText(_translate("CustomerRegistration", "<html><head/><body><p><span style=\" font-size:28pt; color:#ffffff;\">Customer Registration</span></p></body></html>"))
        self.Name.setPlaceholderText(_translate("CustomerRegistration", "Name"))
        self.Username.setPlaceholderText(_translate("CustomerRegistration", "Username"))
        self.Email.setPlaceholderText(_translate("CustomerRegistration", "Email Address"))
        self.Password.setPlaceholderText(_translate("CustomerRegistration", "Password"))
        self.Password2.setPlaceholderText(_translate("CustomerRegistration", "Confirm Password"))
        self.Register_Button.setText(_translate("CustomerRegistration", "Register"))
        self.AgreeText.setText(_translate("CustomerRegistration", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">I Agree To The Terms And Conditions</span></p></body></html>"))
        self.LName.setText(_translate("CustomerRegistration", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">Name</span></p></body></html>"))
        self.LUsername.setText(_translate("CustomerRegistration", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Username</span></p></body></html>"))
        self.LPassword.setText(_translate("CustomerRegistration", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Password</span></p></body></html>"))
        self.LEmail.setText(_translate("CustomerRegistration", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Email</span></p></body></html>"))


class Ui_After_Splash(object):
    def Customer_Registration(self):
        CustomerRegistration.show()

    def Seller_Registration(self):
        SellerRegistration.show()

    def Customer_Login(self):
    	CustomerLogin.show()

    def Seller_Login(self):
    	SellerLogin.show()

    def setupUi(self, After_Splash):
        After_Splash.setObjectName("After_Splash")
        After_Splash.resize(600, 600)
        After_Splash.setMinimumSize(QtCore.QSize(600, 600))
        After_Splash.setMaximumSize(QtCore.QSize(600, 600))
        After_Splash.setBaseSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        After_Splash.setWindowIcon(icon)
        After_Splash.setIconSize(QtCore.QSize(42, 42))
        self.centralwidget = QtWidgets.QWidget(After_Splash)
        self.centralwidget.setObjectName("centralwidget")
        self.Background_1 = QtWidgets.QLabel(self.centralwidget)
        self.Background_1.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.Background_1.setMinimumSize(QtCore.QSize(600, 600))
        self.Background_1.setMaximumSize(QtCore.QSize(600, 600))
        self.Background_1.setText("")
        self.Background_1.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.Background_1.setScaledContents(True)
        self.Background_1.setObjectName("Background_1")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(70, -40, 431, 321))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"))
        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")
        self.Cust_Logo = QtWidgets.QLabel(self.centralwidget)
        self.Cust_Logo.setGeometry(QtCore.QRect(60, 200, 201, 58))
        self.Cust_Logo.setScaledContents(True)
        self.Cust_Logo.setObjectName("Cust_Logo")
        self.Sell_Logo = QtWidgets.QLabel(self.centralwidget)
        self.Sell_Logo.setGeometry(QtCore.QRect(400, 200, 121, 58))
        self.Sell_Logo.setScaledContents(True)
        self.Sell_Logo.setObjectName("Sell_Logo")
        
        self.cust_regis = QtWidgets.QPushButton(self.centralwidget)
        self.cust_regis.setGeometry(QtCore.QRect(60, 280, 201, 41))
        self.cust_regis.setObjectName("cust_regis")
        
        
        self.sell_regis = QtWidgets.QPushButton(self.centralwidget)
        self.sell_regis.setGeometry(QtCore.QRect(350, 280, 201, 41))
        self.sell_regis.setObjectName("sell_regis")
        
        self.cust_log_in = QtWidgets.QPushButton(self.centralwidget)
        self.cust_log_in.setGeometry(QtCore.QRect(60, 340, 201, 41))
        self.cust_log_in.setObjectName("cust_log_in")
        
        self.sell_log_in = QtWidgets.QPushButton(self.centralwidget)
        self.sell_log_in.setGeometry(QtCore.QRect(350, 340, 201, 41))
        self.sell_log_in.setObjectName("sell_log_in")
        
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(293, 280, 20, 111))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        After_Splash.setCentralWidget(self.centralwidget)

        self.retranslateUi(After_Splash)
        QtCore.QMetaObject.connectSlotsByName(After_Splash)

        self.cust_regis.clicked.connect(self.Customer_Registration)
        self.sell_regis.clicked.connect(self.Seller_Registration)
        self.cust_log_in.clicked.connect(self.Customer_Login)
        self.sell_log_in.clicked.connect(self.Seller_Login)

    def retranslateUi(self, After_Splash):
        _translate = QtCore.QCoreApplication.translate
        After_Splash.setWindowTitle(_translate("After_Splash", "Form"))
        self.Cust_Logo.setText(_translate("After_Splash", "<html><head/><body><p><span style=\" font-size:36pt; color:#ffffff;\">Customer</span></p></body></html>"))
        self.Sell_Logo.setText(_translate("After_Splash", "<html><head/><body><p><span style=\" font-size:36pt; color:#ffffff;\">Seller</span></p></body></html>"))
        self.cust_regis.setText(_translate("After_Splash", "Register"))
        self.sell_regis.setText(_translate("After_Splash", "Register"))
        self.cust_log_in.setText(_translate("After_Splash", "Log In"))
        self.sell_log_in.setText(_translate("After_Splash", "Log In"))


class Ui_Splash_Screen(object):

    def Main_Click(self):
        After_Splash.show()
        Splash_Screen.hide()

    def setupUi(self, Splash_Screen):
        Splash_Screen.setObjectName("Splash_Screen")
        Splash_Screen.resize(600, 600)
        Splash_Screen.setMinimumSize(QtCore.QSize(600, 600))
        Splash_Screen.setMaximumSize(QtCore.QSize(600, 600))
        Splash_Screen.setBaseSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Splash_Screen.setWindowIcon(icon)
        Splash_Screen.setIconSize(QtCore.QSize(200, 200))
        self.centralwidget = QtWidgets.QWidget(Splash_Screen)
        self.centralwidget.setObjectName("centralwidget")
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap(":/newPrefix/splash_screen.png"))
        self.Background.setObjectName("Background")
        self.main_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.main_button.setGeometry(QtCore.QRect(160, 180, 301, 181))
        self.main_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_button.setIcon(icon1)
        self.main_button.setObjectName("main_button")
        self.main_button.clicked.connect(self.Main_Click)
        Splash_Screen.setCentralWidget(self.centralwidget)

        self.retranslateUi(Splash_Screen)
        QtCore.QMetaObject.connectSlotsByName(Splash_Screen)

    def retranslateUi(self, Splash_Screen):
        _translate = QtCore.QCoreApplication.translate
        Splash_Screen.setWindowTitle(_translate("Splash_Screen", "Shop"))


if __name__ == "__main__":
    Initialise()

    app = QtWidgets.QApplication(sys.argv)

    Product_Details = QtWidgets.QMainWindow()
    ui21 = Ui_Product_Details()

    Customer_Cart = QtWidgets.QMainWindow()
    ui20 = Ui_Customer_Cart()

    Customer_Shopping = QtWidgets.QMainWindow()
    ui19 = Ui_Customer_Shopping()

    AddItem = QtWidgets.QMainWindow()
    ui18 = Ui_AddItem()

    SellerWarehouse = QtWidgets.QMainWindow()
    ui17 = Ui_SellerWarehouse()

    SellerPayments = QtWidgets.QMainWindow()
    ui16 = Ui_SellerPayments()

    CustomerPayments = QtWidgets.QMainWindow()
    ui15 = Ui_CustomerPayments()

    SellerProfile = QtWidgets.QMainWindow()
    ui14 = Ui_SellerProfile()

    CustomerProfile = QtWidgets.QMainWindow()
    ui13 = Ui_CustomerProfile()

    SellerSettings = QtWidgets.QMainWindow()
    ui12 = Ui_SellerSettings()
    ui12.setupUi(SellerSettings)

    CustomerSettings = QtWidgets.QMainWindow()
    ui11 = Ui_CustomerSettings()
    ui11.setupUi(CustomerSettings)

    SellerHP = QtWidgets.QMainWindow()
    ui10 = Ui_SellerHP()
    ui10.setupUi(SellerHP)

    CustomerHP = QtWidgets.QMainWindow()
    ui9 = Ui_CustomerHP()
    ui9.setupUi(CustomerHP)

    Sell_Forgot = QtWidgets.QMainWindow()
    ui8 = Ui_Sell_Forgot()
    ui8.setupUi(Sell_Forgot)

    Cust_Forgot = QtWidgets.QMainWindow()
    ui7 = Ui_Cust_Forgot()
    ui7.setupUi(Cust_Forgot)

    SellerLogin = QtWidgets.QMainWindow()
    ui6 = Ui_SellerLogin()
    ui6.setupUi(SellerLogin)

    CustomerLogin = QtWidgets.QMainWindow()
    ui5 = Ui_CustomerLogin()
    ui5.setupUi(CustomerLogin)

    SellerRegistration = QtWidgets.QMainWindow()
    ui4 = Ui_SellerRegistration()
    ui4.setupUi(SellerRegistration)
    
    CustomerRegistration = QtWidgets.QMainWindow()
    ui3 = Ui_CustomerRegistration()
    ui3.setupUi(CustomerRegistration)
    
    After_Splash = QtWidgets.QMainWindow()
    ui2 = Ui_After_Splash()
    ui2.setupUi(After_Splash)
    
    Splash_Screen = QtWidgets.QMainWindow()
    ui = Ui_Splash_Screen()
    ui.setupUi(Splash_Screen)
    
    Splash_Screen.show()
    
    sys.exit(app.exec_())