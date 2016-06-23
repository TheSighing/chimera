from distutils.core import setup

setup(
        # Application name:
        name="climber",

        # Version number (initial):
        version="0.1.1",

        # Application author details:
        author="Jared Godfrey",
        author_email="jared.yusef@gmail.com",

        # Packages
        packages=["climber"],

        # Include additional files into the package
        include_package_data=True,

        # Details
        url="http://pypi.python.org/pypi/climber_v010/",

        #
        # license="LICENSE.txt",
        description="Climb wiki pages..",

        # long_description=open("README.txt").read(),

        # Dependent packages (distributions)
        install_requires=[
            "flask",
            ],
        )
