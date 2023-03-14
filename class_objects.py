# Cameron Farhan
# CS 314
# ChocAn Project
# This file contains the member, member service, provider, and provider service
# classes used.

#Used for members
class service:
    def __init__(self, date, provider, service):
        self.date = date
        self.provider = provider
        self.service = service
    def display(self):
        print("Date: ", self.date, "\n", "Provider: ", self.provider, "\n", "Service: ", self.service, "\n\n\n", sep="")

#Used for providers        
class provider_service:
        def __init__(self, service_date, date_time, member_name, member_id, service_code, fee):
            self.service_date = service_date
            self.date_time = date_time
            self.member_name = member_name
            self.member_id = member_id
            self.service_code = service_code
            self.fee = fee
        def display(self):
            print("Service Date: ", self.service_date, "\n", "Date/Time: ", self.date_time, "\n"
                  "Member name: ", self.member_name, "\n", "Service code: ", self.service_code, "\n", "Fee: ", self.fee, "\n\n\n")


class member:
    def __init__(self, name, id, address, city, state, zip):
        self.name = name
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.services = []
    def change_name(self, name):
        self.name = name
    def change_id(self, id):
        self.id = id
    def change_address(self, address):
        self.address = address
    def change_city(self, city):
        self.city = city
    def change_state(self, state):
        self.state = state
    def change_zip(self, zip):
        self.zip = zip
    def add_service(self, service):
        self.services.append(service)
    def display(self):
        print("Name: ", self.name, "\n", "Member ID: ", self.id,"\n", "Address: ", self.address, "\n", 
              "State: ", self.state, "\n", "Zip: ", self.zip, "\n\n\n", sep="")
    def display_services(self):
        for service in self.services:
            service.display()
        
class provider(member):
    def __init__(self, name, id, address, city, state, zip):
        self.name = name
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.services = []
        self.num_consultations = 0
        self.week_fee = 0
    def change_name(self, name):
        self.name = name
    def change_id(self, id):
        self.id = id
    def change_address(self, address):
        self.address = address
    def change_city(self, city):
        self.city = city
    def change_state(self, state):
        self.state = state
    def change_zip(self, zip):
        self.zip = zip
    def add_service(self, service):
        self.services.append(service)
        self.num_consultations += 1
        self.week_fee += service.fee
    def display(self):
        print("Name: ", self.name, "\n", "Member ID: ", self.id,"\n", "Address: ", self.address, "\n", "State: ", self.state, "\n", "Zip: ", self.zip, "\n\n\n", sep="")
    def display_services(self):
        for service in self.services:
            service.display()
 
 
 #Below is code to test the member class. It displays the member's info, and also adds a service to the list and displays it.
'''      
temp = member("Bob Jones", 6922, "4733 NW Po St", "Portland", "OR", "98221")
temp.display()

new = service("05/07/2023", "Ashley K", "Physical Appointment")

temp.add_service(new)
temp.display_services()
'''
