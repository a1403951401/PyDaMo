import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyDaMo",
    version="0.1.0",
    author="Martin",
    author_email="1403951401@qq.com",
    description="Interop.SHDocVw",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://code.aliyun.com/a1403951401/PyDaMo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
    ]
)