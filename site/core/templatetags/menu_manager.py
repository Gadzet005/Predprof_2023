from django import template


class UserGroup:
    ''' Класс для деления пользователей на группы '''

    NotAuth = 1
    Auth = 2

    @classmethod
    def get_user_group(cls, user):
        if user.is_authenticated:
            return cls.Auth
        return cls.NotAuth


class MenuElem:
    def __init__(self, title, url_name=None, can_see=['all'], sub_elems=None):
        self.title = title
        self.url_name = url_name
        self.is_active = False
        ''' Список групп, которые могут видеть это элемент меню '''
        self.can_see = can_see
        self.sub_elems = sub_elems


main_menu = [
    MenuElem('На главную', 'common:home'),
    MenuElem('Каталог', 'catalog:list'),
    MenuElem('Аккаунт', can_see=[UserGroup.Auth], sub_elems=(
        MenuElem('Профиль', 'users:profile'),
        MenuElem('Выйти', 'users:logout'),
    )),
    MenuElem('Авторизация', can_see=[UserGroup.NotAuth], sub_elems=(
        MenuElem('Регистрация', 'users:register'),
        MenuElem('Вход', 'users:login'),
    )),
]


register = template.Library()


@register.inclusion_tag('header.html')
def get_main_menu(request):
    ''' Формируем меню '''
    menu = []
    for elem in main_menu:
        user_group = UserGroup.get_user_group(request.user)
        if user_group in elem.can_see or 'all' in elem.can_see:
            elem.is_active = elem.url_name == request.resolver_match.view_name

            if elem.sub_elems:
                for sub_elem in elem.sub_elems:
                    active = (
                        sub_elem.url_name == request.resolver_match.view_name
                        )
                    if active:
                        elem.is_active = True
                        break

            menu.append(elem)

    return {'menu': menu}
