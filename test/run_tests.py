
from __future__ import print_function

import platform
from unittest import main

# to add the win_unc pakage in parent directory
import sys, os
# for higher precedence:
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
# for lower precedence:
# sys.path += [os.path.dirname(os.path.dirname(__file__))]

from test_cleaners import *
from test_disk_drive import *
from test_net_use_table import *
from test_sanitizors import *
from test_utils import *
from test_unc_directory import *
from test_unc_credentials import *
from test_validators import *


if platform.system() == 'Windows':
    print('Including Windows-specific tests')
    from win_test_connecting import *
    from win_test_connecting_with_credentials import *
    from win_test_disk_drive import *
    from win_test_query import *
    from win_test_shell import *
else:
    print('WARNING: Excluding Windows-specific tests because host is not '
          'Windows')


if __name__ == '__main__':
    main()
