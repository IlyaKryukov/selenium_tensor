from BaseApp import BasePage
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class YandexSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = "//input[@name='text']"
    

class SearchHelper (BasePage):

    def search_href_images(self):
        """
        Поиск на главной странице ссылки на 'Картинки'

        Возвращает:
        True/False - нашел/не нашел (bool)
        """
        try:
            images = self.find_element("//a[@data-id='images']")
            self.images = images
        except NoSuchElementException:
            return False
        return True
    
    def click_images(self):
        """
        Открытие вкладки 'Картинки'
        """
        self.images.click()
        self.open_images_tab()
        
    def open_first_category(self):
        """
        Открытие первой категории с сохранением названия категории
        """
        category_images = self.find_element("//div[@data-grid-name='im']")
        text_search = self.text("//div[@class='PopularRequestList-SearchText']")
        self.text_search = text_search 
        category_images.click()

    def text_in_search(self): 
        """
        Получение содержимого поисковой строки с сохранением текта поиска 
        """
        sleep(2)
        input_field = self.find_element("//span[@class='input__box']")
        input_field.click()
        search = self.text("//span[@class='suggest2-item__text']")
        self.text_after_search = search
        self.find_element("//span[@class='suggest2-item__text']").click()
        sleep(2)

    def click_first_image(self):
        """
        Открытие первого изображения

        Возвращает:
        image - ссылка на картинку (string)
        """
        self.find_element("//a[@class='serp-item__link']").click()        
        sleep(1)
        image = self.get_photo_link("//img[@class='MMImage-Origin']")
        return image

    def next_image(self):
        """
        Открытие следующего изображения с помощью кнопки вперед

        Возвращает:
        image - ссылка на картинку (string)
        """
        self.find_elements("//i[@class='CircleButton-Icon']")[-1].click()
        sleep(1)
        image = self.get_photo_link("//img[@class='MMImage-Origin']")
        return image

    def return_image(self):
        """
        Открытие предыдущего изображения с помощью кнопки назад

        Возвращает:
        image - ссылка на картинку (string)
        """        
        self.find_elements("//i[@class='CircleButton-Icon']")[0].click()
        sleep(1)
        image = self.get_photo_link("//img[@class='MMImage-Origin']")
        return image

   
        
        

