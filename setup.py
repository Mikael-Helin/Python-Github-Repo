from setuptools import setup

setup(
    name='hello_world_package',
    version='0.1',
    py_modules=['hello_world_package'],  # match the module file name
    entry_points={
        'console_scripts': [
            'say_hello=hello_world_package:say_hello',
        ],
    }
)