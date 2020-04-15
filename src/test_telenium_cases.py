from telenium.tests import TeleniumTestCase
import time


class TestSelectAddress(TeleniumTestCase):
    # import pdb;pdb.set_trace()

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application second Page-------------")

    def test_select_address(self):
        time.sleep(8)
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(5)
        # if self.cli.execute('app.root.toggle_nav_drawer()'):
            # time.sleep(5)
        self.cli.click_on('//NavigationDrawerIconButton[0]')
        time.sleep(5)
        # self.cli.wait_click('//NavigationDrawerIconButton[0]/CustomSpinner[0]')
        # time.sleep(3)
        self.cli.click_on('//NavigationDrawerIconButton[1]')


class TestSentMessage(TeleniumTestCase):

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application Thirds Page-------------")

    def test_select_sent(self):
        print("ek issue h solve krna hai----")
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
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[1]/MyTextInput[0]',"text",'BM-2cSsuH1bUWBski8bvdqnK2DivMqQCeQA1J')
        time.sleep(3)
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/MDTextField[0]','text','heyyyyyy')
        time.sleep(3)
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/MDTextField[1]','text','how are you this is body')
        time.sleep(2)
        self.cli.click_on('//MDIconButton[2]')
        time.sleep(2)

    def test_show_sent_messgae_list(self):
        time.sleep(5)       
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(5)
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
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[1]/MyTextInput[0]',"text",'BM-2cSsuH1bUWBski8bvdqnK2DivMqQCeQA1J')
        time.sleep(3)
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/MDTextField[0]','text','Second')
        time.sleep(3)
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/MDTextField[1]','text','Hey This is Second Message Body')
        time.sleep(2)
        self.cli.click_on('//MDIconButton[2]')
        # time.sleep(2)
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
        self.cli.click_on('//Carousel[0]')
        time.sleep(2)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[2]/TwoLineAvatarIconListItem[0]/BoxLayout[1]')
        time.sleep(3)
        # self.cli.click_on('//MDIconButton[1]')
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/Toolbar[0]/BoxLayout[2]/MDIconButton[0]/MDLabel[0]')
        time.sleep(5)

    def test_delete_sent_message_from_list(self):
        print("-----------Delete messgae from message list-------------.")
        time.sleep(5)
        self.cli.drag('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[2]/TwoLineAvatarIconListItem[0]/BoxLayout[1]','/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[1]/Button[0]',1)
        time.sleep(4)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[1]/Button[0]')

    def test_archive_sent_message_from_list(self):
        # Swipe-Arrchive-Sent-Message
        self.cli.drag('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[2]/TwoLineAvatarIconListItem[0]/BoxLayout[0]','/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[0]/Button[0]',1)

        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Sent[0]/BoxLayout[0]/BoxLayout[0]/ScrollView[0]/MDList[0]/Carousel[0]/RelativeLayout[1]/Button[0]')



class DraftMessage(TeleniumTestCase):

    def select_draft_message(self):
        self.cli.execute('app.root.toggle_nav_drawer()')
        time.sleep(1)
        self.cli.click_on('//NavigationDrawerIconButton[1]')
        time.sleep(1)
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Inbox[0]/ComposerButton[0]/MDFloatingActionButton[0]/MDLabel[0]')
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[0]/BoxLayout[0]/CustomSpinner[0]/ArrowImg[0]')
        time.sleep(1)
        self.cli.click_on('//MyTextInput[0]')
        time.sleep(3)
        self.cli.setattr('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[1]/MyTextInput[0]',"text",'BM-2cSsuH1bUWBski8bvdqnK2DivMqQCeQA1J')
        time.sleep(3)
        # BACK-BUTTON
        self.cli.click_on('/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/Toolbar[0]/BoxLayout[0]/MDIconButton[0]/MDLabel[0]')


# SelectAddress().test_select_address()
# cli.click_on('//NavigationDrawerIconButton[0]/CustomSpinner[@on_text="app.getCurrentAccountData(self.text)"]')
