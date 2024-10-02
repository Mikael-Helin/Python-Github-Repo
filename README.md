# Python Github Repo

Steps on how to create a pip repo on GitHub. You can pip install directly from a GitHub repo.

### Step 1: Create the Python Program

First, create a directory for your project and navigate to it:

```bash
mkdir hello_world
cd hello_world
```

Next, create a `hello.py` file with the following content:

```python
def say_hello():
    print("Hello, World!")
```

This is the program we want to import.

### Step 2: Create `setup.py`

Create a `setup.py` file in the project root directory. This file is required for packaging your Python project. Here’s a minimal example of what it should look like:

```python
from setuptools import setup

setup(
    name='hello_world_package',
    version='0.0.1',
    py_modules=['hello_world_package.hello'],  # Manually specify the module path i.e. hello_world_package/hello.py
    entry_points={
        'console_scripts': [
            'say_hello=hello_world_package.hello:say_hello',
        ],
    }
)
```

This `setup.py` file tells Python how to package the module, and the `entry_points` section makes your `say_hello` function accessible from the command line.

### Step 3: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository.
2. Name it something like `hello_world_package` (I named it `Python-Github-Repo`).
3. Follow the instructions on the page to push your code to the repository:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/Mikael-Helin/Python-Github-Repo.git
git push -u origin main
```

### Step 4: Install from GitHub using `pip`

To install the package from GitHub, you can use the following command:

```bash
mkdir example
cd example
python3 -m venv venv
source venv/bin/activate
python -m pip install -U pip setuptools 
python3 -m pip install git+https://github.com/Mikael-Helin/Python-Github-Repo.git
pip list
```

then create a program `hi.py`

```python
# packages are directories containing modules
# modules are the .py files containing your code
# from package_name import module_name
from hello_world_package import hello

hello.say_hello()
```

and run `python3 hi.py`.
