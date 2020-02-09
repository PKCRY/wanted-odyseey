import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="wanted-odyssey"
    version="0.0.1",
    author="Nicholas Card",
    author_email="nickcard2000@gmail.com",
    url="https://github.com/yourusername/wanted-odyssey",
    description="wanted-odyseey is a text based space adventure game",
    long_description="will use python to make a text based adventure game with
    multiple mechanics such as a battle system and random encounters",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)

