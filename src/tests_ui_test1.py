import time
from telenium.tests import TeleniumTestCase
import random
import string


class TestBitMessageApp(TeleniumTestCase):
    cmd_entrypoint = [u'/home/cis/peterwork_new/PyBitmessage/src/main.py']

    def runTest(self):
        print(self,"-------------Welcome To Kivy Testing Application-------------")  
    
    def test_press_button(self):
        print(self,"---------------------------")
        time.sleep(5)
        self.cli.drag("/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Login[0]/ScrollView[0]/BoxLayout[0]/MDCheckbox[0]","/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Login[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[0]",2)
        time.sleep(5)
        self.cli.wait_click(u'/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Login[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[2]/AnchorLayout[0]/MDRaisedButton[0]/MDLabel[0]')
        time.sleep(5)
        self.cli.setattr(u'/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Random[0]/ScrollView[0]/BoxLayout[0]/MDTextField[0]', "text", self.generate_random_string())
        time.sleep(5)

    def test_next_button(self):    
        self.cli.wait_click(u'/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Random[0]/ScrollView[0]/BoxLayout[0]/BoxLayout[0]/AnchorLayout[0]/MDRaisedButton[0]/MDLabel[0]')    
        time.sleep(5)

    def generate_random_string(self):
        """Generate a random string of fixed length """
        # return ''.join(random.choice(letters) for i in range(stringLength))
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(10))
	
    def test_create_screen(self):

        # TYPE-OR-SELECT-SENDER-ADDRESS
       self.cli.wait_click(u'/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[1]/ScrollView[0]/BoxLayout[0]/BoxLayout[4]/MDTextField[1]')
       # SELECT
       self.cli.wait_click(u'/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[1]/ScrollView[0]/BoxLayout[0]/BoxLayout[4]/BoxLayout[0]/CustomSpinner[0]')
       #TYPE-OR-SCAN-OR-SELECT-CODE-FOR-RECEIPINT-ADDRESS
       self.cli.wait_click(u'/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[1]/ScrollView[0]/BoxLayout[0]/BoxLayout[3]/MyTextInput[1]')
       # 
       self.cli.wait_click(u'/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[1]/ScrollView[0]/BoxLayout[0]/BoxLayout[3]/RV[0]')
       # SELECT
       self.cli.wait_click(u'/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[1]/ScrollView[0]/BoxLayout[0]/MDTextField[2]')
       # BODY
       self.cli.wait_click(u'/NavigationLayout/BoxLayout[1]/FloatLayout[0]/BoxLayout[0]/ScreenManager[0]/Create[0]/DropDownWidget[1]/ScrollView[0]/BoxLayout[0]/MDTextField[1]')
	
        

    
if __name__ == '__main__':
    TeleniumTestCase.start_process()
    TestBitMessageApp().runTest()
    TestBitMessageApp().test_press_button()
    TestBitMessageApp().test_next_button()


