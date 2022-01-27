from importlib.metadata import entry_points
from setuptools import setup

setup(name='sys_info_comp30380',
      version='0.1',
      description='Software engineering system information practical 2',
    #   url='https://github.com/mithunumesan/comp30830_test/practical2',
      url = r"C:\Users\mithu\OneDrive\Documents\education\softwareengineering\practicals",
      author='Mithun',
      license='MIT',
      packages=['sys_info_comp30380'],
      entry_points={
        'console_scripts':['sys_info_comp30380=prac2.main:main']
      },
      zip_safe=False)