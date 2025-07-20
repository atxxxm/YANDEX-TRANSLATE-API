# YANDEX TRANSLATE API

## Данный модуль предоставляет две функции для перевода текста с помощью Яндекс Переводчика
- async_yandex_translate_api — асинхронная версия
- yandex_translate_api — синхронная версия

## Требуемые библиотеки:
- playwright
- asyncio (для асинхронной версии)

## Установка Playwright:
```pip install playwright```
```playwright install```

## Импорт:
```from YANDEX_TRANSALTE_API import yandex_translate_api, async_yandex_translate_api```

## Описание функций:
```async def async_yandex_translate_api(text: str, from_lang: str, to_lang: str) -> str - Асинхронный перевод текста с одного языка на другой через Яндекс Переводчик.```

```def yandex_translate_api(text: str, from_lang: str, to_lang: str) -> str - Синхронный перевод текста с одного языка на другой через Яндекс Переводчик.```

## Параметры:

- text (str): Текст для перевода.
- from_lang (str): Язык исходного текста (например, 'ru' — русский).
- to_lang (str): Язык, на который нужно перевести (например, 'en' — английский).

## Возвращаемое значение:
- Переведённый текст (str), либо строка "No text" в случае неудачи.

## Пример использования:

### Синхронно
```result = yandex_translate_api("Привет, мир!", "ru", "en")```
```print(result)```

### Асинхронно
```import asyncio```
```result = asyncio.run(async_yandex_translate_api("Привет, мир!", "ru", "en"))```
```print(result)```

## Доступные языки
- ru — русский
- en — английский
- de — немецкий
- fr — французский
- es — испанский
- it — итальянский
- uk — украинский
- pl — польский
- tr — турецкий
- ar — арабский
- zh — китайский
- ja — японский
- ko — корейский
- vi — вьетнамский
- hi — хинди
- bn — бенгальский
- mr — маратхи
- pa — панджаби
- te — телугу
- th — тайский
- id — индонезийский
- ms — малайский
- nl — голландский
- sv — шведский
- no — норвежский
- fi — финский
- cs — чешский
- ro — румынский
- hu — венгерский
- da — датский
- el — греческий
- ca — каталонский
- sq — албанский
- et — эстонский
- lv — латвийский
- lt — литовский
- sr — сербский
- hr — хорватский
- sk — словацкий
- sl — словенский
- mt — мальтийский
