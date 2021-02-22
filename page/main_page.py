from appium.webdriver.common.mobileby import MobileBy
from page.pre_page import PrePage
from page.quotes_page import QuotesPage


class MainPage(PrePage):
    """
    雪球首页
    """
    # _quotes = (MobileBy.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']")
    # _pen = (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']")

    def goto_quotes_page(self):
        """
        跳转到行情页 \n
        :return: 行情页
        """
        # self.base_page.find(*self._pen).click()
        # self.base_page.find(*self._quotes).click()
        self.base_page.load("quotes_page", "../data/main_page.yaml")
        return QuotesPage(self.base_page)

