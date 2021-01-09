from driver.app_driver import AppDriver


class TestSearch:
    def setup_class(self):
        self.app = AppDriver()

    def teardown_class(self):
        self.app.stop()

    def test_search(self):
        self.app.start().goto_main_page().goto_quotes_page()

