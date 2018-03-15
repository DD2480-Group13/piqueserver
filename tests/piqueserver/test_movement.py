import mock
import unittest
import piqueserver.core_commands.movement as movement

class TestMovement(unittest.TestCase):
    def test_move_silent(self):
        connection = self.get_mock_connection()

        args = ("#0", 10, 11, 12)
        movement.move_silent(connection, *args)

        connection.set_location.assert_called_once_with((10, 11, 12))
        connection.protocol.send_chat.assert_not_called()

    # In movement.py, "position = args[0].upper()" should be "position = args[initial_index].upper()"
    @unittest.expectedFailure
    def test_move_sector(self):
        connection = self.get_mock_connection()

        args = ("#0", "a1")
        movement.move(connection, *args)

        connection.set_location.assert_called_once_with((32, 32, 32))
        connection.protocol.send_chat.assert_called_once_with("c teleported to location A1", irc=True)

    def test_move_x_y_z(self):
        connection = self.get_mock_connection()

        args = ("#0", 10, 11, 12)
        movement.move(connection, *args)

        connection.set_location.assert_called_once_with((10, 11, 12))
        connection.protocol.send_chat.assert_called_once_with("c teleported to location 10 11 12", irc=True)

    def get_mock_connection(self):
        connection = mock.Mock()
        connection.name = "c"
        connection.invisible = False
        connection.set_location = mock.Mock()
        connection.protocol = mock.Mock()
        connection.protocol.map.get_height.return_value = 34
        connection.protocol.send_chat = mock.Mock()
        connection.protocol.players = [connection]

        return connection

    
