import time
from telenium.tests import TeleniumTestCase
import random
import string
import  os
import test_telenium_cases
from random import choice
from string import ascii_lowercase


class Bitmessage_Login_Screen(TeleniumTestCase):
    """Login Functionality Testing"""
    cmd_entrypoint = [u'/home/cis/peterwork_new/PyBitmessage/src/main.py']

    def runTest(self):
        """Test Run Method."""
        print(self,"=====================Welcome To Kivy Testing Application=====================")
    
    def test_login_screen(self):
        """Clicking on Proceed Button to Proceed to Next Screen."""
        print("=====================Test - Login Screen=====================")
        time.sleep(3)   
        self.cli.drag("/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Login[0]/ScrollView[0]/BoxLayout[0]/MDCheckbox[0]","/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Login[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[0]",2)
        time.sleep(3)
        self.cli.wait_click(u'/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Login[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[2]/AnchorLayout[0]/MDRaisedButton[0]/MDLabel[0]')
        time.sleep(3)

    def test_random_screen(self):
        """Creating New Adress For New User."""
        print("=====================Test - Create New Address=====================")
        random_label = ""
        for _ in range(10):
            random_label += choice(ascii_lowercase)                                  
            self.cli.setattr(u'/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Random[0]/ScrollView[0]/BoxLayout[0]/MDTextField[0]', "text", random_label)
            time.sleep(0.2)
        time.sleep(1)    
        self.cli.wait_click(u'/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Random[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[0]/AnchorLayout[0]/MDRaisedButton[0]/MDLabel[0]')    
        time.sleep(5)
     
if __name__ == '__main__':
    """Start Application"""
    TeleniumTestCase.start_process()
    Bitmessage_Login_Screen().runTest()
    print("==================start from first screen=====================")
    f=open("/home/cis/.config/PyBitmessage/keys.dat")
    get_file=f.read()
    find_address=get_file.find("label")
    print(find_address)
    if find_address != -1:
        select_address=test_telenium_cases.Bitmessage_Select_Address()
        select_address.test_check_already_created_address()
        select_address.test_calling_all_methods()
        sent_message=test_telenium_cases.Bitmessage_Sent_Screen_Message()
        sent_message.test_select_sent()
        sent_message.test_sent_multiple_message()
        inbox_message=test_telenium_cases.Bitmessage_Inbox_Screen_Message()
        inbox_message.test_all_inbox_method()
        sent_message.test_all_sent_method()
        # sent_message.test_archive_sent_message_from_list()
        draft_message=test_telenium_cases.TestDraftMessage()
        draft_message.test_all_draft_method()
        trash_message=test_telenium_cases.TestTrashMessage()
        trash_message.test_delete_trash_message()
        all_mails=test_telenium_cases.TestAllMailsMessage()
        all_mails.test_select_all_mails()
        all_mails.test_delete_message_from_draft()
        address_book=test_telenium_cases.TestAddressBookContact()
        address_book.test_all_address_book_method()
    else :    
        Bitmessage_Login_Screen().test_login_screen()
        Bitmessage_Login_Screen().test_random_screen()
        new_address=test_telenium_cases.Bitmessage_Create_New_Address()
        new_address.test_create_new_address()
        Bitmessage_Login_Screen().test_random_screen()
        select_address=test_telenium_cases.Bitmessage_Select_Address()
        select_address.test_calling_all_methods()
        sent_message=test_telenium_cases.Bitmessage_Sent_Screen_Message()
        sent_message.test_select_sent()
        sent_message.test_sent_multiple_message()
        inbox_message=test_telenium_cases.Bitmessage_Inbox_Screen_Message()
        inbox_message.test_all_inbox_method()
        sent_message.test_all_sent_method()
        # sent_message.test_archive_sent_message_from_list()
        draft_message=test_telenium_cases.TestDraftMessage()
        draft_message.test_all_draft_method()
        trash_message=test_telenium_cases.TestTrashMessage()
        trash_message.test_delete_trash_message()
        all_mails=test_telenium_cases.TestAllMailsMessage()
        all_mails.test_select_all_mails()
        all_mails.test_delete_message_from_draft()
        address_book=test_telenium_cases.TestAddressBookContact()
        address_book.test_all_address_book_method()