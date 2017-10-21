from setuptools import setup
setup (name = 'fake_typing',

    install_requires =['keyboard==0.11.0+git8a7df3d'],
    version ='1.1',
    dependency_links = ['https://github.com/HQupgradeHQ/keyboard/archive/8a7df3d29d58f2b873a288722b3935382819fb0d.zip#egg=keyboard-0.11.0+git8a7df3d'],
    scripts =['script.py'],
)
