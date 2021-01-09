from appium.webdriver.common.mobileby import MobileBy
from page.base_page import BasePage
from page.quotes_page import QuotesPage


class MainPage(BasePage):
    """
    需求首页
    """
    _quotes = (MobileBy.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']")
    _pen = (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']")

    def goto_quotes_page(self):
        """
        跳转到行情页
        :return: 行情页
        """
        self.find(*self._pen).click()
        self.find(*self._quotes).click()
        return QuotesPage(self.driver)

