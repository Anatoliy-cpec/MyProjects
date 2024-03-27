from django import template


register = template.Library()


BAD_WORDS = [
   "огурец",
   "помидор",
   "редиска"
]


@register.filter()
def censor(value: str):
    try:
        if type(value) is str:
            for word in BAD_WORDS:
                if word in value:
                    value = value.replace(word, f"{word[0]}"+"*"*(len(word)-1))
                if word.capitalize() in value:
                    value = value.replace(word.capitalize(), f"{word.capitalize()[0]}"+"*"*(len(word)-1))
        else:
            raise ValueError
    except ValueError:
        print('error while filtering')
    finally:
        return value
