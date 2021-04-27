from Yandex_Search import SearchHelper

def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    check = yandex_main_page.search_field()
    assert check == True, "Нет поля поиска"
    yandex_main_page.enter_word('Тензор')
    check = yandex_main_page.check_suggest()
    assert check == True, "Таблица с подсказками не появилась"   
    yandex_main_page.press_enter()
    list_href = yandex_main_page.list_href()
    result_href = list(filter(lambda x: 'tensor.ru' in x, list_href))
    assert len(result_href) > 0, "В первых 5 ссылках нет ссылки на tensor.ru"




    