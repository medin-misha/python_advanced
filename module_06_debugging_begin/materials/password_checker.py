import getpass
import hashlib
import logging


logger = logging.getLogger("passwordLogger")

def input_and_check_password(
        number_count:int,
        _true_password:str
) -> bool:
    logger.debug("запрос на вход в программу")
    user_password_input:str
    try:
        for i in range(1, number_count + 1):
            logger.debug("запрос на пароль")

            user_password_input:str = input(
                f"попытка {i}\nВведите пароль: "
            )


            if _true_password == user_password_input:
                logger.warning("пользователь ввёл правильный пароль")
                return True
            elif not user_password_input:
                logger.info(f"пользователь ввёл пустой пароль попыток использовано {i}")
                return False

            logger.info(f"пользователь ввёл не правильный пароль")
            print(f"не правильный пароль, попыток использовано {i} из {number_count}")

        else:
            raise ValueError

    except (ValueError):
        logger.error("Пользователь ввёл не правильный пароль 3 раза")
        return False

    except:
        logger.error("произошла неизвесная ошбка")
        return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename="password_checker.log")

    count_number:int = 3
    password:str = "0301mishana"
    print(
        input_and_check_password(
            number_count=count_number,
            _true_password = password
        )
    )