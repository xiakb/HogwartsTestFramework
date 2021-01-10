from page.base_page import BasePage


class PrePage:
    """
    driver对象
    """
    def __init__(self, base_page: BasePage):
        """
        初始化driver对象 \n
        :param base_page: driver对象
        """
        self.base_page = base_page
