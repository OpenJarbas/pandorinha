from setuptools import setup

setup(
    name="pandorinha",
    version="0.0.1a2",
    description="discover music",
    license="",
    author="JarbasAi",
    url="https://github.com/OpenJarbas/pandorinha",
    packages=["pandorinha"],
    install_requires=[
        "pydora", "rapidfuzz", "json_database"
    ]
)
