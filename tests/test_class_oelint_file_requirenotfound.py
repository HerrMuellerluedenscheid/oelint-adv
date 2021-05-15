import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from base import TestBaseClass

class TestClassOelintRequireNotFound(TestBaseClass):

    @pytest.mark.parametrize('id', ['oelint.file.requirenotfound'])
    @pytest.mark.parametrize('occurance', [1])
    @pytest.mark.parametrize('input', 
        [
            {
            'oelint_adv_test.bb':
            '''
            require oelint_adv_test.inc
            '''
            }
        ],
    )
    def test_bad(self, input, id, occurance):
        self.check_for_id(self._create_args(input), id, occurance)

    @pytest.mark.parametrize('id', ['oelint.file.requirenotfound'])
    @pytest.mark.parametrize('occurance', [0])
    @pytest.mark.parametrize('input', 
        [
            {
            'oelint_adv_test.bb':
            '''
            require oelint_adv_test.inc
            '''
            ,
            'oelint_adv_test.inc':
            '''
            VAR = "a"
            '''
            }
        ],
    )
    def test_good(self, input, id, occurance):
        self.check_for_id(self._create_args(input), id, occurance)