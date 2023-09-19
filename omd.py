# Guido van Rossum <guido@python.org>

def choose_options(text=None):
    """Provides interaction with user and checks if input is correct"""
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        if text:
            print('{} Выберите: {}/{}'.format(text, *options))
        else:
            print('Выберите: {}/{}'.format(*options))
        option = input()
    return options[option]


def step1():
    """Setup of story"""
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )

    if choose_options():
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    """Duck took an umbrella"""
    print('Естественно, дождя не было')

    if choose_options('Хотите узнать, что было бы, если бы не утка взяла зонт?'):
        return step2_no_umbrella()
    print('Ну ладно, пока!')


def step2_no_umbrella():
    """Duck didn't take an umbrella"""
    print('Из бара утка вышла только когда перестала видеть дождь')

    if choose_options('Хотите узнать, что было бы, если бы утка взяла зонт?'):
        return step2_umbrella()
    print('Ну ладно, пока!')


if __name__ == '__main__':
    step1()
