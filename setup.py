from setuptools import setup
setup (name = 'fake_typing',

    install_requires =['keyboard==0.11.0+git5196a01'],
    version ='1.1',
    dependency_links = ['https://github.com/HQupgradeHQ/keyboard/tree/5196a013bcc304cde509880ea9666fbde2ee081a.zip#egg=keyboard.0.11.0+git5196a01'],
   # dependency_links =['https://github.com/boppreh/keyboard/archive/3483c578cbd9105aae831bf1a47572b4d5bd5aff.zip#egg=keyboard-0.11.0+git.3483c57'],
    
    scripts =['script.py'],
)
