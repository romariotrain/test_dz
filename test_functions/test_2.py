import pytest

import yandex

def test_create_file():
    result = yandex.ya.create_file('lala')
    assert result == 201



