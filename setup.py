from setuptools import setup, find_packages


setup(
    version="0.0.1",
    name="uci-class",
    long_description="Data loaders for UCI classification datasets.",
    url="https://github.com/ivan-chai/uci-class",
    author="Ivan Karpukhin",
    author_email="karpuhini@yandex.ru",
    packages=find_packages(include=["uci_class", "uci_class.*"]),
    install_requires=[
        "openpyxl",
        "pandas",
        "numpy>=1.12.0",
        "scikit-learn>=0.24.2",
        "torch>=1.10.2",
        "tqdm",
        "xlrd"
    ]
)
