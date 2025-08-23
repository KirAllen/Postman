import json

import requests
from postman.secrects import y_key

def generation_letter(title: str = "мамкин программист", description: str ="программировать мамок"):
    prompt = {
        "modelUri": "gpt://b1goa28uo5i40028s8m8/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": "ты очень необычный рекрутер, который обожает писать интересные пиcьма кандидатам с анекдотичными вставками."
                        "Тебе от 40 до 65 лет, тебя зовут Гога, ты этнический грузин, поэтому в твоей речи часто встречается слова 'Вай', "
                        " 'канешно, дорогой' и прочие грузинские обороты."
                        "Письма твои изобилуют двуссмысленными намеками ну вот прям совсем на грани приличия и к тому же еще испольуешь разного рода уловки, "
                        "чтобы заманить кандидата ответить на письмо или приехать к тебе на шашлыки. В своем письме ты используешь разного рода отсылки и аналогии, связанные с названием и описанием вакансии"
                        "и старыми грузинскими анекдотами"
            },
            {
                "role": "user",
                "text": f"Привет, рекрутер! Мне нужна твоя помощь, чтобы ты написал оригинальное письмо кандидату и пригласил его на собеседование на позицию {title}, содержание вакансии: {description}"
            }
        ]
    }

    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'
    headers = {
        "Content-Type": "application/json",
        "Authorization": y_key
    }

    response = requests.post(url, headers=headers, json=prompt)
    result_generation = response.json()
    return result_generation['result']['alternatives'][0]['message']['text']


