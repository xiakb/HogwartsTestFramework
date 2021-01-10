import time
import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


def get_yaml_data(filepath):
    """
    读取指定的文件信息 \n
    :param filepath: 需要读取的文件路径
    :return: 返回读取的文件
    """
    with open(filepath, 'rb') as file:
        data = file.read()
        result = yaml.safe_load(data)
    return result


def location_mode(mode):
    """
    定位方式 \n
    :param mode: 需要的定位方式
    :return: 指定的的定位方式
    """
    modes = [
        "by_id",
        "by_name",
        "by_class_name",
        "by_css_selector",
        "by_tag_name",
        "by_link_text",
        "by_partial_link_text",
        "by_xpath",
        "mobile_by_xpath",
        "mobile_by_css_selector"
    ]
    locate_modes = [
        By.ID,
        By.NAME,
        By.CLASS_NAME,
        By.CSS_SELECTOR,
        By.TAG_NAME,
        By.LINK_TEXT,
        By.PARTIAL_LINK_TEXT,
        By.XPATH,
        MobileBy.XPATH,
        MobileBy.CSS_SELECTOR
    ]
    for num in range(len(modes)):
        if mode == modes[num]:
            return locate_modes[num]


def get_time():
    """
    获取当前时间，并格式化输出 \n
    :return: 当前时间
    """
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    return now


def get_picture_data(picture_path):
    """
    读取图片文件 \n
    :param picture_path: 要读取的文件路径
    :return: 读取的文件
    """
    with open(picture_path, 'rb') as file:
        picture_data = file.read()
    return picture_data


