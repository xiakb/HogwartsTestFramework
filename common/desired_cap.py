from common.common_fun import *
from appium import webdriver


def desired_cap():
    """
    启动对应APP \n
    :return: common
    """
    data = get_yaml_data("../data/desired_caps.yaml")
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
