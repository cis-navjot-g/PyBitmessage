import time
from telenium.tests import TeleniumTestCase
import random
import string
import  os
import test_telenium_cases
from random import choice
from string import ascii_lowercase


class TestBitMessageApp(TeleniumTestCase):
    cmd_entrypoint = [u'/home/cis/peterwork_new/PyBitmessage/src/main.py']

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application-------------")  
    
    def test_login_screen(self):
        print(self,"---------------------------")
        time.sleep(5)   
        print("first screen")
        self.cli.drag("/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Login[0]/ScrollView[0]/BoxLayout[0]/MDCheckbox[0]","/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Login[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[0]",2)
        time.sleep(5)
        self.cli.wait_click(u'/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Login[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[2]/AnchorLayout[0]/MDRaisedButton[0]/MDLabel[0]')
        time.sleep(5)

    def test_random_screen(self):
        random_label = ""
        for _ in range(10):
            random_label += choice(ascii_lowercase)                                  
            self.cli.setattr(u'/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Random[0]/ScrollView[0]/BoxLayout[0]/MDTextField[0]', "text", random_label)
            time.sleep(0.2)
        self.cli.wait_click(u'/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Random[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[0]/AnchorLayout[0]/MDRaisedButton[0]/MDLabel[0]')    
        time.sleep(5)
     
if __name__ == '__main__':
    TeleniumTestCase.start_process()
    TestBitMessageApp().runTest()
    print("==================start from first screen=====================")
    TestBitMessageApp().test_login_screen()
    TestBitMessageApp().test_random_screen()
    obj_3=test_telenium_cases.TestCreateNewAddress()
    obj_3.test_create_new_address()
    TestBitMessageApp().test_random_screen()
    obj=test_telenium_cases.TestSelectAddress()
    obj.test_select_second_address()
    obj.test_select_address()
    obj_1=test_telenium_cases.TestSentMessage()
    obj_1.test_select_sent()
    obj_1.test_sent_multiple_message()
    obj_inbox=test_telenium_cases.TestInboxMessage()
    obj_inbox.test_select_inbox_of_second_address()
    obj_inbox.test_show_inbox_message()
    obj_inbox.test_delete_inbox_message()
    obj_1.test_show_sent_messgae_list()
    obj_1.test_serach_sent_messages()
    obj_1.test_show_sent_message_body()
    obj_1.test_delete_sent_message_body()
    obj_1.test_delete_sent_message_from_list()
    obj_1.test_archive_sent_message_from_list()
    obj_2=test_telenium_cases.TestDraftMessage()
    obj_2.test_select_draft_message()
    obj_2.test_edit_draft_messgae()
    obj_2.test_delete_draft_message()
    obj_5=test_telenium_cases.TestAddressBookContact()
    obj_5.test_save_address()
    obj_5.test_cancel_address()
    obj_5.test_send_message_to_addressbook()
    obj_5.test_delete_address_from_address_contact()
   
        