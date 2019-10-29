import pytest

from pages.csms import aaa_page

@pytest.mark.usefixtures('driver')
class TestDemo(object):

    def test_01_order(self):
        aaa = aaa_page.AAAPage(self.driver)
        aaa.is_page_persent()