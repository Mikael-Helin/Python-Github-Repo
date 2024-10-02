from setuptools import setup

setup(
    name='hello_world_package',
    version='0.0.1',
    py_modules=['hello'],
    entry_points={
        'console_scripts': [
            'say_hello=hello:say_hello',
        ],
    }
)