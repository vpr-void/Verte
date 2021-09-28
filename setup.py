import cx_Freeze
from cx_Freeze import *

setup(

	name = "Lee",
	options = {'build_exe' : {'packages' : ['pygame']}},
	executables = [
		Executable("platf.py",)
	]

	)