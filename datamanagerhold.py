#Sienna Day
#Contains holder functionality used by menus file

class data_manager:
  def __init__(self):
    self.member_directory = []
    self.provider_directory = []
    self.service_directory = []
  def add_provider(self, name, id, address, city, state, zip):
    return True
  def remove_provider(self, provider_id):
    return True
  def edit_provider(self, id, name, address, city, state, zip):
    return True
  def add_member(self, name, id, address, city, state, zip):
    return True
  def remove_member(self, member_id):
    return True
  def edit_member(self, id, name, address, city, state, zip):
    return True
  def services_recieved(self, member_id):
    return True
  def services_provided(self, provider_id):
    return True
  def service_fees(self):
    return True
  def member_check(self, member_id):
    #if member is in the list
    return True
    #if member is not in the list
    #return False
  def provider_check(self, provider_id):
    #if provider is in the list
    return True
    #if provider is not in the list
    #return False
  def import_members(self):
    return True
  def import_providers(self):
    return True
  def print_member(self):
    return True
  def print_provider(self):
    return True
  def load_services(self):
    #Load services from external file into service directory - object lives in classobjects
    return True