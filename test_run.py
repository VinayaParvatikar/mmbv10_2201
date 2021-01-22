import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import string
import random
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import conftest


@pytest.fixture(scope="class")
def setup(request):
    """Setup fixture to set the chromedriver and electron path, launch the application and
    sign in with username and password. Teardown to delete the cretaed project and close the application"""
    chromedriver_path = "C:\\Users\\vp094039\\Downloads\\chromedriver-v3.1.6-win32-ia32\\chromedriver"
    electron_path = "C:\\Users\\vp094039\\AppData\\Local\\Programs\\mmb-ui\\Movie Magic Budgeting.exe"

    opts = Options()
    opts.binary_location = electron_path
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=opts)
    request.cls.driver = driver
    driver.implicitly_wait(15)
    driver.find_element_by_id('username').send_keys('vinaya.parvatikar@accionlabs.com')
    driver.find_element_by_id('password').send_keys('Welcome123$')
    driver.find_element_by_id('signOnButton').click()
    driver.implicitly_wait(10)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    assert "Startup: Open Budgets" in driver.title

    # yield driver
    # project_to_be_deleted = driver.find_element_by_xpath(
    #     '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div/div[2]/div[3]')
    # project_to_be_deleted.click()
    # delete_project = driver.find_element_by_xpath(
    #     '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/a[2]/i')
    # delete_project.click()
    # winHandleBefore = driver.window_handles[0]
    # driver.switch_to.window(winHandleBefore)
    # driver.close()

# class MyListener(AbstractEventListener):
#     def before_click(self, element, driver):
#         print("Before clicking close on window", driver.window_handles)
#
#     def after_click(self, element, driver):
#         print("After clicking close on window", driver.window_handles)


@pytest.mark.usefixtures("setup")
class TestMMB:
    def test_close_help(self):
        """Verify the help window title and close it"""
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert "Help and Tutorials" in self.driver.title
        self.driver.close()

    def test_dropdown_selection(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        assert "Startup: Open Budgets" in self.driver.title
    #     new_budget_field = self.driver.find_element_by_css_selector(
    #         '.ui.inline.dropdown .dropdown.icon')
    #     new_budget_field.click()
    #     time.sleep(2)
    #     new_blank_budget = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/'
    #                                                          'div[4]/div/div[1]/div[1]/div/div[1]/span')
    #     #
    #     # #new_blank_budget = self.driver.find_element_by_css_selector('span.text.New Blank Budget')
    #     new_blank_budget.click()
    #     created_new_budget = self.driver.find_element_by_css_selector('.grid .grid-body .row.selected .cell>input')
    #     time.sleep(2)
    #     new_budget_field.click()
    #     time.sleep(1)
    #     # #new_budget_from_template =  self.driver.find_element_by_class_name('file alternate icon')
    #     new_budget_from_template = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]'
    #                                                                  '/div/div[1]/div[1]/div/div[2]')
    #     # #new_budget_from_template = self.driver.find_element_by_css_selector('span.text.New Budget From Template')
    #     new_budget_from_template.click()
    #     time.sleep(2)
    #     # #focused = self.driver.find_element_by_class_name('active item')
    #     focused = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/a[2]')
    #     # #focused = self.driver.find_element_by_css_selector('a.active item.Templates')
    #     assert focused.text == 'TEMPLATES'
    #     time.sleep(1)
    #     # print("########################Focused element:", focused.text)
    #     switch_open_budget = self.driver.find_element_by_css_selector('.ui.menu>.item:first-child')
    #     switch_open_budget.click()
    #     time.sleep(2)
    #     """
    #     # For Import budget test
    #     new_budget_dropdown = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div'
    #                                                             '/div[4]/div/div[1]/div[1]/i')
    #     new_budget_dropdown.click()
    #     time.sleep(1)
    #     import_mmb7_budget_template = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/'
    #                                                                     'div[4]/div/div[1]/div[1]/div/div[3]/span')
    #     import_mmb7_budget_template.click()
    #     time.sleep(1)
    #
    #     # #Add the assert statement to check whether new window to select the budget to import is opened or not
    #
    #     # time.sleep(2)
    #     x = self.driver.switch_to.active_element
    #     time.sleep(5)
    #     print("###*********title of window:", x)
    #     #x.send_keys('C:\\Budget2.mbd')
    #     print("$$$$$$$$$$$$x=", x)
    #     print("*************x.text:", x.text)
    #     print("##################x.attribute:", x.get_attribute('value'))
    #     #import_mmb7_budget_template.send_keys('C:\\Budget2.mbd')
    #     time.sleep(5)
    #     """

    def test_drilling_down_sheets(self):
        select_budget = self.driver.find_element_by_css_selector('.startup .open-content .grid .cell i.icon.file, '
                                                                 '.startup .open-content .grid .cell i.icon.folder')
        action = ActionChains(self.driver)
        action.double_click(select_budget)
        action.perform()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(1)
        drilldown_to_account_from_topsheet = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/'
                                                         'div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/span')
        action = ActionChains(self.driver)
        action.double_click(drilldown_to_account_from_topsheet)
        action.perform()
        drilldown_to_detail_from_account = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]'
                                                                             '/div[1]/div/div[2]/div/div[2]/div[1]'
                                                                             '/div[1]')
        action = ActionChains(self.driver)
        action.double_click(drilldown_to_detail_from_account)
        action.perform()

    # def test_multi_window_support(self):
    #     open_setup_location = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/button[1]')
    #     open_setup_location.click()
    #     self.driver.implicitly_wait(5)
    #     self.driver.switch_to.window(self.driver.window_handles[1])
    #     assert "Budget Setup" in self.driver.title
    #     time.sleep(2)
    #     fringes_setup = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/a[2]')
    #     fringes_setup.click()
    #     time.sleep(2)
    #     globals_Setup = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/a[3]')
    #     globals_Setup.click()
    #     time.sleep(2)
    #     self.driver.close()
    #     self.driver.switch_to.window(self.driver.window_handles[0])
    #     select_option = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div')
    #     select_option.click()
    #     time.sleep(2)
    #     select_report_setup = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div[2]/'
    #                                                             'div[1]/span')
    #     select_report_setup.click()
    #     self.driver.implicitly_wait(5)
    #     self.driver.switch_to.window(self.driver.window_handles[1])
    #     time.sleep(1)
    #     assert "Report" in self.driver.title
    #     time.sleep(2)
    #     self.driver.close()
    #     # self.driver.switch_to.window(self.driver.window_handles[0])
    #     # time.sleep(1)
    #     # select_share = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/button[2]')
    #     # select_share.click()
    #     # self.driver.implicitly_wait(5)
    #     # time.sleep(2)
    #     # print("#######################Total windows:", len(self.driver.window_handles))
    #     # size = len(self.driver.window_handles)
    #     # for window in range(size-1):
    #     #     self.driver.switch_to.window(self.driver.window_handles[window])
    #     #     print(self.driver.title)
    #     #     self.driver.close()
    #
    #     # Unable to find the window handle for "Share & Delegate" window
    #     # self.driver.switch_to.window(self.driver.window_handles[3])
    #     # assert "Share" in self.driver.title
    #     # time.sleep(2)

    def test_enabling_disabling_columns(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(1)
        select_ellipsis_enable_columns_details = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/'
                                                                'div[1]/div[1]/div/div[2]/div/div[1]/div[10]/i')
        select_ellipsis_enable_columns_details.click()
        time.sleep(1)
        select_agg_column = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/label')
        select_agg_column.click()
        time.sleep(1)
        select_unit2_column = self.driver.find_element_by_xpath('/html/body/div[2]/div[9]/div/label')
        select_unit2_column.click()
        time.sleep(1)
        select_fringes_column = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/label')
        select_fringes_column.click()
        time.sleep(1)
        select_groups_column = self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/label')
        select_groups_column.click()
        time.sleep(1)
        select_location_column = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/label')
        select_location_column.click()
        time.sleep(1)
        select_set_column = self.driver.find_element_by_xpath('/html/body/div[2]/div[5]/div/label')
        select_set_column.click()

    def test_right_click_operation(self):
        action = ActionChains(self.driver)
        right_click_selected_row = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/'
                                                       'div[2]/div[1]/div[1]')
        action.context_click(right_click_selected_row)
        action.perform()
        time.sleep(5)
        insert_row = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/'
                                                       'div[1]/a[4]/span[1]')
        insert_row.click()
        time.sleep(2)

        location_field = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/'
                                                           'div/div[2]/div[1]/div[6]')
        action = ActionChains(self.driver)
        action.double_click(location_field)
        action.perform()
        time.sleep(1)
        edit_location_field = self.driver.find_element_by_class_name('typeahead')
        location_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6))
        edit_location_field.send_keys(location_string)
        time.sleep(2)
        edit_location_field.send_keys(Keys.TAB)
        time.sleep(2)
        create_new_location = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/'
                                        'div[2]/div/div[2]/div[1]/div[6]/div[1]/div[1]/div/div[2]/div/div/button[2]')
        create_new_location.click()
        time.sleep(2)
        set_field = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/'
                                                      'div[2]/div[1]/div[7]')
        action = ActionChains(self.driver)
        action.double_click(set_field)
        action.perform()
        time.sleep(1)
        edit_set_field = self.driver.find_element_by_class_name('typeahead')
        set_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=2))
        edit_set_field.send_keys(set_string)
        time.sleep(2)
        edit_set_field.send_keys(Keys.TAB)
        time.sleep(3)
        create_new_set = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/'
                                                                'div[2]/div/div[2]/div[1]/div[7]/div[1]/div[1]/div/div[2]/div/div/button[2]')
        create_new_set.click()
        time.sleep(3)
        select_field = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[8]')
        action = ActionChains(self.driver)
        action.double_click(select_field)
        action.perform()
        edit_desc_field = self.driver.find_element_by_class_name('grid-input-cell')
        edit_desc_field.send_keys("TEST")
        time.sleep(2)
        edit_desc_field.send_keys(Keys.TAB)
        time.sleep(1)

    def edit_field(self, field_name, input):
        action = ActionChains(self.driver)
        action.double_click(field_name)
        action.perform()
        edit_field = self.driver.find_element_by_class_name('grid-input-cell')
        #field_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        edit_field.send_keys(input)
        time.sleep(2)
        edit_field.send_keys(Keys.TAB)
        time.sleep(2)

    def test_budget_pref(self):
        action = ActionChains(self.driver)
        action.key_down(Keys.CONTROL).send_keys('9').key_up(Keys.CONTROL).perform()
        self.driver.implicitly_wait(5)
        #self.driver.switch_to.window(self.driver.window_handles[1])
        #time.sleep(1)


    def enable_setup_tool(self, setup_item):
        setup_item.click()
        time.sleep(1)


    def test_enable_setups(self):
        select_tools_fringes_tab = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/'
                                                                     'div/div/div[1]/div/div[1]/div[1]/a[1]')
        select_tools_fringes_tab.click()
        time.sleep(1)
        enable_fringe_1 = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/'
                                                    'div[1]/div/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]')
        self.enable_setup_tool(enable_fringe_1)
        enable_fringe_2 = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/'
                                                    'div[1]/div/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[6]/div[1]')
        self.enable_setup_tool(enable_fringe_2)
        select_tools_groups_tab = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/'
                                                                    'div/div/div[4]/div/div/div[1]/a[1]')
        select_tools_groups_tab.click()
        time.sleep(1)
        enable_group = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/'
                                                         'div[4]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]')
        self.enable_setup_tool(enable_group)
        time.sleep(1)

    def test_add_credit(self):
        credit_setup = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/button[8]')
        credit_setup.click()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(1)
        add_credit = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div/button')
        add_credit.click()
        time.sleep(1)
        close_credit_window = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]')
        close_credit_window.click()
        time.sleep(1)

    def test_add_note(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(1)
        action = ActionChains(self.driver)
        right_click_selected_row = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/'
                                                                     'div/div[2]/div/div[2]/div[1]/div[1]')
        action.context_click(right_click_selected_row)
        action.perform()
        time.sleep(1)
        add_note = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/'
                                                     'div/div[1]/a[9]')
        add_note.click()
        time.sleep(1)
        edit_note = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/div[4]/'
                                                      'div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/textarea')
        edit_note.send_keys("TEST_NOTE")
        time.sleep(1)
        #self.driver.switch_to.active_element.click()
        save_note = self.driver.find_element_by_css_selector('.ui.small.primary.button')
        save_note.click()
        # save_note = self.driver.find_element_by_xpath('/*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/div[4]/'
        #                                              'div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/div/'
        #                                              'button[2]')
        # save_note.click()
        time.sleep(1)


    # def test_add_fringes(self):
    #     fringes_field = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/div/'
    #                                                       'div[1]/div/div[1]/div[1]/a[1]')
    #     fringes_field.click()
    #     select_fringes_setup = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div[4]/div/'
    #                                                         'div/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/a')
    #     select_fringes_setup.click()
    #     self.driver.implicitly_wait(5)
    #     self.driver.switch_to.window(self.driver.window_handles[1])
    #     add_fringe = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[1]/'
    #                                                   'div/a[1]')
    #     add_fringe.click()
    #     time.sleep(1)
    #     fringe_name = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/'
    #                                                     'div[2]/div/div[2]')
    #     fringe_name_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    #     self.edit_field(fringe_name, 'test')
    #     time.sleep(1)
    #     fringe_desc = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/'
    #                                                     'div[2]/div/div[3]')
    #     fringe_desc_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    #     self.edit_field(fringe_desc, 'test')
    #     time.sleep(2)
    #     fringe_id = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/'
    #                                                     'div[2]/div/div[4]')
    #     self.edit_field(fringe_id, 15)
    #     time.sleep(1)
    #     fringe_rate = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/'
    #                                                     'div[2]/div/div[5]')
    #     self.edit_field(fringe_rate, 14)
    #     time.sleep(1)
    #     fringe_cutoff = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div/div[4]/div/div[2]/'
    #                                                       'div[2]/div/div[7]')
    #     self.edit_field(fringe_cutoff, 16)
    #     time.sleep(2)

        # ef_driver = EventFiringWebDriver(self.driver, MyListener())
        # ef_driver.execute_script()
        # time.sleep(2)
        #
        # self.driver.switch_to.window(self.driver.window_handles[0])
        # time.sleep(2)
        # # close_fringe_setup = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/button')
        # # close_fringe_setup.click()
        # # time.sleep(1)
