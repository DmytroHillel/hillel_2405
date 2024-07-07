"""Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import pytest


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s - %(levelname)s'  #,
        # force=True
    )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)


# @pytest.mark.parametrize('status', ['success'])
# def test_log_param_success(status):
#     log_event('John', status)


def test_log_success():
    assert log_event('John', 'success')


def test_log_expired():
    assert log_event('Natalka', 'expired')


def test_log_error():
    assert AssertionError
    log_event('Vasyl', 'glvld')


@pytest.mark.parametrize('name, status, expected', [("Jonn", "success", "Login event - Username: John, Status: success")])
def test_success_log_2(name, status, expected):
    assert log_event(name, status) == expected
    with open("login_system.log", "r") as f:
        assert f"Login event - Username: {name}, Status: {status}" in f.read()
    # with open("login_system.log", "r") as f:
    #     assert f"Login event - Username: {param_1}, Status: {param_2}" == expected in f.read()

# def test_success_log_2():
#     log_event("John", "success")
#     with open("login_system.log", "r") as f:
#         assert "Login event - Username: John, Status: success" in f.read()
#
#
# def test_expired_log():
#     log_event("John", "expired")
#     with open("login_system.log", "r") as f:
#         assert "Login event - Username: John, Status: expired" in f.read()
#
#
# def test_failed_log():
#     log_event("John", "failed")
#     with open("login_system.log", "r") as f:
#         assert "Login event - Username: John, Status: failed" in f.read()
