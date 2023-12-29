import data
from UrbanRoutesPage import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import selector


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)

    def setup_method(self):
        self.driver.get(data.urban_routes_url)
        self.routes_page = UrbanRoutesPage(self.driver)

    def configure_address(self):
        address_from = data.address_from
        address_to = data.address_to
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "from")))
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def select_comfort_rate(self):
        self.configure_address()
        self.routes_page.check_mode_button_in_is_enabled()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[1]/div[3]')))
        self.routes_page.check_text_mode_button()
        self.routes_page.click_mode_button()
        self.routes_page.check_order_a_taxi_button_is_enabled()
        assert self.routes_page.is_order_taxi_button_enabled()
        self.routes_page.check_text_order_a_taxi_button()
        self.routes_page.click_order_a_taxi_button()
        self.routes_page.check_rate_selection_is_enabled()
        assert self.routes_page.is_rate_selection_enabled()
        self.routes_page.check_text_rate_selection()
        self.routes_page.click_rate_selection()

    def fill_phone_number(self):
        add_phone_number = data.phone_number
        self.select_comfort_rate()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]')))
        self.routes_page.check_phone_number_field_is_enabled()
        assert self.routes_page.is_phone_number_field_enabled()
        self.routes_page.check_text_phone_number_field()
        self.routes_page.click_phone_number_field()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(selector.phone_number_field))
        self.routes_page.check_enter_phone_number_is_enabled()
        self.routes_page.check_text_enter_phone_number()
        self.routes_page.click_enter_phone_number()
        time.sleep(1)
        self.routes_page.set_phone_number(add_phone_number)
        self.routes_page.click_save_phone_number()
        self.routes_page.check_field_code_is_enabled()
        self.routes_page.check_text_field_code()
        self.routes_page.click_field_code()
        self.routes_page.check_save_code_button_is_enabled()
        self.routes_page.check_text_save_code_button()
        self.routes_page.click_save_code()

    def add_credit_card(self):
        add_number_card = data.card_number
        add_code_card = data.card_code
        self.fill_phone_number()
        self.routes_page.check_way_to_pay_button_is_enabled()
        assert self.routes_page.is_way_to_pay_button_enabled()
        self.routes_page.check_text_way_to_pay_button()
        self.routes_page.click_way_to_pay_button()
        time.sleep(1)
        self.routes_page.check_add_card_button_is_enabled()
        self.routes_page.click_add_card()
        time.sleep(1)
        self.routes_page.check_number_card_is_enabled()
        self.routes_page.check_text_card_number()
        self.routes_page.click_card_number()
        self.routes_page.set_enter_number_card(add_number_card)
        self.routes_page.check_save_card_button_is_disabled()
        self.routes_page.check_code_card_is_enabled()
        self.routes_page.check_text_code_card()
        self.routes_page.click_code_card()
        self.routes_page.set_enter_code_card(add_code_card)
        self.routes_page.tab_code_card()
        self.routes_page.check_save_code_button_is_enabled()
        self.routes_page.click_save_card_button()
        self.routes_page.check_new_card_is_present()
        self.routes_page.new_card_is_select()
        self.routes_page.click_close_way_to_pay()

    def write_message_to_driver(self):
        comment_to_the_driver = data.message_for_driver
        self.add_credit_card()
        assert self.routes_page.is_enter_comment_to_the_driver_button_enabled()
        self.routes_page.set_enter_comment_to_the_driver(comment_to_the_driver)

    def request_blankets_and_scarves(self):
        self.write_message_to_driver()
        self.routes_page.check_blankets_and_scarves_is_present()
        self.routes_page.check_switch_blankets_and_scarves_is_disabled()
        self.routes_page.click_activate_switch_blankets_and_scarves()
        self.routes_page.check_switch_blankets_and_scarves_is_enabled()

    def order_2_ice_creams(self):
        self.request_blankets_and_scarves()
        assert self.routes_page.check_text_ice_cream_n0(), f'El texto del campo helado no coincide'
        self.routes_page.click_add_ice_cream()

    def modal_appears_for_taxi_search(self):
        self.request_blankets_and_scarves()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button/span[1]')))
        self.routes_page.check_order_a_taxi_button_is_enabled()
        self.routes_page.check_text_order_a_taxi_button2()
        self.routes_page.click_order_taxi_button()

    def wait_for_driver_info_in_modal(self):
        self.modal_appears_for_taxi_search()
        time.sleep(40)

    def test_configure_address(self):
        self.configure_address()
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    def test_select_comfort_rate(self):
        self.select_comfort_rate()
        assert EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]'))

    def test_fill_phone_number(self):
        self.fill_phone_number()
        assert self.routes_page.is_phone_number_field_enabled()

    def test_add_credit_card(self):
        self.add_credit_card()
        assert self.routes_page.is_way_to_pay_button_enabled()

    def test_write_message_to_driver(self):
        self.write_message_to_driver()
        assert self.routes_page.is_enter_comment_to_the_driver_button_enabled()

    def test_request_blankets_and_scarves(self):
        self.request_blankets_and_scarves()
        assert self.routes_page.check_text_blankets_and_scarves(), f'El texto del campo mantas no coincide'

    def test_order_2_ice_creams(self):
        self.order_2_ice_creams()
        assert self.routes_page.check_text_ice_cream_n2(), f'El texto del campo helado no coincide'

    def test_modal_appears_for_taxi_search(self):
        self.modal_appears_for_taxi_search()
        assert self.routes_page.check_order_a_taxi_button_is_enabled()

    def test_wait_for_driver_info_in_modal(self):
        self.wait_for_driver_info_in_modal()
        assert self.driver.find_element(*selector.modal_searching).text.startswith('El conductor llegará en')

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
