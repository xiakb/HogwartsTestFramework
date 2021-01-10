from appium.webdriver.common.mobileby import MobileBy


class BlackList:
    """
    黑名单
    """
    _advertising_popup = (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/ib_close']")
    _login_popup = (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")

    @classmethod
    def black_list(cls):
        """
        黑名单列表 \n
        :return: 黑名单列表
        """
        black_lists = [cls._advertising_popup, cls._login_popup]
        return black_lists

