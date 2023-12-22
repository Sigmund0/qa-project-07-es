import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import time


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    mode_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[1]/div[3]')
    order_a_taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    rate_selection = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    phone_number_field = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]')
    enter_phone_number = (By.ID, 'phone')
    text_enter_phone_number = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[1]/div[1]/label')
    save_phone_number = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    order_taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button')
    text_order_taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button/span[1]')
    text_enter_code = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[1]/div[1]')
    click_enter_code = (By.ID, 'code')
    save_code_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    way_to_pay = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]')
    add_card = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[3]/div')
    number_card = (By.ID, 'number')
    code_card = (By.CSS_SELECTOR, '#code.card-input')
    button_save_card = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    new_card = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]')
    close_way_to_pay = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    comment_to_the_driver = (By.CSS_SELECTOR, '#comment.input')
    container_blankets_and_scarves = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div')
    activate_switch_blankets_and_scarves = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div')
    container_ice_cream = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div')
    add_ice_cream =(By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def set_number(self, phone_number):
        self.driver.find_element(*self.enter_phone_number).send_keys(phone_number)

    def get_number(self):
        return self.driver.find_element(*self.enter_phone_number).get_property('value')

    def set_phone_number(self, add_phone_number):
        self.set_number(add_phone_number)

    def set_number_card(self, enter_number_card):
        self.driver.find_element(*self.number_card).send_keys(enter_number_card)

    def get_number_card(self):
        return self.driver.find_element(*self.number_card).get_property('value')

    def set_enter_number_card(self, add_number_card):
        self.set_number_card(add_number_card)

    def set_code_card(self, enter_code_card):
        self.driver.find_element(*self.code_card).send_keys(enter_code_card)

    def tab_code_card(self):
        self.driver.find_element(*self.code_card).send_keys(Keys.TAB)
    def get_code_card(self):
        return self.driver.find_element(*self.code_card).get_property('value')

    def set_enter_code_card(self, add_code_card):
        self.set_code_card(add_code_card)

    def set_comment_to_the_driver(self, text_to_enter):
        self.driver.find_element(*self.comment_to_the_driver).send_keys(text_to_enter)

    def get_comment_to_the_driver(self):
        return self.driver.find_element(*self.comment_to_the_driver).get_property('value')

    def set_enter_comment_to_the_driver(self, enter_comment):
        self.set_comment_to_the_driver(enter_comment)

    def check_mode_button_in_is_enabled(self):
        return self.driver.find_element(*self.mode_button).is_enabled()

    def check_text_mode_button(self):
        registration_button_text = self.driver.find_element(*self.mode_button).text
        assert registration_button_text == 'Personal', 'El texto del botón no coincide con "Personal"'

    def click_mode_button(self):
        self.driver.find_element(*self.mode_button).click()

    def check_order_a_taxi_button_is_enabled(self):
        return self.driver.find_element(*self.order_a_taxi).is_enabled()

    def check_text_order_a_taxi_button(self):
        registration_button_text = self.driver.find_element(*self.order_a_taxi).text
        assert registration_button_text == 'Pedir un taxi', 'El texto del botón no coincide con "Pedir un taxi"'

    def click_order_a_taxi_button(self):
        self.driver.find_element(*self.order_a_taxi).click()

    def check_rate_selection_is_enabled(self):
        return self.driver.find_element(*self.rate_selection).is_enabled()

    def check_text_rate_selection(self):
        registration_button_text = self.driver.find_element(*self.rate_selection).text
        assert registration_button_text == 'Comfort\n$10', 'El texto del botón no coincide con "Comfort"'

    def click_rate_selection(self):
        self.driver.find_element(*self.rate_selection).click()

    def check_phone_number_field_is_enabled(self):
        return self.driver.find_element(*self.phone_number_field).is_enabled()

    def check_text_phone_number_field(self):
        registration_button_text = self.driver.find_element(*self.phone_number_field).text
        assert registration_button_text == 'Número de teléfono', 'El texto del botón no coincide con "Número de teléfono"'

    def click_phone_number_field(self):
        self.driver.find_element(*self.phone_number_field).click()

    def check_enter_phone_number_is_enabled(self):
        return self.driver.find_element(*self.enter_phone_number).is_enabled()

    def check_text_enter_phone_number(self):
        registration_button_text = self.driver.find_element(*self.text_enter_phone_number).text
        assert registration_button_text == 'Número de teléfono', 'El texto del botón no coincide con "Número de teléfono"'

    def click_enter_phone_number(self):
        input_element = self.driver.find_element(*self.enter_phone_number)
        self.driver.execute_script("arguments[0].click();", input_element)

    def click_save_phone_number(self):
        self.driver.find_element(*self.save_phone_number).click()

    def check_field_code_is_enabled(self):
        return self.driver.find_element(*self.click_enter_code).is_enabled()

    def check_text_field_code(self):
        registration_button_text = self.driver.find_element(*self.text_enter_code).text
        assert registration_button_text == 'Introduce el código', 'El texto del botón no coincide con "Introduce el código"'

    def click_field_code(self):
        code = retrieve_phone_code(
            self.driver)  # Asegúrate de que retrieve_phone_code acepte el argumento del controlador.
        input_element = self.driver.find_element(*self.click_enter_code)
        input_element.clear()  # Limpia cualquier texto existente en el campo (opcional)
        input_element.send_keys(code)
        input_element.click()

    def check_save_code_button_is_enabled(self):
        return self.driver.find_element(*self.save_code_button).is_enabled()

    def check_text_save_code_button(self):
        registration_button_text = self.driver.find_element(*self.save_code_button).text
        assert registration_button_text == 'Confirmar', 'El texto del botón no coincide con "Confirmar"'

    def click_save_code(self):
        self.driver.find_element(*self.save_code_button).click()

    def check_way_to_pay_button_is_enabled(self):
        return self.driver.find_element(*self.way_to_pay).is_enabled()

    def check_text_way_to_pay_button(self):
        registration_button_text = self.driver.find_element(*self.way_to_pay).text
        assert registration_button_text == 'Forma de pago\nEfectivo', 'El texto del botón no coincide con "Forma de pago"'
    def click_way_to_pay_button(self):
        self.driver.find_element(*self.way_to_pay).click()
    def check_add_card_button_is_enabled(self):
        return self.driver.find_element(*self.add_card).is_enabled()
    def click_add_card(self):
        self.driver.find_element(*self.add_card).click()
    def check_number_card_is_enabled(self):
        return self.driver.find_element(*self.number_card).is_enabled()

    def check_text_card_number(self):
        card_number_placeholder = self.driver.find_element(*self.number_card).get_attribute("placeholder")
        expected_text = '1234 0000 4321'
        assert card_number_placeholder == expected_text, f'El texto del campo no coincide con "{expected_text}"'

    def click_card_number(self):
        input_element = self.driver.find_element(*self.number_card)
        self.driver.execute_script("arguments[0].click();", input_element)

    def check_code_card_is_enabled(self):
        return self.driver.find_element(*self.code_card).is_enabled()

    def check_text_code_card(self):
        card_code_placeholder = self.driver.find_element(*self.code_card).get_attribute("placeholder")
        expected_text = '12'
        assert card_code_placeholder == expected_text, f'El texto del campo no coincide con "{expected_text}"'

    def click_code_card(self):
        self.driver.find_element(*self.code_card).click()

    def check_save_card_button_is_enabled(self):
        return self.driver.find_element(*self.button_save_card).is_enabled()

    def check_save_card_button_is_disabled(self):
        save_card_button = self.driver.find_element(*self.button_save_card)
        return save_card_button.get_attribute("disabled") == "true"
    def click_save_card_button(self):
        self.driver.find_element(*self.button_save_card).click()

    def check_new_card_is_present(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.new_card)
            )
            return True
        except TimeoutException:
            return False
    def new_card_is_select(self):
        return self.driver.find_element(*self.new_card).is_selected()

    def click_close_way_to_pay(self):
        return self.driver.find_element(*self.close_way_to_pay).click()

    def check_blankets_and_scarves_is_present(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.container_blankets_and_scarves)
            )
            return True
        except TimeoutException:
            return False

    def check_text_blankets_and_scarves(self):
        element = self.driver.find_element(*self.container_blankets_and_scarves)
        actual_text = element.text
        expected_text = 'Manta y pañuelos'
        assert actual_text == expected_text, f'El texto del campo no coincide con "{expected_text}"'

    def check_switch_blankets_and_scarves_is_enabled(self):
        return self.driver.find_element(*self.activate_switch_blankets_and_scarves).is_enabled()

    def check_switch_blankets_and_scarves_is_disabled(self):
        switch_blankets_and_scarves = self.driver.find_element(*self.activate_switch_blankets_and_scarves)
        return switch_blankets_and_scarves.get_attribute("disabled") == "true"


    def click_activate_switch_blankets_and_scarves(self):
        return self.driver.find_element(*self.activate_switch_blankets_and_scarves).click()

    def check_text_ice_cream_n0(self):
        element = self.driver.find_element(*self.container_ice_cream)
        actual_text = element.text
        expected_text = 'Helado\n–\n0\n+'
        assert actual_text == expected_text, f'El texto del campo no coincide con "{expected_text}"'

    def click_add_ice_cream(self):
        ice_cream_element = self.driver.find_element(*self.add_ice_cream)
        ice_cream_element.click()
        ice_cream_element.click()
    def check_text_ice_cream_n2(self):
        element = self.driver.find_element(*self.container_ice_cream)
        actual_text = element.text
        expected_text = 'Helado\n–\n2\n+'
        assert actual_text == expected_text, f'El texto del campo no coincide con "{expected_text}"'

    def check_order_taxi_button_is_enabled(self):
        return self.driver.find_element(*self.order_taxi_button).is_enabled()

    def check_text_order_a_taxi_button2(self):
        registration_button_text = self.driver.find_element(*self.text_order_taxi).text
        assert registration_button_text == 'Pedir un taxi', 'El texto del botón no coincide con "Pedir un taxi"'

    def click_order_taxi_button(self):
        try:
            input_element = self.driver.find_element(*self.order_taxi_button)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.order_taxi_button)
            )
            self.driver.execute_script("arguments[0].click();", input_element)
        except Exception as e:
            print(f"Error al hacer clic en el botón: {e}")

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)

    def test_full_flow(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        add_phone_number = data.phone_number
        add_number_card = data.card_number
        add_code_card = data.card_code
        comment_to_the_driver = data.message_for_driver
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "from")))
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        routes_page.check_mode_button_in_is_enabled()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[1]/div[3]')))
        routes_page.check_text_mode_button()
        routes_page.click_mode_button()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')))
        routes_page.check_order_a_taxi_button_is_enabled()
        routes_page.check_text_order_a_taxi_button()
        routes_page.click_order_a_taxi_button()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')))
        routes_page.check_rate_selection_is_enabled()
        routes_page.check_text_rate_selection()
        routes_page.click_rate_selection()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]')))
        routes_page.check_phone_number_field_is_enabled()
        routes_page.check_text_phone_number_field()
        routes_page.click_phone_number_field()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(routes_page.phone_number_field))
        routes_page.check_enter_phone_number_is_enabled()
        routes_page.check_text_enter_phone_number()
        routes_page.click_enter_phone_number()
        time.sleep(1)
        routes_page.set_phone_number(add_phone_number)
        routes_page.click_save_phone_number()
        routes_page.check_field_code_is_enabled()
        routes_page.check_text_field_code()
        routes_page.click_field_code()
        routes_page.check_save_code_button_is_enabled()
        routes_page.check_text_save_code_button()
        routes_page.click_save_code()
        routes_page.check_way_to_pay_button_is_enabled()
        routes_page.check_text_way_to_pay_button()
        routes_page.click_way_to_pay_button()
        time.sleep(1)
        routes_page.check_add_card_button_is_enabled()
        routes_page.click_add_card()
        time.sleep(1)
        routes_page.check_number_card_is_enabled()
        routes_page.check_text_card_number()
        routes_page.click_card_number()
        routes_page.set_enter_number_card(add_number_card)
        routes_page.check_save_card_button_is_disabled()
        routes_page.check_code_card_is_enabled()
        routes_page.check_text_code_card()
        routes_page.click_code_card()
        routes_page.set_enter_code_card(add_code_card)
        routes_page.tab_code_card()
        routes_page.check_save_code_button_is_enabled()
        routes_page.click_save_card_button()
        routes_page.check_new_card_is_present()
        routes_page.new_card_is_select()
        routes_page.click_close_way_to_pay()
        routes_page.set_enter_comment_to_the_driver(comment_to_the_driver)
        routes_page.check_blankets_and_scarves_is_present()
        routes_page.check_text_blankets_and_scarves()
        routes_page.check_switch_blankets_and_scarves_is_disabled()
        routes_page.click_activate_switch_blankets_and_scarves()
        routes_page.check_switch_blankets_and_scarves_is_enabled()
        routes_page.check_text_ice_cream_n0()
        routes_page.click_add_ice_cream()
        routes_page.check_text_ice_cream_n2()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button/span[1]')))
        routes_page.check_order_a_taxi_button_is_enabled()
        routes_page.check_text_order_a_taxi_button2()
        time.sleep(5)
        routes_page.click_order_taxi_button()
        time.sleep(35)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
