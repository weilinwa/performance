'''
pre-command
'''
import sys
import os
from performance.logger import setup_loggers
from shared.precommands import PreCommands
from shared import const

setup_loggers(True)
precommands = PreCommands()
precommands.existing(os.path.join(sys.path[0], const.SRCDIR), os.path.join('WpfLarge', 'WpfLarge.csproj'))
precommands.execute()