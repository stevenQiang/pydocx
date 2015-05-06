# coding: utf-8
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
)

from pydocx.openxml.packaging.open_xml_part import OpenXmlPart
from pydocx.openxml.wordprocessing.numbering import Numbering


class NumberingDefinitionsPart(OpenXmlPart):
    '''
    Represents the list numbering definitions within a document container.
    '''

    relationship_type = '/'.join([
        'http://schemas.openxmlformats.org',
        'officeDocument',
        '2006',
        'relationships',
        'numbering',
    ])

    NUM_FORMAT_UPPER_ROMAN = 'upperRoman'

    def __init__(self, *args, **kwargs):
        super(NumberingDefinitionsPart, self).__init__(*args, **kwargs)
        self._numbering = None

    @property
    def numbering(self):
        if not self._numbering:
            self.numbering = self.load_numbering()
        return self._numbering

    @numbering.setter
    def numbering(self, numbering):
        self._numbering = numbering

    def load_numbering(self):
        self.numbering = Numbering.load(self.root_element)
        return self.numbering
