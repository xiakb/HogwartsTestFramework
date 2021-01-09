from driver.desired_cap import *
from page.base_page import BasePage
from page.main_page import MainPage


class AppDriver(BasePage):
    """
    启动、重启、停止App
    """
    def start(self):
        """
        启动 APP
        :return: self
        """
        if self.driver is None:
            self.driver = desired_cap()
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(8)
        return self

    def restart(self):
        """
        重启 APP
        :return: self
        """
        self.driver.close_app()
        self.driver.launch_app()
        return self

    def stop(self):
        """
        停止 APP
        :return:
        """
        self.driver.quit()

    def goto_main_page(self):
        """
        跳转到首页
        :return: 首页对象
        """
        return MainPage(self.driver)


if __name__ == '__main__':
    app = AppDriver()
    app.start()
