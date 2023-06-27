"""
Test custom Django management command
"""

from django.test import SimpleTestCase
from unittest.mock import patch

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTest(SimpleTestCase):
    """Test my wait_for_db command"""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for db if db ready"""
        pass

    def test_wait_for_db_delay(self):
        """Test waiting for db when getting OperationalError"""
        pass
