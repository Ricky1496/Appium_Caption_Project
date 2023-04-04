import pytest
from appium.webdriver.common.appiumby import AppiumBy


@pytest.mark.usefixtures("start_appium_server")
class TestAndroidDeviceLocal:
    def test_allow_notification(self):
        self.driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_deny_button").click()

    def test_swipe_down(self):
        self.driver.swipe(540, 736, 540, 1568)

    def test_search(self):
        self.driver.find_element(AppiumBy.ID, "naukriApp.appModules.login:id/editTextSearch").click()

    def test_enter_skills(self):
        self.driver.find_element(AppiumBy.ID, "naukriApp.appModules.login:id/et_skills").send_keys("Python")

    def test_enter_location(self):
        self.driver.find_element(AppiumBy.ID, "naukriApp.appModules.login:id/et_loc").send_keys("Ahmedabad")

    def test_search_jobs(self):
        self.driver.find_element(AppiumBy.ID, "naukriApp.appModules.login:id/b_search").click()
