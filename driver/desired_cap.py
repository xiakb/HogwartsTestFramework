import yaml
from appium import webdriver


def get_data(filepath):
    """
    读取指定的文件信息
    :param filepath: 需要读取的文件路径
    :return: 返回读取的文件
    """
    with open(filepath, 'rb') as file:
        data = file.read()
        result = yaml.safe_load(data)
    return result


def desired_cap():
    """
    启动对应APP
    :return: driver
    """
    data = get_data("../data/desired_caps.yaml")
    # 启动app参数
    desired_caps = {
        'platformName': data['platformName'],
        'platformVersion': data['platformVersion'],
        'deviceName': data['deviceName'],
        'noReset': data['noReset'],
        # 'unicodeKeyboard': data['unicodeKeyboard'],
        # 'resetKeyboard': data['resetKeyboard'],
        # 'dontStopAppOnReset': data['dontStopAppOnReset'],
        # 'settings[waitForIdleTimeout]': data['settings[waitForIdleTimeout]'],
        'appPackage': data['appPackage'],
        'appActivity': data['appActivity'],
        'newCommandTimeout': data['newCommandTimeout']
    }

    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)
    return driver


if __name__ == '__main__':
    desired_cap()
