import unittest
import class_objects

# Unit testing of member variables for the member and provider objects.
# py .\testing.py to run the unit tests


#Test each individual member variable to see if they are the accurate length
class test_member_length(unittest.TestCase):
    
    def test_name(self):
        member_null = class_objects.member("Bobby","","","","","")

        self.assertGreater(len(member_null.name),0)
        self.assertLessEqual(len(member_null.name),25)
        
    def test_id(self):
        member_null = class_objects.member("","987345123","","","","")

        self.assertEqual(len(member_null.id), 9)

    def test_address(self):
        member_null = class_objects.member("","","9451 Imaginary St","","","")
        
        self.assertGreater(len(member_null.address),0)
        self.assertLessEqual(len(member_null.address),25)
        
    def test_city(self):
        member_null = class_objects.member("","","","Portland","","")
        
        self.assertGreater(len(member_null.city),0)
        self.assertLessEqual(len(member_null.city),14)
        
    def test_state(self):
        member_null = class_objects.member("","","","","OR","")

        self.assertEqual(len(member_null.state),2)
        
    def test_zip(self):
        member_null = class_objects.member("","","","","","98772")

        self.assertEqual(len(member_null.zip),5)
        
  
#Test each provider member variable to see if they are the accurate length
class test_provider_length(unittest.TestCase):
    
    def test_name(self):
        provider_null = class_objects.provider("Lucy","","","","","")

        self.assertGreater(len(provider_null.name),0)
        self.assertLessEqual(len(provider_null.name),25)
        
    def test_id(self):
        member_null = class_objects.member("","165234796","","","","")

        self.assertEqual(len(member_null.id), 9)
        
    def test_address(self):
        provider_null = class_objects.provider("","","2941 Rand St","","","")
       
        self.assertGreater(len(provider_null.address),0)
        self.assertLessEqual(len(provider_null.address),25)
        
    def test_city(self):
        provider_null = class_objects.provider("","","","Portland","","")
        
        self.assertGreater(len(provider_null.city),0)
        self.assertLessEqual(len(provider_null.city),14)
        
    def test_state(self):
        provider_null = class_objects.provider("","","","","CA","")
       
        self.assertEqual(len(provider_null.state),2)

    def test_zip(self):
        provider_null = class_objects.provider("","","","","","98221")
       
        self.assertEqual(len(provider_null.zip),5)
        
        

if __name__ == '__main__':
    unittest.main()