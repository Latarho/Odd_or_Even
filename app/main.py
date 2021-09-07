from typing import List

from fastapi import FastAPI

app = FastAPI(title="Odd_or_Even")


@app.get("/even")
def check_even_number(number: int) -> dict:
    """Проверка целого числа на четность.
    Если число четное, то возвращается словарь вида {"result": "true"},
    если число нечетное, то возвращается словарь вида {"result": "false"}."""

    if number % 2 == 0:
        return {"result": "true"}
    else:
        return {"result": "false"}


@app.get("/odd")
def check_odd_number(number: int) -> dict:
    """Проверка целого числа на нечетность.
    Если число четное, то возвращается словарь вида {"result": "false"},
    если число нечетное, то возвращается словарь вида {"result": "true"}."""

    if number % 2 != 0:
        return {"result": "true"}
    else:
        return {"result": "false"}


@app.post("/even")
def check_even_list(numbers: List[int]) -> dict:
    """Проверка списка состоящего из целых чисел на четность.
    В результате возвращается словарь вида {"result": List[int]},
    значение которого содержит список из четных чисел."""

    only_even_list = [x for x in numbers if x % 2 == 0]
    return {"result": only_even_list}


@app.post("/odd")
def check_odd_list(numbers: List[int]) -> dict:
    """Проверка списка состоящего из целых чисел на нечетность.
    В результате возвращается словарь вида {"result": List[int]},
    значение которого содержит список из нечетных чисел."""

    only_odd_list = [x for x in numbers if x % 2 != 0]
    return {"result": only_odd_list}
