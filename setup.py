# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
import io
from setuptools import setup

def long_description():
    with io.open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme

setup(name='qunix-tools',
    version='0.1.1',
    description='Library of unix-like python programs related to Qiskit',
    long_description=long_description(),
    url='https://github.com/echo724/qcb',
    author='qunix',
    author_email='eunchan1001@gmail.com',
    license='Apache License 2.0',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        ],
    scripts=['bin/qcb','bin/alea'],
    zip_safe=False)