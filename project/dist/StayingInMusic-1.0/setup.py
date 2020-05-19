from distutils.core import setup

setup(name="StayingInMusic",
      version="1.0",
      scripts=["main.py"],
      py_modules=["main1", "main2"],
      packages=["modules",
                "data",
                ],
      )
