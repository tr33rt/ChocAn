#Harrison Huynh and Sienna Day
#Contains holder functionality used by menus file

from class_objects import *
from datetime import datetime

  
class data_manager:
  def __init__(self):
    self.member_directory = []
    self.provider_directory = []
    self.service_directory = []
  def add_provider(self, name, id, address, city, state, zip):
    obj = provider(name, id, address, city, state, zip)
    self.provider_directory.append(obj)
    return True
  def remove_provider(self, provider_id):
    for i in self.provider_directory:
      if(i.id == provider_id):
        self.provider_directory.remove(i)
        return


  def edit_provider(self, id, name, address, city, state, zip):

    for i in self.provider_directory:
      if(i.id == id):
        i.change_name(name)
        i.change_address(address)
        i.change_city(city)
        i.change_state(state)
        i.change_zip(zip)

        
  def add_member(self, name, id, address, city, state, zip):
    obj = member(name, id, address, city, state, zip)
    self.member_directory.append(obj)
    return True
  def remove_member(self, member_id):
    for i in self.member_directory:
      if(i.id == member_id):
        self.member_directory.remove(i)
        return

  def edit_member(self, id, name, address, city, state, zip):

    for i in self.member_directory:
      if(i.id == id):
        i.change_name(name)
        i.change_address(address)
        i.change_city(city)
        i.change_state(state)
        i.change_zip(zip)

  def services_received(self, member_id):
    for i in self.member_directory:
      if(i.id == id):
        filename = i.name + '.txt'
        with open(filename, 'a',) as f:
          f.write('Name:' + i.name)
          f.write('Number:' + str(i.id))
          f.write('Street Address:' + i.address)
          f.write('City:' + i.city)
          f.write('State:' + i.state)
          f.write('Zip Code:' + str(i.zip))
          for j in i.services:
            f.write('Date of Service:' + str(j.date))
            f.write('Provider name:' + j.provider)
            f.write('Service name:' + j.service)

    return True
  def services_provided(self, provider_id):
    for i in self.provider_directory:
      if(i.id == id):
        filename = i.name + '.txt'
        with open(filename, 'a') as f:
          for j in i.services:
            f.write('Current date and time:' + str(datetime.now))
            f.write('Date service was provided' + str(j.service_date))
            f.write('Member name:' + j.member_name)
            f.write('Member number:' + j.member_id)
            f.write('Service code:' + j.service_code)
            f.write('Comments:' + j.comments)

    return True
  def service_fees(self):
    
    return True
  def member_check(self, member_id):
    #if member is in the list
    for i in self.member_directory:
      if(i.id == member_id):
        return True
    #if member is not in the list
    return False
    #return False
  def provider_check(self, provider_id):
    #if provider is in the listS
    for i in self.member_directory:
      if(i.get_id() == provider_id):
        return True
    #if provider is not in the list
    return False
  def import_members(self):
    file = open("members.txt", 'r')
    name = file.readline().replace("\n", "")
    
    while name != "":
      id = int(file.readline())
      address = file.readline().replace("\n", "")
      city = file.readline().replace("\n", "")
      state = file.readline().replace("\n", "")
      zip = int(file.readline())
      obj = member(name, id, address, city, state, zip)
      self.member_directory.append(obj)
      name = file.readline().replace("\n", "")
      

    file.close()

  def import_providers(self):
    file = open("members.txt", 'r')
    name = file.readline().replace("\n", "")
    
    while name != "":
      id = int(file.readline())
      address = file.readline().replace("\n", "")
      city = file.readline().replace("\n", "")
      state = file.readline().replace("\n", "")
      zip = int(file.readline())
      obj = member(name, id, address, city, state, zip)
      self.provider_directory.append(obj)
      name = file.readline().replace("\n", "")

    file.close()

  def print_member(self):
    for i in self.member_directory:
      i.display()
    return True
  def print_provider(self):
    for i in self.provider_directory:
      i.display()
    return True
  def write_file_member(self):
    file = open("members.txt", "w")
    for i in self.member_directory:
      file.write(i.name + "\n")
      file.write(str(i.id) + "\n")
      file.write(i.address + "\n")
      file.write(i.city + "\n")
      file.write(i.state + "\n")
      file.write(str(i.zip) + "\n")
      #file.write(i.display_services())
    file.close()
  
  def write_file_provider(self):
    file = open("providers.txt", "w")
    for i in self.provider_directory:
      file.write(i.name + "\n")
      file.write(str(i.id) + "\n")
      file.write(i.address + "\n")
      file.write(i.city + "\n")
      file.write(i.state + "\n")
      file.write(str(i.zip) + "\n")
      #file.write(i.display_services())
    file.close()

  def load_services(self):
    #Load services from external file into service directory - object lives in classobjects

    return True
