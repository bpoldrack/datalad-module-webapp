#!/usr/bin/env python

from setuptools import setup

setup(
    # basic project properties can be set arbitrarily
    name="datalad_webapp",
    author="The DataLad Team and Contributors",
    author_email="team@datalad.org",
    version='0.1',
    description="DataLad extension for exposing commands via a web request API",
    # datalad command suite specs from here
    install_requires=[
        # in general datalad will be a requirement, unless the datalad extension
        # aspect is an optional component of a larger project
        'datalad',
    ],
    entry_points = {
        'datalad.modules': [
            'webapp=datalad_webapp:module_suite',
        ],
        # 'datalad.webapps' is THE entrypoint inspected by the datalad webapp command
        'datalad.webapps': [
            # the label in front of '=' is the webapp name
            # the entrypoint can point to any symbol of any name, as long it is
            # valid datalad interface specification
            'example_metadata=examples.metadata.app:MetadataAppExample',
        ]
    },
)
