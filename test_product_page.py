from .pages.product_page import ProductPage
import pytest


list_N = [n if n != 7 else pytest.param(n, marks=pytest.mark.xfail(reason="fixing this bug righ tnow")) for n in range(10)]

@pytest.mark.parametrize("N", list_N)
def test_guest_can_add_product_to_basket(browser, N):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{N}"
    page = ProductPage(browser, link)
    page.open()
    page.click_on_button()
    page.solve_quiz_and_get_code()
    page.should_message_product_added_to_cart()
    page.should_message_cost_basket()



