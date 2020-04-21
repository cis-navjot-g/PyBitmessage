from telenium.tests import TeleniumTestCase
import time
import random
import string
import  os
data=[]

class TestCreateNewAddress(TeleniumTestCase):

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application Thirteenth Page-------------")

    def test_create_new_address(self):
        time.sleep(5)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(4)
        self.cli.drag("//NavigationDrawerSubheader[@text=\"All labels\"]","//NavigationDrawerIconButton[@text=\"All Mails\"]",1)
        time.sleep(3)
        self.cli.click_on('//NavigationDrawerIconButton[10]')
        time.sleep(4)
        self.cli.wait_click(u'/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Login[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[2]/AnchorLayout[0]/MDRaisedButton[0]/MDLabel[0]')

class TestSelectAddress(TeleniumTestCase):

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application second Page-------------")

    def test_select_second_address(self):
        global data 
        time.sleep(5)
        second_address=self.cli.getattr("//CustomTwoLineAvatarIconListItem[0]","secondary_text")
        data.append(second_address)
        return data[0]

    def test_select_address(self):
        time.sleep(8)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(3)
        self.cli.drag("//NavigationDrawerSubheader[@text=\"All labels\"]","//NavigationDrawerIconButton[@text=\"Address Book\"]",2)
        time.sleep(5)
        self.cli.click_on('//NavigationDrawerIconButton[0]')
        time.sleep(5)
        self.cli.click_on('//NavigationDrawerIconButton[1]')
        time.sleep(5)

class TestInboxMessage(TestSelectAddress):

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application For Inbox Screen-------------")
    
    def test_select_inbox_of_second_address(self):
        time.sleep(2)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(5)
        self.cli.click_on('//NavigationDrawerIconButton[0]')
        time.sleep(5)
        self.cli.click_on('//NDBadgeLabel[2]')
        time.sleep(2)

    def test_show_inbox_message(self):
        time.sleep(1)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(4)
        self.cli.click_on('//CustomTwoLineAvatarIconListItem[0]')
        time.sleep(3)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/Toolbar[0]/BoxLayout[0]/MDIconButton[0]/MDLabel[0]')
        time.sleep(3)

class TestSentMessage(TestSelectAddress):

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application Thirds Page-------------")

    def test_select_sent(self):
        print("ek issue h solve krna hai----")
        time.sleep(5)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(5)
        self.cli.click_on('//NavigationDrawerIconButton[1]')
        time.sleep(3)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Inbox[0]/ComposerButton[0]/MDFloatingActionButton[0]/MDLabel[0]')
        time.sleep(4)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[0]/BoxLayout[0]/CustomSpinner[0]/ArrowImg[0]')
        time.sleep(5)
        self.cli.click_on('//MyTextInput[0]')
        time.sleep(3)
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[1]/MyTextInput[0]',"text",data[0])
        time.sleep(3)
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/MDTextField[0]','text','heyyyyyy')
        time.sleep(3)
        random_label=""
        for char in "how are you this is message body":
            random_label += char
            self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/MDTextField[1]','text',random_label)
            time.sleep(0.2)
        time.sleep(2)
        self.cli.click_on('//MDIconButton[2]')
        time.sleep(2)

    def test_show_sent_messgae_list(self):
        time.sleep(5)       
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(5)
        self.cli.click_on('//NavigationDrawerIconButton[0]')
        time.sleep(5)
        self.cli.click_on('//NDBadgeLabel[1]')
        time.sleep(6)
        self.cli.click_on('//NavigationDrawerIconButton[2]')
        time.sleep(2)

    def test_sent_multiple_message(self):
        print("---------ek issue h solve krna hai----")
        time.sleep(3)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(5)
        self.cli.click_on('//NavigationDrawerIconButton[1]')
        time.sleep(3)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Inbox[0]/ComposerButton[0]/MDFloatingActionButton[0]/MDLabel[0]')
        time.sleep(4)
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
        time.sleep(5)
        self.cli.click_on('//NavigationDrawerIconButton[2]')
        time.sleep(2)    
        
    def test_serach_sent_messages(self):
        print("-------serach message---------")
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
        print("-------------check message body------------")
        time.sleep(5)
        self.cli.click_on('//Carousel[0]')
        time.sleep(5)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/Toolbar[0]/BoxLayout[0]/MDIconButton[0]/MDLabel[0]')
        time.sleep(2)

    def test_delete_sent_message_body(self):
        print("------------Delete messgae from message body option-----------------.")
        time.sleep(2)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[2]/CustomTwoLineAvatarIconListItem[0]/BoxLayout[2]')
        time.sleep(3)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/Toolbar[0]/BoxLayout[2]/MDIconButton[0]/MDLabel[0]')
        time.sleep(5)

    def test_delete_sent_message_from_list(self):
        print("-----------Delete messgae from message list-------------.")
        time.sleep(5)
        self.cli.drag('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[2]/CustomTwoLineAvatarIconListItem[0]/BoxLayout[1]','/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[1]/Button[0]',1)
        time.sleep(4)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[1]/Button[0]')

    def test_archive_sent_message_from_list(self):
        print("-----------Archive Message From Message List-----------")
        # Swipe-Arrchive-Sent-Message
        time.sleep(7)
        self.cli.drag('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[2]/CustomTwoLineAvatarIconListItem[0]/BoxLayout[0]','/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[0]/Button[0]',1)
        time.sleep(2)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[1]/Button[0]')
        time.sleep(4)

class TestDraftMessage(TeleniumTestCase):

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application Fourth Page-------------")

    def test_select_draft_message(self):
        print("----------Show Draft Message--------------------")
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
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[1]/MyTextInput[0]',"text",data[0])
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
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[1]/MyTextInput[0]',"text",data[0])
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
        print("---------------Edit Draft Message----------------") 
        # OPEN NAVIGATION-DRAWER
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(4)
        # OPEN DRAFT SCREEN
        self.cli.click_on('//NavigationDrawerIconButton[3]')
        time.sleep(7)
        # SHOW DRAFT MESSAGE AND SELECT FIRST MESSAGE
        self.cli.click_on('//Carousel[0]')
        time.sleep(3)
        # CLICK EDIT BUTTON
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/Toolbar[0]/BoxLayout[2]/MDIconButton[0]/MDLabel[0]')
        time.sleep(5)
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/MDTextField[0]','text','draft message')
        time.sleep(4)
        random_label=""
        for char in "Hey,This is draft Message Body":
            random_label += char
            self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/MDTextField[1]','text',random_label)
            time.sleep(0.2)
        time.sleep(3)
        self.cli.click_on('//MDIconButton[2]')
        time.sleep(5)
        
    def test_delete_draft_message(self):
        print("-------------Delete Draft Message-----------------")
        time.sleep(5)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(4)
        self.cli.click_on('//NavigationDrawerIconButton[3]')
        time.sleep(5)
        self.cli.click_on('//Carousel[0]')
        time.sleep(5)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/Toolbar[0]/BoxLayout[2]/MDIconButton[1]/MDLabel[0]')
        time.sleep(2)
