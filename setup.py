from setuptools import setup

setup(
    name="klein",
    version="0.1.0",
    description="werkzeug + twisted.web",
    packages=["klein"],
    test_suite="klein",
    setup_requires=['setuptools_trial'],
    install_requires=["Twisted", "werkzeug", "mock", "Flask"]
)
