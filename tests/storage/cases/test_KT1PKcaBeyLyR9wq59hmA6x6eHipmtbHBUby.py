from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline, micheline_to_michelson


class StorageTestKT1PKcaBeyLyR9wq59hmA6x6eHipmtbHBUby(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.contract = get_data('storage/carthagenet/KT1PKcaBeyLyR9wq59hmA6x6eHipmtbHBUby.json')

    def test_storage_encoding_KT1PKcaBeyLyR9wq59hmA6x6eHipmtbHBUby(self):
        type_expr = self.contract['script']['code'][1]
        val_expr = self.contract['script']['storage']
        schema = build_schema(type_expr)
        decoded = decode_micheline(val_expr, type_expr, schema)
        actual = encode_micheline(decoded, schema)
        self.assertEqual(val_expr, actual)

    def test_storage_schema_KT1PKcaBeyLyR9wq59hmA6x6eHipmtbHBUby(self):
        _ = build_schema(self.contract['script']['code'][0])

    def test_storage_format_KT1PKcaBeyLyR9wq59hmA6x6eHipmtbHBUby(self):
        _ = micheline_to_michelson(self.contract['script']['code'])
        _ = micheline_to_michelson(self.contract['script']['storage'])
