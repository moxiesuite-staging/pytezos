from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline, micheline_to_michelson


class StorageTestKT1M8MStwA1R5SuGx2V6AMvgd8dGAFYcEUmu(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.contract = get_data('storage/zeronet/KT1M8MStwA1R5SuGx2V6AMvgd8dGAFYcEUmu.json')

    def test_storage_encoding_KT1M8MStwA1R5SuGx2V6AMvgd8dGAFYcEUmu(self):
        type_expr = self.contract['script']['code'][1]
        val_expr = self.contract['script']['storage']
        schema = build_schema(type_expr)
        decoded = decode_micheline(val_expr, type_expr, schema)
        actual = encode_micheline(decoded, schema)
        self.assertEqual(val_expr, actual)

    def test_storage_schema_KT1M8MStwA1R5SuGx2V6AMvgd8dGAFYcEUmu(self):
        _ = build_schema(self.contract['script']['code'][0])

    def test_storage_format_KT1M8MStwA1R5SuGx2V6AMvgd8dGAFYcEUmu(self):
        _ = micheline_to_michelson(self.contract['script']['code'])
        _ = micheline_to_michelson(self.contract['script']['storage'])
