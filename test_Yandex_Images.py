from Yandex_Images import SearchHelper

def test_yandex_images(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    check_href_images = yandex_main_page.search_href_images()
    assert check_href_images == True, "Отсутствует ссылка на картинки"
    yandex_main_page.click_images()
    url_images = yandex_main_page.current_url()
    assert 'https://yandex.ru/images/' in url_images, "Не был выполнен переход на https://yandex.ru/images/"
    yandex_main_page.open_first_category()
    yandex_main_page.text_in_search()
    text_search = str(yandex_main_page.text_search).lower()
    text_after_search = str(yandex_main_page.text_after_search).lower()
    assert text_search == text_after_search, "Неверный поиск категории"
    image_one = yandex_main_page.click_first_image()
    image_two = yandex_main_page.next_image()
    assert str(image_one) != str(image_two), "Картинка не изменилась при переходе вперед"
    image_return = yandex_main_page.return_image()    
    assert str(image_one) == str(image_return), "Картинки до перехода вперед и после возвращения назад различны"