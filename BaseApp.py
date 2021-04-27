class BasePage:

    def __init__(self, driver):        
        self.driver = driver
        self.base_url = "https://yandex.ru/"

    def find_element(self, locator):
        """
        Поиск элемента по значению локатора

        Вход:
        locator - критерии для поиска элемента в виде xpath (string)
        """
        return self.driver.find_element_by_xpath(locator)

    def find_elements(self, locator):
        """
        Поиск элементов по значению локатора

        Вход:
        locator - критерии для поиска элементов в виде xpath (string)
        """
        return self.driver.find_elements_by_xpath(locator)

    def go_to_site(self):
        """
        Переход на базовую страницу
        """
        return self.driver.get(self.base_url)

    def open_images_tab(self):
        """
        Перелистывание вкладок до вкладки с картинками
        """
        for handle in self.driver.window_handles:
            self.driver.switch_to_window(handle)
            if 'images' in self.driver.current_url:
                break
    
    def current_url(self):
        """
        Получение текущего url
        """
        return self.driver.current_url

    def text(self, locator):
        """
        Получение текста определенного элемента

        Вход:
        locator - критерии для поиска элемента в виде xpath (string)
        """
        text = self.driver.find_element_by_xpath(locator).text
        return text

    def get_photo_link(self,locator):
        """
        Получение ссылки на изображение по локатору
        """
        return self.driver.find_element_by_xpath(locator).get_attribute("src")       
       

    
