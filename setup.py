import cx_Freeze
import  os.path
#from cx_Freeze import *

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
cx_Freeze.setup(
    name = "SpaceInvaders",
    options = {'build_exe': {'packages': ['pygame','numpy']}},
    executables = [cx_Freeze.Executable("SpaceInvaders.py",)]
)