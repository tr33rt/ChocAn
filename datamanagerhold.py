#Sienna Day
#Contains holder functionality used by menus file

from class_objects import *

  
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
    count = 0
    for i in self.member_directory:
      if(self.i.id == provider_id):
        self.i.remove(count)
        return True
      else:
        count += 1
    return False

  def edit_provider(self, id, name, address, city, state, zip):

    for i in self.member_directory:
      if(self.provider_directory.id == id):
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
    count = 0
    for i in self.member_directory:
      if(self.i.id == member_id):
        self.i.remove(count)
        return True
      else:
        count += 1
    return False
  def edit_member(self, id, name, address, city, state, zip, index):

    for i in self.member_directory:
      if(self.member_directory.id == id):
        i.change_name(name)
        i.change_address(address)
        i.change_city(city)
        i.change_state(state)
        i.change_zip(zip)

  def services_received(self, member_id):
    return True
  def services_provided(self, provider_id):
    return True
  def service_fees(self):
    return True
  def member_check(self, member_id):
    #if member is in the list
    for i in self.member_directory:
      if(self.i.id == member_id):
        return True
    #if member is not in the list
    return False
    #return False
  def provider_check(self, provider_id):
    #if provider is in the list
    for i in self.member_directory:
      if(self.i.id == provider_id):
        return True
    #if provider is not in the list
    return False
  def import_members(self):
    return True
  def import_providers(self):
    return True
  def print_member(self):
    for i in self.member_directory:
      i.display()
    return True
  def print_provider(self):
    for i in self.provider_directory:
      i.display()
    return True
  def load_services(self):
    #Load services from external file into service directory - object lives in classobjects
    return True
