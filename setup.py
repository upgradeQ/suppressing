from setuptools import setup
setup (name = 'fake_typing',

    install_requires =['keyboard==0.11.0+git.3483c57'],
    version ='1',
    dependency_links =['https://github.com/boppreh/keyboard/archive/3483c578cbd9105aae831bf1a47572b4d5bd5aff.zip#egg=keyboard-0.11.0+git.3483c57'],
    #dependency_links = ['https://github.com/boppreh/keyboard@suppress#egg=keyboard-0.11.0'],
    scripts =['script.py'],
)
