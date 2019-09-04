
from configparser import (
    ConfigParser,
    NoOptionError,
    NoSectionError
)


class ParseConfig(ConfigParser):
    """解析配置文件"""
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.read(self.filename, encoding='utf-8')

    def get_option_value(self, section, option=None):
        """get value of section with option"""
        try:
            if option is None:
                value = dict(self[section])
                return value
            value = self.get(section, option)
            if '->' in value:
                value = tuple(value.split("->"))
            return value
        except (NoOptionError, NoSectionError) as e:
            raise e

    def __call__(self, *args, **kwargs):
        return self.get_option_value(*args, **kwargs)


if __name__ == '__main__':
    from config.config import LOCATOR_PATH

    locator = ParseConfig(LOCATOR_PATH)
    username_input = locator('LoginPage', 'username_input')
    print(username_input)
