from pydantic import BaseSettings, SecretStr


# класс для секретных данных (токенов бота, погоды, приема платежей и gpt), а так же
# id-шники админов бота
class Settings(BaseSettings):
    # Желательно использовать SecretStr для конфиденциальных данных
    bot_token: SecretStr
    admin_id: int
    api_token: SecretStr
    gpt_token: SecretStr
    pay_token: SecretStr

    # Вложенный класс с доп. указаниями для настройки
    class Config:
        # Имя файла, откуда будут прочитаны данные
        # (Относительно текущей рабочей директории)
        env_file = '.env'
        # Кодировка читаемого файла
        env_file_encoding = 'utf-8'


config = Settings()

if __name__ == "__main__":
    pass
