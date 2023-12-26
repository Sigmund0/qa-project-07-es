from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import selector
from retrieve_phone_code import retrieve_phone_code
class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*selector.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*selector.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*selector.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*selector.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def set_number(self, phone_number):
        self.driver.find_element(*selector.enter_phone_number).send_keys(phone_number)

    def get_number(self):
        return self.driver.find_element(*selector.enter_phone_number).get_property('value')

    def set_phone_number(self, add_phone_number):
        self.set_number(add_phone_number)

    def set_number_card(self, enter_number_card):
        self.driver.find_element(*selector.number_card).send_keys(enter_number_card)

    def get_number_card(self):
        return self.driver.find_element(*selector.number_card).get_property('value')

    def set_enter_number_card(self, add_number_card):
        self.set_number_card(add_number_card)

    def set_code_card(self, enter_code_card):
        self.driver.find_element(*selector.code_card).send_keys(enter_code_card)

    def tab_code_card(self):
        self.driver.find_element(*selector.code_card).send_keys(Keys.TAB)
    def get_code_card(self):
        return self.driver.find_element(*selector.code_card).get_property('value')

    def set_enter_code_card(self, add_code_card):
        self.set_code_card(add_code_card)

    def set_comment_to_the_driver(self, text_to_enter):
        self.driver.find_element(*selector.comment_to_the_driver).send_keys(text_to_enter)

    def get_comment_to_the_driver(self):
        return self.driver.find_element(*selector.comment_to_the_driver).get_property('value')

    def set_enter_comment_to_the_driver(self, enter_comment):
        self.set_comment_to_the_driver(enter_comment)

    def check_mode_button_in_is_enabled(self):
        return self.driver.find_element(*selector.mode_button).is_enabled()

    def check_text_mode_button(self):
        registration_button_text = self.driver.find_element(*selector.mode_button).text
        assert registration_button_text == 'Personal', 'El texto del botón no coincide con "Personal"'

    def click_mode_button(self):
        self.driver.find_element(*selector.mode_button).click()

    def check_order_a_taxi_button_is_enabled(self):
        return self.driver.find_element(*selector.order_a_taxi).is_enabled()

    def check_text_order_a_taxi_button(self):
        registration_button_text = self.driver.find_element(*selector.order_a_taxi).text
        assert registration_button_text == 'Pedir un taxi', 'El texto del botón no coincide con "Pedir un taxi"'

    def click_order_a_taxi_button(self):
        self.driver.find_element(*selector.order_a_taxi).click()

    def check_rate_selection_is_enabled(self):
        return self.driver.find_element(*selector.rate_selection).is_enabled()

    def check_text_rate_selection(self):
        registration_button_text = self.driver.find_element(*selector.rate_selection).text
        assert registration_button_text == 'Comfort\n$10', 'El texto del botón no coincide con "Comfort"'

    def click_rate_selection(self):
        self.driver.find_element(*selector.rate_selection).click()

    def check_phone_number_field_is_enabled(self):
        return self.driver.find_element(*selector.phone_number_field).is_enabled()

    def check_text_phone_number_field(self):
        registration_button_text = self.driver.find_element(*selector.phone_number_field).text
        assert registration_button_text == 'Número de teléfono', 'El texto del botón no coincide con "Número de teléfono"'

    def click_phone_number_field(self):
        self.driver.find_element(*selector.phone_number_field).click()

    def check_enter_phone_number_is_enabled(self):
        return self.driver.find_element(*selector.enter_phone_number).is_enabled()

    def check_text_enter_phone_number(self):
        registration_button_text = self.driver.find_element(*selector.text_enter_phone_number).text
        assert registration_button_text == 'Número de teléfono', 'El texto del botón no coincide con "Número de teléfono"'

    def click_enter_phone_number(self):
        input_element = self.driver.find_element(*selector.enter_phone_number)
        self.driver.execute_script("arguments[0].click();", input_element)

    def click_save_phone_number(self):
        self.driver.find_element(*selector.save_phone_number).click()

    def check_field_code_is_enabled(self):
        return self.driver.find_element(*selector.click_enter_code).is_enabled()

    def check_text_field_code(self):
        registration_button_text = self.driver.find_element(*selector.text_enter_code).text
        assert registration_button_text == 'Introduce el código', 'El texto del botón no coincide con "Introduce el código"'

    def click_field_code(self):
        code = retrieve_phone_code(
            self.driver)  # Asegúrate de que retrieve_phone_code acepte el argumento del controlador.
        input_element = self.driver.find_element(*selector.click_enter_code)
        input_element.clear()  # Limpia cualquier texto existente en el campo (opcional)
        input_element.send_keys(code)
        input_element.click()

    def check_save_code_button_is_enabled(self):
        return self.driver.find_element(*selector.save_code_button).is_enabled()

    def check_text_save_code_button(self):
        registration_button_text = self.driver.find_element(*selector.save_code_button).text
        assert registration_button_text == 'Confirmar', 'El texto del botón no coincide con "Confirmar"'

    def click_save_code(self):
        self.driver.find_element(*selector.save_code_button).click()

    def check_way_to_pay_button_is_enabled(self):
        return self.driver.find_element(*selector.way_to_pay).is_enabled()

    def check_text_way_to_pay_button(self):
        registration_button_text = self.driver.find_element(*selector.way_to_pay).text
        assert registration_button_text == 'Forma de pago\nEfectivo', 'El texto del botón no coincide con "Forma de pago"'
    def click_way_to_pay_button(self):
        self.driver.find_element(*selector.way_to_pay).click()
    def check_add_card_button_is_enabled(self):
        return self.driver.find_element(*selector.add_card).is_enabled()
    def click_add_card(self):
        self.driver.find_element(*selector.add_card).click()
    def check_number_card_is_enabled(self):
        return self.driver.find_element(*selector.number_card).is_enabled()

    def check_text_card_number(self):
        card_number_placeholder = self.driver.find_element(*selector.number_card).get_attribute("placeholder")
        expected_text = '1234 0000 4321'
        assert card_number_placeholder == expected_text, f'El texto del campo no coincide con "{expected_text}"'

    def click_card_number(self):
        input_element = self.driver.find_element(*selector.number_card)
        self.driver.execute_script("arguments[0].click();", input_element)

    def check_code_card_is_enabled(self):
        return self.driver.find_element(*selector.code_card).is_enabled()

    def check_text_code_card(self):
        card_code_placeholder = self.driver.find_element(*selector.code_card).get_attribute("placeholder")
        expected_text = '12'
        assert card_code_placeholder == expected_text, f'El texto del campo no coincide con "{expected_text}"'

    def click_code_card(self):
        self.driver.find_element(*selector.code_card).click()

    def check_save_card_button_is_enabled(self):
        return self.driver.find_element(*selector.button_save_card).is_enabled()

    def check_save_card_button_is_disabled(self):
        save_card_button = self.driver.find_element(*selector.button_save_card)
        return save_card_button.get_attribute("disabled") == "true"
    def click_save_card_button(self):
        self.driver.find_element(*selector.button_save_card).click()

    def check_new_card_is_present(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(selector.new_card)
            )
            return True
        except TimeoutException:
            return False
    def new_card_is_select(self):
        return self.driver.find_element(*selector.new_card).is_selected()

    def click_close_way_to_pay(self):
        return self.driver.find_element(*selector.close_way_to_pay).click()

    def check_blankets_and_scarves_is_present(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(selector.container_blankets_and_scarves)
            )
            return True
        except TimeoutException:
            return False

    def check_text_blankets_and_scarves(self):
        element = self.driver.find_element(*selector.container_blankets_and_scarves)
        actual_text = element.text
        expected_text = 'Manta y pañuelos'
        assert actual_text == expected_text, f'El texto del campo no coincide con "{expected_text}"'

    def check_switch_blankets_and_scarves_is_enabled(self):
        return self.driver.find_element(*selector.activate_switch_blankets_and_scarves).is_enabled()

    def check_switch_blankets_and_scarves_is_disabled(self):
        switch_blankets_and_scarves = self.driver.find_element(*selector.activate_switch_blankets_and_scarves)
        return switch_blankets_and_scarves.get_attribute("disabled") == "true"


    def click_activate_switch_blankets_and_scarves(self):
        return self.driver.find_element(*selector.activate_switch_blankets_and_scarves).click()

    def check_text_ice_cream_n0(self):
        element = self.driver.find_element(*selector.container_ice_cream)
        actual_text = element.text
        expected_text = 'Helado\n–\n0\n+'
        assert actual_text == expected_text, f'El texto del campo no coincide con "{expected_text}"'

    def click_add_ice_cream(self):
        ice_cream_element = self.driver.find_element(*selector.add_ice_cream)
        ice_cream_element.click()
        ice_cream_element.click()
    def check_text_ice_cream_n2(self):
        element = self.driver.find_element(*selector.container_ice_cream)
        actual_text = element.text
        expected_text = 'Helado\n–\n2\n+'
        assert actual_text == expected_text, f'El texto del campo no coincide con "{expected_text}"'

    def check_order_taxi_button_is_enabled(self):
        return self.driver.find_element(*selector.order_taxi_button).is_enabled()

    def check_text_order_a_taxi_button2(self):
        registration_button_text = self.driver.find_element(*selector.text_order_taxi).text
        assert registration_button_text == 'Pedir un taxi', 'El texto del botón no coincide con "Pedir un taxi"'

    def click_order_taxi_button(self):
        try:
            input_element = self.driver.find_element(*selector.order_taxi_button)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(selector.order_taxi_button)
            )
            self.driver.execute_script("arguments[0].click();", input_element)
        except Exception as e:
            print(f"Error al hacer clic en el botón: {e}")


