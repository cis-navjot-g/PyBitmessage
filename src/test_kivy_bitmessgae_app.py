import time
from telenium.tests import TeleniumTestCase
import random
import string
import  os
import test_telenium_cases 



class TestBitMessageApp(TeleniumTestCase):
    cmd_entrypoint = [u'/home/cis/peterwork_new/PyBitmessage/src/main.py']

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application-------------")  

    
    def test_login_screen(self):
        print(self,"---------------------------")
        time.sleep(5)
        # if not os.path.isdir("/home/cis/.config/PyBitmessage"):
        print("first screen")
        self.cli.drag("/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Login[0]/ScrollView[0]/BoxLayout[0]/MDCheckbox[0]","/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Login[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[0]",2)
        time.sleep(5)
        self.cli.wait_click(u'/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Login[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[2]/AnchorLayout[0]/MDRaisedButton[0]/MDLabel[0]')
        time.sleep(5)

    def test_random_screen(self):
        # if not os.path.isdir("/home/cis/.config/PyBitmessage"):    
        self.cli.setattr(u'/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Random[0]/ScrollView[0]/BoxLayout[0]/MDTextField[0]', "text", self.generate_random_string())
        time.sleep(5)
        self.cli.wait_click(u'/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Random[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[0]/AnchorLayout[0]/MDRaisedButton[0]/MDLabel[0]')    
        time.sleep(5)

    def generate_random_string(self):
        """Generate a random string of fixed length """
        # return ''.join(random.choice(letters) for i in range(stringLength))
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(10))

  
    
if __name__ == '__main__':
    TeleniumTestCase.start_process()
    TestBitMessageApp().runTest()
    TestBitMessageApp().test_login_screen()
    TestBitMessageApp().test_random_screen()
    obj=test_telenium_cases.TestSelectAddress()
    obj.test_select_address()
    obj_1=test_telenium_cases.TestSentMessage()
    obj_1.test_select_sent()
    obj_1.test_show_sent_messgae_list()
    obj_1.test_sent_multiple_message()
    obj_1.test_serach_sent_messages()
    obj_1.test_show_sent_message_body()
    obj_1.test_delete_sent_message_body()
    obj_1.test_archive_sent_message_from_list()
   
