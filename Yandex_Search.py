from BaseApp import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException 


class YandexSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = "//input[@name='text']"


class SearchHelper (BasePage):
    
    def search_field(self):
        """
        Поиск строки поиска

        Возвращает:
        True/False - нашел/не нашел (bool)
        """
        try:
            search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
            self.search_field = search_field
        except NoSuchElementException:
            return False
        return True

    def enter_word(self, word): 
        """
        Печать в строке поиска

        Вход:
        word - слово для печати в строке (string)
        """       
        self.search_field.send_keys(word)  

    def check_suggest(self):
        """
        Обнаружение таблицы подсказок

        Возвращает:
        True/False - нашел/не нашел (bool)
        """
        try:
            self.find_element("//div[@class='mini-suggest__popup mini-suggest__popup_svg_yes mini-suggest__popup_theme_flat mini-suggest__popup_visible']")
        except NoSuchElementException:
            return False
        return True

    def list_href(self):
        """
        Получение первых 5 ссылок в результатах

        Возвращает:
        list_href - лист ссылок
        """
        list_href = []
        elems = self.find_elements("//*[@id='search-result']/li/div/h2/a")
        count=0                           
        for item in elems:            
            list_href.append(item.get_attribute("href"))
            count += 1
            if count == 5:
                break
        return list_href

    def press_enter(self):
        """
        Нажатие на ENTER для получения результатов поиска
        """
        self.search_field.send_keys(Keys.ENTER)
    
    