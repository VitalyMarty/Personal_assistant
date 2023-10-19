from setuptools import setup, find_packages

setup(
    name="tough_assistant",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    author="Vitaly Martynenko, Savenko Vitalii, Andrii Kononov, Symbirtsev Serhii, Bohdan Turkot",
    description="This Bot-Assistant help you manage you adressbook and notebook, also can sort files and folder",
    entry_points={'console_scripts': ['assistant = tough_assistant.main:main']},
    install_requires=[
        'prompt_toolkit'
        ],
)
