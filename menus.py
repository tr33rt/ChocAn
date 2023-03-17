#Sienna Day
#CS 314
#ChocAn Term Project
#This file contains the account and controller classes

#Need to add
  #Checking for input data types
  #Create return oppurtunities from sub to main menu
  #Update user file upon editing

import datamanagerhold
import class_objects
from class_objects import *
from datetime import datetime
from random import randint

#Holds one instance of a user account
class account:
  #Initialize object
  def __init__(self, name, user, password, access):
    self.name = name
    self.user = user
    self.password = password
    self.access = access
#Displays and operates menus and forms

#Controls menus, submenus, forms, and account modification
class controller:
  def __init__(self):
      self.logins = []
      self.data_manager = datamanagerhold.data_manager()

  
  #Check if username is in the accounts list for new user creation
  def username_check(self, username): 
    for i in self.logins:
      if(i.user == username):
        return True
    return False
  def account_check(self, username, password):
    hold = [account for account in self.logins if (account.user == username and account.password == password)]
    if (hold == []):
      return -1
    else:
      return int(hold[0].access)
  def import_accounts(self):
    holdthis = open("account_info.txt", "r")
    data = holdthis.readlines()
    x = 0
    for line in data:
      row = line.split(',')
      name, username, password, access_level = [i.strip() for i in row]
      account_info = account(name, username, password, access_level)
      self.logins.append(account_info)
      x+=1

  def startup(self):
    self.import_accounts()    
    self.data_manager.import_members()
    self.data_manager.import_providers()
    
    print("Welcome to the ChocAn data management system, this is an intermediary system meant to be later connected to a different user interface. \n")
    x = 5
    access_level = -1
    username = input("username: ")
    password = input("password: ")
    access_level = self.account_check(username, password)
    while (access_level < 0 and x >= 0):
        print("That account information is incorrect. You have " + str(x) + " more tries before you are locked out")
        username = input("username: ")
        password = input("password: ")
        access_level = self.account_check(username, password)
        x -= 1
    if (x == -1):
      print("You have run out of tries for this session - reboot the session to try again")
    else:
      print("Welcome to your ChocAn dashboard " + username)
    self.menu(access_level)
#Go to corresponding menu based on access level
  def menu(self, access_level):
    match access_level:
      case 1:
        self.provider_menu()
        return 1
      case 2: 
        self.manager_menu()
        return 1
      case 3:
        self.admin_menu()
        return 1
  #Display menus and forms for provider level access
  def provider_menu(self):
      print("[1] Validate member number")
      print("[2] Bill for services")
      print("[3] View provider directory")
      print("[4] Request services provided report")
      print("[X] Exit")
      menuval = input("Please enter the number corresponding to which menu item you would like to access: ")
      match menuval:
        case "1":
          if (self.member_verification() == True):
            print("Member number is valid")
          else:
            print("Member number is not valid")
        case "2":
          self.member_billing()
        case "3":
          pd = class_objects.provider_directory.list
          for i in pd:
            print(str(i.code) + " : " + i.desc)
        case "4":
          provider_id = int(input("Input Provider ID: "))
          self.data_manager.services_provided(provider_id)
        case "X":
          print("Thank you for using ChocAn. Goodbye!")
          quit()
      self.provider_menu()
  def admin_menu(self):
    exit_val = "N"
    while(exit_val == "N"): 
      print("[1] Validate member number")
      print("[2] Access provider directory")
      print("[3] Access member directory")
      print("[4] Request reports")
      print("[X] Exit")
      menuhold = input("Please enter the number corresponding to which menu item you would like to access: ")
      match menuhold:
        case "1":
          if (self.member_verification() == True):
            print("Member number is valid")
          else:
            print("Member number is not valid")
        case "2":
          self.provider_submenu()
        case "3":
          self.member_submenu()
        case "4":
          self.reports_submenu()
        case "5":
          self.user_submenu()
        case "X":
          print("Thank you for using ChocAn. Goodbye!")
          quit()
      self.admin_menu()
  #Display menus and forms for manager level access
  def manager_menu(self):
    exit_val = "N"
    while(exit_val == "N"):
      print("[1] Validate member number")
      print("[2] Access provider directory")
      print("[3] Access member directory")
      print("[4] Request reports")
      print("[X] Exit")
      menuval = input("Please enter the number corresponding to which menu item you would like to access: ")
      match menuval:
        case "1":
          if (self.member_verification() == True):
            print("Member number is valid")
          else:
            print("Member number is not valid")
        case "2":
          self.provider_submenu()
        case "3":
          self.member_submenu()
        case "4":
          self.reports_submenu()
        case "X":
          print("Thank you for using ChocAn. Goodbye!")
          quit()
      self.manager_menu()
  def member_submenu(self):
    print("[1] Print member directory")
    print("[2] Add member")
    print("[3] Remove member")
    print("[4] Modify existing member")
    print("[X] Exit to main menu")
    menuval = input("Please enter the number corresponding to which menu item you would like to access: ")
    match menuval:
      case "1":
        self.data_manager.print_member()
      case "2":
        self.add_member()
      case "3":
        self.remove_member()
      case "4":
        self.edit_member()
      case "X":
        return
    self.member_submenu()
  def provider_submenu(self):
    print("[1] Print provider directory")
    print("[2] Add provider")
    print("[3] Remove provider")
    print("[4] Modify existing provider")
    print("[X] Return to main menu")
    menuval = input("Please enter the number corresponding to which menu item you would like to access: ")
    match menuval:
      case "1":
        self.data_manager.print_provider()
      case "2":
        self.add_provider()
      case "3":
        self.remove_provider()
      case "4":
        self.edit_provider()
      case "X":
        return
    self.provider_submenu()
  def user_submenu(self):
    print("[1] Print user directory")
    print("[2] Add user")
    print("[3] Remove user")
    print("[4] Modify existing user")
    print("[X] Return to main menu")
    menuval = input("Please enter the number corresponding to which menu item you would like to access: ")
    match menuval:
      case "1":
        self.print_user_list()
      case "2":
        self.add_user_form()
      case "3":
        self.remove_user_form()
      case "4":
        self.edit_user()
      case "X":
        return
    self.user_submenu()
  def reports_submenu(self):
    print("[1] Print services provided report")
    print("[2] Print services recieved report")
    print("[3] Print service fees report")
    print("[X] Exit to main menu")
    menuval = input("Please enter the number corresponding to which menu item you would like to access: ")
    match menuval:
      case "1":
        provider_id = int(input("Input Provider ID: "))
        self.data_manager.services_provided(provider_id)
      case "2":
        member_id = int(input("Input Member ID: "))
        self.data_manager.services_received(member_id)
      case "3":
        self.data_manager.service_fees()
      case "X":
        return
    self.reports_submenu()
  def remove_user_form(self):
    self.print_user_list()
    username = input("Enter username of user to remove: ")
    if (self.remove_user(username) > 0):
      print("User " + username + "'s account has been removed")
      self.print_user_list()
      return 1
    else:
      print("This username does not exist")
      print("[1] Retry new username")
      print("[2] Exit to previous menu")
      holdinput = input("Please enter the number corresponding to which menu item you would like to acccess")
      match holdinput:
        case "1":
          return self.remove_user_form()
        case "2":
          return
  def remove_user(self, username):
    holdlist = [account for account in self.logins if account.user == username]
    if (holdlist != None):
      obj = holdlist[0]
      i = self.logins.index(obj)
      self.logins.pop(i)
      return True
    return False
  def add_user_form(self):
    self.print_user_list()
    username = input("Enter username of user to add: ")
    if (self.username_check(username) < 0):
      name = input("Enter name for new user: ")
      password = input("Enter password for new user: ")
      access_level = input("Enter numerical access level for new user: ")
      self.logins.append(account(name, username, password, access_level))
      self.print_user_list()
      return 1
    else:
      print("This username already exists. Please select a different username")
      print("[1] Retry with new username")
      print("[2] Exit to previous menu")
      holdinput = input("Please enter the number corresponding to which menu item you would like to acccess")
      match holdinput:
        case "1":
          return self.add_user_form()
        case "2":
          return 
  def edit_user(self):
    self.print_user_list()
    username = input("Enter username of user to edit: ")
    if (self.username_check(username) > 0):
      holdlist = [account for account in self.logins if account.user == username]
      if (holdlist != None):
        obj = holdlist[0]
        i = self.logins.index(obj)
      self.logins[i].username = username
      name = input("Enter name for updated user: ")
      self.logins[i].name = name
      password = input("Enter password for updated user: ")
      self.logins[i].password = password
      access_level = input("Enter numerical access level for updated user: ")
      self.logins[i].access = access_level
      self.print_user_list()
      return 1
    else:
      print("This username does not exist. Please select a different username")
      print("[1] Retry with new username")
      print("[2] Exit to previous menu")
      holdinput = input("Please enter the number corresponding to which menu item you would like to acccess")
      match holdinput:
        case "1":
          return self.edit_user_form()
        case "2":
          return 
  def print_user_list(self):
    x = 0
    while(x < len(self.logins)):
      match self.logins[x].access:
        case "1":
          level = "Provider"
        case "2":
          level = "Manager"
        case "3":
          level = "Administrator"
      print("Name: " + self.logins[x].name + "\n Username: " + self.logins[x].user + "\n Password: " + self.logins[x].password + "\n Access Level: " + level)
      x += 1
    return
  def member_verification(self):
    id = input("Input Member ID: ")
    if(datamanagerhold.data_manager().member_check(id) == False):
      print("Invalid member number")
      print("[1] Retry with new member ID")
      print("[2] Return to menu")
      menuval = input("Please enter the number corresponding to which menu item you would like to access: ")
      match menuval:
        case "1":
          return self.member_verification()
        case "2":
          return False
    else:
      return True
  def member_billing(self):
    member_id = int(input("Input member ID or slide member card: "))
    if(datamanagerhold.data_manager().member_check(member_id) == False):
      print("Invalid member number")
      print("[1] Retry with new member ID")
      print("[2] Return to main menu")
      menuval = input("Please enter the number corresponding to which menu item you would like to access: ")
      match menuval:
        case "1":
          return self.member_billing()
        case "2":
          return
    else:
      print("Validated")
      DOS = input("Date of service: ")
      Service_ID = int(input("Service ID: "))
      Provider_ID = int(input("Provider ID: "))
      #search service directory
      holdlist = [class_objects.service for class_objects.service in self.data_manager.service_directory if service.code == Service_ID]
      if(holdlist == None):
        print("Incorrect Service ID, restarting form.")
        self.member_verification()
      if(holdlist):
        print(holdlist[0].code + ": " + holdlist[0].desc)
      holdval = input("Is this the service you provided today? \n [1] Yes \n [2] No \n")
      match holdval:
        case "1":
          comments = ("Comments: ")
          #Update once comments are added
          
          holdthis = [member for member in self.data_manager.member_directory if member.id == member_id]
          if (holdthis):
            member_name = holdthis[0].name
            fee = holdlist[0].fee
            timehold = datetime.now
            self.data_manager.provider_directory[len(self.data_manager.provider_directory)].addservice(provider_service(DOS, timehold.datetime(),  member_name, member_id, holdlist[0].code, fee, commments))
            print("The fee for this visit is: " + fee)
            return True
          else:
            print("There are no members under that ID, resetting form")
            self.member_billing()
        case "2":
          holdval2 = input("Would you like to \n [1] Reset the current form \n [2] Exit to main menu")
          match holdval2:
            case "1":
              self.member_billing()
            case "2":
              return

  def add_member(self):
    id = randint(10 ** (8), (10 ** 9) - 1)
    if(self.data_manager.member_check(id) == False):
      name = input("Member name: ")
      address = input("Member Address: ")
      city = input("Member city: ")
      state = input("Member state: ")
      zip = input("Member zip: ")
      self.data_manager.add_member(name, id, address, city, state, zip)
    else:
      hold = input("This member ID already exists. Would you like to try again with a different number? \n [1] Yes \n [2] No")
      match hold:
        case "1":
          return self.add_member()
        case "2":
          return
  def remove_member(self):
    id = int(input("ID of member to remove: "))
    if(self.data_manager.member_check(id) == True):
      self.data_manager.remove_member(id)
    else:
      hold = input("This member ID does not exist. Would you like to try again with a different number? \n [1] Yes \n [2] No \n")
      match hold:
        case "1":
          return self.remove_member()
        case "2":
          return
  def edit_member(self):
    id = int(input("ID of member to edit: "))
    if(self.data_manager.member_check(id) == True):
      name = input("Updated name of member: ")
      address = input("Updated address of member: ")
      city = input("Updated city of member: ")
      state = input("Updated state of member: ")
      zip = int(input("Updated zip of member: "))
      self.data_manager.edit_member(id, name, address, city, state, zip)
      return 1
    else:
      return -1

  def add_provider(self):
    id = id = randint(10 ** (8), (10 ** 9) - 1)
    if(self.data_manager.member_check(id) == False):
      name = input("Provider name: ")
      address = input("Provider Address: ")
      city = input("Provider city: ")
      state = input("Provider state: ")
      zip = input("Provider zip: ")
      self.data_manager.add_provider(name, id, address, city, state, zip)
    else:
      hold = input("This Provider ID already exists. Would you like to try again with a different number? \n [1] Yes \n [2] No")
      match hold:
        case "1":
          return self.add_provider()
        case "2":
          return
  def remove_provider(self):
    id = int(input("ID of provider to remove: "))
    if(self.data_manager.provider_check(id) == False):
      self.data_manager.remove_provider(id)
    else:
      hold = input("This provider ID does not exist. Would you like to try again with a different number? \n [1] Yes \n [2] No")
      match hold:
        case "1":
          return self.remove_provider()
        case "2":
          return
  def edit_provider(self):
    id = int(input("ID of provider to edit: "))
    if(self.data_manager.provider_check(id) == True):
      name = input("Updated name of Provider: ")
      address = input("Updated address of Provider: ")
      city = input("Updated city of Provider: ")
      state = input("Updated state of Provider: ")
      zip = input("Updated zip of Provider: ")
      self.data_manager.edit_provider(id, name, address, city, state, zip)
      return 1
    else:
      return -1

