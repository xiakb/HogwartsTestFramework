from page.base_page import BasePage
from page.main_page import MainPage


class TestSearch:
    def setup_class(self):
        base_page = BasePage()
        self.app = MainPage(base_page)

    def teardown_class(self):
        self.app.base_page.quit()

    def test_search(self):
        self.app.goto_quotes_page()

