import os
import signal
import subprocess
import pytest


@pytest.fixture(scope='module', autouse=True)
def record_vedio():
    """
    录视频 \n
    :return:
    """
    cmd = "scrcpy --record file.mp4"
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    yield
    os.kill(p.pid, signal.CTRL_C_EVENT)

