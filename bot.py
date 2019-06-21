from automation import TaskManager, CommandSequence
import tempfile
import time
import os
import copy
import json
import pdb

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

EXTENSION_FOLDER = os.path.join(__location__,'automation/Extension')
EXTENSION = os.path.join(EXTENSION_FOLDER, "stealth_bot.xpi")
NUM_BROWSERS = 1

site = 'http://localhost:8080/'
config = "FX_nightly_67.0.1_64-bit_headful_mac_os_x_webdriver_v0.24.0"


manager_params, browser_params = TaskManager.load_default_params(NUM_BROWSERS)
manager_params['data_directory'] = './Restults/'
manager_params['log_directory'] = './Restults/'

browser_params[0]['headless'] = False  # Launch only browser 0 headless

manager = TaskManager.TaskManager(manager_params, browser_params)

command_sequence = CommandSequence.CommandSequence(site)
command_sequence.get(sleep=30)
#command_sequence.install_extension(EXTENSION)
command_sequence.fill_config(config, 5)
command_sequence.take_fingerprint(15)

manager.execute_command_sequence(command_sequence, index='**')
manager.close()