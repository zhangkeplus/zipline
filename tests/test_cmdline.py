import zipline.__main__ as main
from zipline.testing import ZiplineTestCase
from zipline.testing.predicates import (
    assert_equal,
    assert_raises_str,
)


class CmdLineTestCase(ZiplineTestCase):

    def init_instance_fixtures(self):
        super(CmdLineTestCase, self).init_instance_fixtures()

        main.extension_args = {}

        # make sure this starts empty
        assert_equal(main.extension_args, {})

    def test_parse_args(self):
        main._parse_extension_arg('arg1=test1')
        main._parse_extension_arg('arg2=test2')

        assert_equal(main.extension_args, {'arg2': 'test2', 'arg1': 'test1'})
        msg = 'invalid extension argument 1=test3, ' \
              'must be in key=value form'
        with assert_raises_str(ValueError, msg):
            main._parse_extension_arg('1=test3')
        msg = 'invalid extension argument arg4 test4, ' \
              'must be in key=value form'
        with assert_raises_str(ValueError, msg):
            main._parse_extension_arg('arg4 test4')