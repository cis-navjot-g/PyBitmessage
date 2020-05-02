from telenium.tests import TeleniumTestCase
import time
import random
import string
import  os
data=[]

class Bitmessage_Create_New_Address(TeleniumTestCase):
    """Generate New Address Functionality Testing"""

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application Thirteenth Page-------------")

    def test_create_new_address(self):
        """Clicking on Navigation Drawer To Open New Address"""
        print("=====================Test - Create New Address=====================")
        time.sleep(5)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(2)
        self.cli.drag("//NavigationDrawerSubheader[@text=\"All labels\"]","//NavigationDrawerIconButton[@text=\"All Mails\"]",1)
        time.sleep(3)
        self.cli.click_on('//NavigationDrawerIconButton[10]')
        time.sleep(4)
        self.cli.wait_click(u'/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Login[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[2]/AnchorLayout[0]/MDRaisedButton[0]/MDLabel[0]')

class Bitmessage_Select_Address(TeleniumTestCase):
    """Select Address Functionality Testing"""

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application second Page-------------")

    def test_check_already_created_address(self):
        """Check The Address Is Already Created Or Not"""
        print("=====================Test - Select Address From Navigation Drawer=====================")
        time.sleep(6)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(4)
        self.cli.drag("//NavigationDrawerSubheader[@text=\"All labels\"]","//NavigationDrawerIconButton[@text=\"All Mails\"]",1)
        time.sleep(3)
        self.cli.click_on('//NavigationDrawerIconButton[12]')
        time.sleep(4)

    def test_select_second_address(self):
        """Select Text From Second Address Generated"""
        print("=====================Test - Select Text From Second Address Created====================")
        global data
        time.sleep(3)
        second_address=self.cli.getattr("//CustomTwoLineAvatarIconListItem[0]","secondary_text")
        first_address=self.cli.getattr("//CustomTwoLineAvatarIconListItem[1]","secondary_text")
        data.append(second_address)
        data.append(first_address)
        return data

    def test_select_address(self):
        """Select First Address From Drawer-Box"""
        print("=====================Test - Select First Address From Drawer-Box=======================")
        time.sleep(3)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(2)
        self.cli.drag("//NavigationDrawerSubheader[@text=\"All labels\"]","//NavigationDrawerIconButton[@text=\"Address Book\"]",2)
        time.sleep(2)
        self.cli.click_on('//NavigationDrawerIconButton[0]')
        time.sleep(2)
        self.cli.click_on('//NDBadgeLabel[1]')

    def test_calling_all_methods(self):
        self.test_select_second_address()
        self.test_select_address()

class Bitmessage_Inbox_Screen_Message(TeleniumTestCase):
    """Inbox Screen Functionality Testing"""

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application For Inbox Screen-------------")
    
    def test_select_inbox_of_second_address(self):
        """Select Inbox Screen From Navigation-Drawer-Box"""
        print("=====================Test - Select Second Address From Drawer-Box=======================")
        time.sleep(2)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(3)
        self.cli.click_on('//NavigationDrawerIconButton[0]')
        time.sleep(3)
        self.cli.click_on('//NDBadgeLabel[2]')
        time.sleep(2)

    def test_show_inbox_message(self):
        """Select First Message from Inbox Screen"""
        print("=====================Test - Select First Message from Inbox Screen=====================")
        time.sleep(1)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(4)
        self.cli.click_on('//CustomTwoLineAvatarIconListItem[0]')
        time.sleep(3)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/Toolbar[0]/BoxLayout[0]/MDIconButton[0]/MDLabel[0]')
        time.sleep(3)

    def test_delete_inbox_message(self):
        """Deleting Message From Inbox Screen"""
        print("=====================Test - Deleting Message From Inbox Screen=====================")
        time.sleep(4)
        self.cli.drag('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Inbox[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[2]/CustomTwoLineAvatarIconListItem[0]/BoxLayout[1]','/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Inbox[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[1]/Button[0]',1)
        time.sleep(2)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Inbox[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[1]/Button[0]')
        time.sleep(4)

    def test_all_inbox_method(self):
        """Calling All The Methods Inbox Class"""
        self.test_select_inbox_of_second_address()
        self.test_show_inbox_message()
        self.test_delete_inbox_message()

class Bitmessage_Sent_Screen_Message(TeleniumTestCase):
    """Sent Screen Functionality Testing"""

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application Thirds Page-------------")

    def test_select_sent(self):
        """Sending Message From Inbox Screen
        opens a pop-up(screen)which send message from sender to reciever"""
        print("=====================Test - Sending Message From Inbox Screen=====================")
        time.sleep(2)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(1)
        self.cli.click_on('//NavigationDrawerIconButton[1]')
        time.sleep(1)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Inbox[0]/ComposerButton[0]/MDFloatingActionButton[0]/MDLabel[0]')
        time.sleep(3)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[0]/MDTextField[0]')
        time.sleep(3)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[1]/MyTextInput[0]')
        time.sleep(3)
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[1]/MyTextInput[0]',"text","second add")
        time.sleep(3)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/MDTextField[0]')
        time.sleep(4)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/MDTextField[1]')
        time.sleep(4)
        # time.sleep(3)
        self.cli.click_on('//MDIconButton[2]')
        time.sleep(3)
        self.cli.click_on('//MDRaisedButton[0]')
        time.sleep(5)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[0]/BoxLayout[0]/CustomSpinner[0]/ArrowImg[0]')
        time.sleep(2)
        self.cli.click_on('//MyTextInput[0]')
        time.sleep(3)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/MDTextField[0]')
        time.sleep(2)
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/MDTextField[0]','text','heyyyyyy')
        time.sleep(3)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/MDTextField[1]')
        time.sleep(4)
        random_label=""
        for char in "how are you this is message body":
            random_label += char
            self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/MDTextField[1]','text',random_label)
            time.sleep(0.2)
        time.sleep(3)
        self.cli.click_on('//MDIconButton[2]')
        time.sleep(3)
        self.cli.click_on('//MDRaisedButton[0]')
        time.sleep(6)
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[1]/MyTextInput[0]',"text",data[0])
        time.sleep(3)
        self.cli.click_on('//MDIconButton[2]')
        time.sleep(3)
        self.cli.click_on('//MDRaisedButton[0]')
        time.sleep(3)       
   
    def test_sent_multiple_message(self):
        """Sending Second Message From Inbox Screen
        for testing the search and delete functionality for two messages on the screen"""
        print("=====================Test - Sending Message From Inbox Screen=====================")
        time.sleep(3)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(5)
        self.cli.click_on('//NavigationDrawerIconButton[1]')
        time.sleep(3)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Inbox[0]/ComposerButton[0]/MDFloatingActionButton[0]/MDLabel[0]')
        time.sleep(3)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[0]/BoxLayout[0]/CustomSpinner[0]/ArrowImg[0]')
        time.sleep(2)
        self.cli.click_on('//MyTextInput[0]')
        time.sleep(3)
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[1]/MyTextInput[0]',"text",data[0])
        time.sleep(3)
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/MDTextField[0]','text','Second')
        time.sleep(3)
        random_label=""
        for char in "Hey This Is Second Message Body":
            random_label += char
            self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/MDTextField[1]','text',random_label)
            time.sleep(0.2)
        time.sleep(2)
        self.cli.click_on('//MDIconButton[2]')
        time.sleep(5)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(3)
        self.cli.click_on('//NavigationDrawerIconButton[2]')
        time.sleep(3)
        
    def test_show_sent_messgae_list(self):
        """Displaying All the Messages on Sent Screen"""
        print("=====================Test - Show Sent Screen Message=====================")
        time.sleep(5)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(5)
        self.cli.click_on('//NavigationDrawerIconButton[0]')
        time.sleep(5)
        self.cli.click_on('//NDBadgeLabel[1]')
        time.sleep(6)
        self.cli.click_on('//NavigationDrawerIconButton[2]')
        time.sleep(2)

    def test_search_sent_messages(self):
        """Search Message From a Word Of Subject/Body on Sent Screen"""
        print("=====================Test - Search Message On The Sent Screen=====================")
        time.sleep(1)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/SearchBar[0]/MDTextField[0]')
        time.sleep(2)
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/SearchBar[0]/MDTextField[0]','text','how')
        time.sleep(2)
        self.cli.send_keycode('Enter')
        time.sleep(5)
        self.cli.click_on('//MDIconButton[0]')
        time.sleep(3)

    def test_show_sent_message_body(self):
        """Show A Message From Message Body"""
        print("=====================Test - Show A Message From Message Body=====================")
        time.sleep(5)
        self.cli.click_on('//Carousel[0]')
        time.sleep(5)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/Toolbar[0]/BoxLayout[0]/MDIconButton[0]/MDLabel[0]')
        time.sleep(2)

    def test_delete_sent_message_body(self):
        """Delete A Message From Message Body"""
        print("=====================Test - Delete A Message From Message Body=====================")
        time.sleep(2)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[2]/CustomTwoLineAvatarIconListItem[0]/BoxLayout[2]')
        time.sleep(3)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/Toolbar[0]/BoxLayout[2]/MDIconButton[0]/MDLabel[0]')
        time.sleep(5)

    def test_delete_sent_message_from_list(self):
        """Delete A Message From List Of Messages Of Sent Screen"""
        print("=====================Test - Delete A Message From List Of Messages=====================")
        time.sleep(5)
        self.cli.drag('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[2]/CustomTwoLineAvatarIconListItem[0]/BoxLayout[1]','/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[1]/Button[0]',1)
        time.sleep(4)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[1]/Button[0]')

    def test_archive_sent_message_from_list(self):
        """Archive A Message From List Of Messages Of Sent Screen"""
        print("=====================Test - Archive A Message From List Of Messages=====================")
        # Swipe-Arrchive-Sent-Message
        time.sleep(4)
        self.cli.drag('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[2]/CustomTwoLineAvatarIconListItem[0]/BoxLayout[0]','/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[0]/Button[0]',1)
        time.sleep(2)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[1]/Button[0]')
        time.sleep(4)

    def test_all_sent_method(self):
        """Calling All The Methods Sent Class"""
        self.test_show_sent_messgae_list()
        self.test_search_sent_messages()
        self.test_show_sent_message_body()
        self.test_delete_sent_message_body()
        self.test_delete_sent_message_from_list()

class Bitmessage_Draft_Screen_Message(TeleniumTestCase):
    """Draft Screen Functionality Testing"""

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application Fourth Page-------------")

    def test_select_draft_message(self):
        """Select A Draft Screen From Navigaion-Drawer-Box Then
           Send a drafted message """
        print("=====================Test - Select A Draft Screen From Navigaion-Drawer-Box=====================")
        # OPEN NAVIGATION-DRAWER
        time.sleep(4)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(2)
        # OPEN INBOX SCREEN
        self.cli.click_on('//NavigationDrawerIconButton[1]')
        time.sleep(2)
        # CLICK ON PLUS ICON BUTTON
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Inbox[0]/ComposerButton[0]/MDFloatingActionButton[0]/MDLabel[0]')
        time.sleep(3)
        # SELECT - TO ADDRESS
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[0]/BoxLayout[0]/CustomSpinner[0]/ArrowImg[0]')
        time.sleep(2)
        self.cli.click_on('//MyTextInput[0]')
        time.sleep(3)
        # ADD FROM MESSAGE
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[1]/MyTextInput[0]',"text",'BM-2cSsuH1bUWBski8bvdqnK2DivMqQCeQA1J')
        time.sleep(3)
        # CLICK BACK-BUTTON
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/Toolbar[0]/BoxLayout[0]/MDIconButton[0]/MDLabel[0]')
        time.sleep(5)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Inbox[0]/ComposerButton[0]/MDFloatingActionButton[0]/MDLabel[0]')
        time.sleep(3)
        # SELECT - TO ADDRESS
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[0]/BoxLayout[0]/CustomSpinner[0]/ArrowImg[0]')
        time.sleep(1)
        self.cli.click_on('//MyTextInput[0]')
        time.sleep(3)
        # ADD FROM MESSAGE
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[1]/MyTextInput[0]',"text",'BM-2cSsuH1bUWBski8bvdqnK2DivMqQCeQA1J')
        time.sleep(4)
        random_label=""
        for char in "Another Draft message":
            random_label += char
            self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/MDTextField[0]','text',random_label)
            time.sleep(0.2)
        # CLICK BACK-BUTTON
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/Toolbar[0]/BoxLayout[0]/MDIconButton[0]/MDLabel[0]')
        time.sleep(4)
   
    def test_edit_draft_messgae(self):
        """Select A Message From List of Messages Then
            make changes and send it."""
        print("=====================Test - Edit A Message From Draft Screen=====================")
        # OPEN NAVIGATION-DRAWER
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(4)
        # OPEN DRAFT SCREEN
        self.cli.click_on('//NavigationDrawerIconButton[3]')
        time.sleep(4)
        # SHOW DRAFT MESSAGE AND SELECT FIRST MESSAGE
        self.cli.click_on('//Carousel[0]')
        time.sleep(3)
        # CLICK EDIT BUTTON
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/Toolbar[0]/BoxLayout[2]/MDIconButton[0]/MDLabel[0]')
        time.sleep(5)
        random_label=""
        for char in "Hey,This is draft Message Body":
            random_label += char
            self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/MDTextField[1]','text',random_label)
            time.sleep(0.2)
        time.sleep(3)
        self.cli.click_on('//MDIconButton[2]')
        time.sleep(5)
        
    def test_delete_draft_message(self):
        """Delete A Message From List of Messages"""
        print("=====================Test - Delete A Message From List of Messages=====================")
        time.sleep(5)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(4)
        self.cli.click_on('//NavigationDrawerIconButton[3]')
        time.sleep(5)
        self.cli.click_on('//Carousel[0]')
        time.sleep(5)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/Toolbar[0]/BoxLayout[2]/MDIconButton[1]/MDLabel[0]')
        time.sleep(2)
    
    def test_all_draft_method(self):
        """Calling All The Methods Draft Class"""
        self.test_select_draft_message()
        self.test_edit_draft_messgae()
        self.test_delete_draft_message()

class Bitmessage_AllMail_Screen_Message(TeleniumTestCase):
    """AllMail Screen Functionality Testing"""

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application Sixth Page-------------")

    def test_select_all_mails(self):
        """Show All Messages on Mail Screen/Window"""
        print("=====================Test -Show Messages Of Mail Screen=====================")
        time.sleep(5)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(4)
        self.cli.click_on('//NavigationDrawerIconButton[5]')
        time.sleep(4)
      
    def test_delete_message_from_draft(self):
        """Delete Message From Message body of Mail Screen/Window"""
        print("=====================Test -Delete Messages Of Mail Screen=====================")
        time.sleep(4)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Allmails[0]/Allmails[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]')
        time.sleep(5)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/Toolbar[0]/BoxLayout[2]/MDIconButton[0]/MDLabel[0]')
        time.sleep(3)

class Bitmessage_Trash_Screen_Message(TeleniumTestCase):
    """Trash Screen Functionality Testing"""

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application Fifth Page-------------")

    def test_delete_trash_message(self):
        """Delete Message From List of Message Permanently Of Trash Screen/Window"""
        print("=====================Test -Delete Messages Of Trash Screen=====================")
        time.sleep(6)
        # self.cli.click_on('//NavigationDrawerIconButton[4]')
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(4)
        self.cli.click_on('//NavigationDrawerIconButton[4]')
        time.sleep(4)
        self.cli.drag('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Trash[0]/Trash[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[1]/CustomTwoLineAvatarIconListItem[0]/BoxLayout[1]/AvatarSampleWidget[0]','/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Trash[0]/Trash[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[1]/CustomTwoLineAvatarIconListItem[0]/BoxLayout[2]',1)
        time.sleep(4)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Trash[0]/Trash[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[1]/Button[0]')
        time.sleep(2)
        self.cli.click_on('//MDRaisedButton[0]')
        time.sleep(4)

class Bitmessage_AddressBook_Screen_Message(TeleniumTestCase):
    """AddressBook Screen Functionality Testing"""

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application Seven Page-------------")

    def test_save_address(self):
        """Save Address On Address Book Screen/Window"""
        print("=====================Test -Save Address In Address Book=====================")
        time.sleep(6)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(4)
        self.cli.drag("//NavigationDrawerSubheader[@text=\"All labels\"]","//NavigationDrawerIconButton[@text=\"All Mails\"]",1)
        time.sleep(3)
        self.cli.click_on('//NavigationDrawerIconButton[6]')
        time.sleep(4)
        self.cli.execute('app.addingtoaddressbook()')
        time.sleep(3)
        self.cli.click_on('/GrashofPopup/GridLayout[0]/BoxLayout[0]/BoxLayout[0]/BoxLayout[0]/MDTextField[0]')
        time.sleep(4)
        self.cli.click_on('/GrashofPopup/GridLayout[0]/BoxLayout[0]/BoxLayout[0]/BoxLayout[0]/MDTextField[1]')
        time.sleep(4)
        self.cli.click_on('//MDRaisedButton[0]')
        time.sleep(4)
        self.cli.click_on('/GrashofPopup/GridLayout[0]/BoxLayout[0]/BoxLayout[0]/BoxLayout[0]/MDTextField[0]')
        time.sleep(3)
        self.cli.setattr('/GrashofPopup/GridLayout[0]/BoxLayout[0]/BoxLayout[0]/BoxLayout[0]/MDTextField[0]','text','peter')
        time.sleep(3)
        self.cli.click_on('//MDRaisedButton[0]')
        time.sleep(4)
        self.cli.click_on('/GrashofPopup/GridLayout[0]/BoxLayout[0]/BoxLayout[0]/BoxLayout[0]/MDTextField[1]')
        time.sleep(3)
        self.cli.setattr('/GrashofPopup/GridLayout[0]/BoxLayout[0]/BoxLayout[0]/BoxLayout[0]/MDTextField[1]','text','sectorAppartment')
        time.sleep(3)
        self.cli.click_on('//MDRaisedButton[0]')
        time.sleep(5)
        self.cli.click_on('/GrashofPopup/GridLayout[0]/BoxLayout[0]/BoxLayout[0]/BoxLayout[0]/MDTextField[1]')
        time.sleep(3)
        self.cli.setattr('/GrashofPopup/GridLayout[0]/BoxLayout[0]/BoxLayout[0]/BoxLayout[0]/MDTextField[1]','text',data[0])
        time.sleep(3)
        self.cli.setattr('/GrashofPopup/GridLayout[0]/BoxLayout[0]/BoxLayout[0]/BoxLayout[0]/MDTextField[1]','text','')
        time.sleep(3)
        self.cli.click_on('//MDRaisedButton[0]')
        time.sleep(4)
        self.cli.setattr('/GrashofPopup/GridLayout[0]/BoxLayout[0]/BoxLayout[0]/BoxLayout[0]/MDTextField[1]','text','BM-2cX78L9CZpb6GGC3rRVizYiUBwHELMLybd')
        time.sleep(3)
        self.cli.click_on('//MDRaisedButton[0]')
        time.sleep(4)

    def test_cancel_address(self):
        """Cancel Address"""
        print("=====================Test -Cancel Address=====================")
        time.sleep(3)
        self.cli.execute('app.addingtoaddressbook()')
        time.sleep(3)
        self.cli.setattr('/GrashofPopup/GridLayout[0]/BoxLayout[0]/BoxLayout[0]/BoxLayout[0]/MDTextField[0]','text','prachi')
        time.sleep(3)
        self.cli.setattr('/GrashofPopup/GridLayout[0]/BoxLayout[0]/BoxLayout[0]/BoxLayout[0]/MDTextField[1]','text',data[0])
        time.sleep(3)
        self.cli.click_on('/GrashofPopup/GridLayout[0]/BoxLayout[0]/BoxLayout[0]/BoxLayout[1]/MDRaisedButton[1]')

    def test_send_message_to_addressbook(self):
        """Directly Send Message To The User"""
        print("=====================Test -Directly Send Message To The User=====================")
        time.sleep(4)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/AddressBook[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]')
        time.sleep(3)
        self.cli.click_on('/AddbookDetailPopup/GridLayout[0]/BoxLayout[0]/BoxLayout[0]/BoxLayout[1]/MDRaisedButton[0]/MDLabel[0]')
        time.sleep(3)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[0]/BoxLayout[0]/CustomSpinner[0]/ArrowImg[0]')
        time.sleep(2)
        self.cli.click_on('//MyTextInput[0]')
        time.sleep(3)
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/MDTextField[0]','text','Second')
        time.sleep(3)
        random_label=""
        for char in "Hey This is Message From Address Book":
            random_label += char
            self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/MDTextField[1]','text',random_label)
            time.sleep(0.2)
        self.cli.click_on('//MDIconButton[2]')
        time.sleep(2)

    def test_delete_address_from_address_contact(self):
        """Delete Address From Address Book"""
        print("=====================Test -Delete Address From Address Book=====================")
        time.sleep(3)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(3)
        self.cli.click_on('//NavigationDrawerIconButton[6]')
        time.sleep(3)
        self.cli.drag('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/AddressBook[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[1]/CustomTwoLineAvatarIconListItem[0]/BoxLayout[1]/AvatarSampleWidget[0]','/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/AddressBook[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[1]/CustomTwoLineAvatarIconListItem[0]/BoxLayout[2]',1)
        time.sleep(2)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/AddressBook[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[1]/Button[0]')

    def test_all_address_book_method(self):
        self.test_save_address()
        self.test_cancel_address()
        self.test_send_message_to_addressbook()
        self.test_delete_address_from_address_contact()

class Bitmessage_Setting_Screen(TeleniumTestCase):
    """Setting Screen Functionality Testing"""

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application Eight Page-------------")

    def test_setting(self):
        """Show Setting Screen"""
        print("=====================Test -Show Setting Screen=====================")
        time.sleep(4)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(3)
        self.cli.click_on('//NavigationDrawerIconButton[7]')
        time.sleep(2)

class Bitmessage_MyAddress_Screen_Message(TeleniumTestCase):
    """MyAddress Screen Functionality Testing"""

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application Ninth Page-------------")

    def test_select_myaddress_list(self):
        """Select Address From List of Address"""
        print("=====================Test -Select Address From List of Address=====================")
        time.sleep(4)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(3)
        self.cli.click_on('//NavigationDrawerIconButton[12]')
        time.sleep(4)

    def test_send_message_from(self):
        """Send Message From Send Message From Button"""
        print("=====================Test -Send Message From Send Message From Button=====================")
        time.sleep(4)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/MyAddress[0]/BoxLayout[0]/FloatLayout[0]/MDScrollViewRefreshLayout[0]/MDList[0]/CustomTwoLineAvatarIconListItem[0]/BoxLayout[0]/MDLabel[1]')
        time.sleep(4)
        self.cli.click_on('/MyaddDetailPopup/GridLayout[0]/BoxLayout[0]/BoxLayout[0]/BoxLayout[1]/MDRaisedButton[0]/MDLabel[0]')
        time.sleep(3)
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[1]/MyTextInput[0]',"text",data[1])
        time.sleep(3)
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/MDTextField[0]','text','Hey')
        time.sleep(3)
        random_label=""
        for char in "Hey,i am sending message directly from MyAddress book":
            random_label += char
            self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/MDTextField[1]','text',random_label)
            time.sleep(0.2)
        time.sleep(2)
        self.cli.click_on('//MDIconButton[2]')
        time.sleep(2)

class Bitmessage_SubscriptionPayment_Screen(TeleniumTestCase):
    """SubscriptionPayment Screen Functionality Testing"""

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application Tenth Page-------------")

    def test_select_subscripton(self):
        """Select Subscripton From List of Subscriptons"""
        print("=====================Test -Select Subscripton From List of Subscriptons=====================")
        time.sleep(4)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(3)
        self.cli.click_on('//NavigationDrawerIconButton[8]')
        time.sleep(3)
        self.cli.drag('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Payment[0]/ScrollView[0]/BoxLayout[0]','/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Payment[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[0]',1)
        time.sleep(2)
        self.cli.drag('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Payment[0]/ScrollView[0]/BoxLayout[0]','/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Payment[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[2]',1)
        time.sleep(2)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Payment[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[0]/MDRaisedButton[0]/MDLabel[0]')
        time.sleep(2)

class Bitmessage_Credits_Screen(TeleniumTestCase):
    """Credits Screen Functionality Testing"""

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application Eleventh Page-------------")

    def test_check_credits(self):
        """Show Added Credits"""
        print("=====================Test -Select Credits From List of Credits=====================")
        time.sleep(4)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(3)
        self.cli.click_on('//NavigationDrawerIconButton[9]')
        time.sleep(2)

class Bitmessage_NetwrokStatus_Screen(TeleniumTestCase):
    """NetwrokStatus Screen Functionality Testing"""

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application Twelth Page-------------")

    def test_total_selection(self):
        """Show NetwrokStatus"""
        print("=====================Test -Show NetwrokStatus=====================")
        time.sleep(4)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(3)
        self.cli.click_on('//NavigationDrawerIconButton[11]')
        time.sleep(4)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/NetworkStat[0]/MDTabbedPanel[0]/ScrollView[0]/MDTabBar[0]/MDTabHeader[1]/MDLabel[0]')
        time.sleep(4)