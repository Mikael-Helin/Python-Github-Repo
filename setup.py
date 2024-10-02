from setuptools import setup

setup(
    name='hello_world_package',
    version='0.0.1',
    py_modules=['hello_world_package.hello'],  # Manually specify the module path
    entry_points={
        'console_scripts': [
            'say_hello=hello_world_package.hello:say_hello',
        ],
    }
)