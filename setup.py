# Copyright 2022 CSIRO
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'version'), 'r') as vf:
    version = vf.read().strip()

setup(
    name='apsrm',
    description='A mulit-box model for assessing disease transmission risks',
    author='Simon Knapp',
    author_email='simon.knapp@csiro.au',
    version=version,
    python_requires='>=3',
    packages=find_packages(),
    include_package_data=True,
    scripts=[],
    install_requires=[
        "matplotlib",
        "networkx",
        "nptyping",
        "numpy",
        "scipy"],
    extras_require={
        "dev": [
            "autoflake",
            "ipython",
            "isort",
            "pre-commit",
            "pyinstrument",
            "pylint",
            "pytest",
            "sphinx",
            "sphinx-autodoc-typehints",
            "sphinx_readable_theme",
            "yapf"],
        "notebooks": [
            "jupyter",
            "pandas",
            "tqdm"]}
)
