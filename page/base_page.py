from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from driver.black_handle import black_wrapper
from driver.black_list import BlackList


class BasePage:
    def __init__(self, driver: WebDriver = None):
        """
        初始化driver、黑名单列表
        :param driver:
        """
        self.driver = driver
        self.black_list = BlackList.black_list()

    @black_wrapper
    def find(self, by, locator):
        """
        element定位器
        :param by: 定位方法
        :param locator: 素属性值
        :return: element定位器
        """
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        """
        elements定位器
        :param by: 定位方法
        :param locator: 元素属性值
        :return: elements定位器
        """
        return self.driver.find_elements(by, locator)

    def scroll_find(self, text):
        """
        根据text属性值滚动查找元素
        :param text: 需要查找元素的text属性值
        :return: 查找到的元素
        """
        scroll = (MobileBy.ANDROID_UIAUTOMATOR, "new UiScrollable(new UiSelector()."
                                                "scrollable(true)."
                                                "instance(0))."
                                                "scrollIntoView(new UiSelector()."
                                                f"text({text}).instance(0));")
        return self.find(*scroll)

    def display_wait(self, locator):
        """
        显示等待
        :param locator: 需要等待的元素
        :return:
        """
        return WebDriverWait(self.driver, 9).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for(self, *loc):
        def wait_ele_for():
            eles = self.finds(*loc)
            return len(eles) > 0
        WebDriverWait(self.driver, 10).until(wait_ele_for)

    def get_window_size(self):
        """
        获取屏幕尺寸
        :return:
        """
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        """
        屏幕滑动
        :param start_x: 起始点的横坐标
        :param start_y: 起始点的纵坐标
        :param end_x: 结束点的横坐标
        :param end_y: 结束点的纵坐标
        :param duration: 持续时长
        :return:
        """
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def swipe_find(self, *loc, start_x, start_y, end_x, end_y, duration):
        self.driver.implicitly_wait(2)
        elements = self.finds(*loc)
        while len(elements) == 0:
            self.swipe(start_x, start_y, end_x, end_y, duration)
            elements = self.finds(*loc)
        return elements[0]


