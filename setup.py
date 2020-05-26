#! /usr/bin/env python
import pathlib

import setuptools

subpackage_name = "example"


def read_version():
    root_path = pathlib.Path(__file__).parent
    version_path = root_path / "abjadext" / subpackage_name / "_version.py"
    with version_path.open() as file_pointer:
        file_contents = file_pointer.read()
    local_dict = {}
    exec(file_contents, None, local_dict)
    return local_dict["__version__"]


if __name__ == "__main__":
    setuptools.setup(
        author="Josiah Wolf Oberholtzer",
        author_email="josiah.oberholtzer@gmail.com",
        classifiers=[
            "Development Status :: 3 - Alpha",
            "License :: OSI Approved :: GNU General Public License (GPL)",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: Implementation :: CPython",
            "Topic :: Artistic Software",
        ],
        extras_require={
            "test": [
                "black",
                "flake8",
                "isort",
                "mypy >= 0.660",
                "pytest >= 4.1.0",
                "pytest-cov >= 2.6.0",
                "pytest-helpers-namespace",
            ]
        },
        include_package_data=True,
        install_requires=["abjad >= 3.1"],
        license="MIT",
        long_description=pathlib.Path("README.md").read_text(),
        keywords=", ".join(
            [
                "music composition",
                "music notation",
                "formalized score control",
                "lilypond",
                "documentation",
                "cli",
            ]
        ),
        name="abjad-ext-{}".format(subpackage_name),
        packages=["abjadext"],
        platforms="Any",
        url="http://www.projectabjad.org",
        version=read_version(),
    )
