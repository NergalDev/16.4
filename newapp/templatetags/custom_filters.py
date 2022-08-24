from django import template

register = template.Library()  # если мы не зарегистрируем наши фильтры, то Django никогда не узнает,


@register.filter(name='Censor')
def Censor(value, arg):
    value = value.replace("охренеть", "В ШОКЕ")
    value = value.replace("афигенно", "ЗДОРОВО")
    value = value.replace("фигня", "ПЛОХО")
    return value


# прошлая версия, не используется
@register.filter(name='Censor1')
def Censor1(value, arg):  # первый аргумент здесь это то значение, к которому надо применить фильтр,
    # второй аргумент — это аргумент фильтра, т. е. примерно следующее будет в шаблоне value|multiply:arg
    if ("охренеть" in value) or ("афигенно" in value) or ("фигня" in value):
        arg = 'Вы используете плохие слова'
        return arg   # возвращаемое функцией значение — это то значение, которое подставится к нам в шаблон
    else:
        return value
