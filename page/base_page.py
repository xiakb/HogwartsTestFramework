import os
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from common.black_handle import black_wrapper
from common.black_list import BlackList
from common.desired_cap import desired_cap
from common.common_fun import *


class BasePage:
    FIND = "find"
    ACTION = "action"
    FIND_AND_CLICK = "find_and_click"
    SEND = "send"
    CONTENT = "content"
    LOCATE_MODE = "locate_mode"

    def __init__(self):
        """
        初始化driver、黑名单列表
        """
        self.driver = desired_cap()
        self.black_list = BlackList.black_list()
        self.driver.implicitly_wait(8)

    @black_wrapper
    def find(self, by, locator):
        """
        element定位器 \n
        :param by: 定位方法
        :param locator: 元素属性值
        :return: element定位器
        """
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        """
        定位元素，并点击 \n
        :param by: 定位方法
        :param locator: 元素属性值
        :return: 定位元素，并点击
        """
        return self.find(by, locator).click()

    def send(self, by, locator, content):
        """
        定位元素，并输入内容 \n
        :param by: 定位方法
        :param locator: 元素属性值
        :param content: 输入的内容
        :return: 定位元素，并输入内容
        """
        return self.find(by, locator).send_keys(content)

    def finds(self, by, locator):
        """
        elements定位器 \n
        :param by: 定位方法
        :param locator: 元素属性值
        :return: elements定位器
        """
        return self.driver.find_elements(by, locator)

    def scroll_find(self, text):
        """
        根据text属性值滚动查找元素 \n
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
        显示等待 \n
        :param locator: 需要等待的元素
        :return:
        """
        return WebDriverWait(self.driver, 9).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for(self, *loc):
        """
        显示等待 \n
        :param loc: 需要等待的元素
        :return:
        """
        def wait_ele_for():
            eles = self.finds(*loc)
            return len(eles) > 0
        WebDriverWait(self.driver, 10).until(wait_ele_for)

    def get_window_size(self):
        """
        获取屏幕尺寸 \n
        :return: 屏幕尺寸
        """
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        """
        屏幕滑动 \n
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

    def load(self, page, filepath):
        """
        操作元素 \n
        :param filepath: 读取文件的路径
        :return:
        """
        data = get_yaml_data(filepath)
        for key in data:
            if page == key:
                for step in data[key]:
                    attribute_value = step.get(self.FIND)
                    action = step.get(self.ACTION)
                    locate_mode = step.get(self.LOCATE_MODE)
                    if action == self.FIND_AND_CLICK:
                        self.find_and_click(location_mode(locate_mode), attribute_value)
                    elif action == self.SEND:
                        content = step.get(self.CONTENT)
                        self.send(location_mode(locate_mode), attribute_value, content)

    def restart(self):
        """
        重启APP \n
        :return: self
        """
        self.driver.close_app()
        self.driver.launch_app()
        return self

    def quit(self):
        """
        停止APP或退出浏览器 \n
        :return:
        """
        self.driver.quit()

    def screenshot(self, module):
        """
        截图，并保存到指定的文件夹 \n
        :param module: 文件夹名称
        :return:
        """
        now_time = get_time()
        image_file = os.path.dirname(os.path.dirname(__file__)) + f'/screenshots/{module}_{now_time}.png'
        self.driver.get_screenshot_as_file(image_file)

    def latest_screenshot(self, screenshot_dir):
        """
        查找最新的截图，并返回 \n
        1、os.listdir() 用于返回指定文件夹包含的文件或文件夹的名称的列表 \n
        2、sort()按时间顺序对该文件夹下面的文件进行排序 \n
        3、os.path.join()输出最新的报告路径 \n
        :param screenshot_dir: 接收存放截图的路径
        :return: 返回最新的截图
        """
        lists = os.listdir(screenshot_dir)
        lists.sort(key=lambda fn: os.path.getatime(screenshot_dir + '//' + fn))
        picture = os.path.join(screenshot_dir, lists[-1])
        return picture
