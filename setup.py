from setuptools import setup
setup (name = 'fake_typing',
    install_requires =['keyboard==0.11.0']
    version ='1',
    dependency_links = ['git+https://github.com/boppreh/keyboard@suppress#egg=keyboard-0.11.0'],
    scripts =['script.py'],
)
