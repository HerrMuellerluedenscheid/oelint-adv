import pytest

from .base import TestBaseClass


class TestClassOelintVarNativeSDKFilename(TestBaseClass):

    @pytest.mark.parametrize('id', ['oelint.var.nativesdkfilename'])
    @pytest.mark.parametrize('occurrence', [1])
    @pytest.mark.parametrize('input',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     'inherit nativesdk',
                                 },
                             ],
                             )
    def test_bad(self, input, id, occurrence):
        self.check_for_id(self._create_args(input), id, occurrence)

    @pytest.mark.parametrize('id', ['oelint.var.nativesdkfilename'])
    @pytest.mark.parametrize('occurrence', [0])
    @pytest.mark.parametrize('input',
                             [
                                 {
                                     'nativesdk-oelint-adv-test.bb':
                                     'inherit nativesdk',
                                 },
                             ],
                             )
    def test_good(self, input, id, occurrence):
        self.check_for_id(self._create_args(input), id, occurrence)
