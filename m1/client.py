import socket as socket_lib


class Client:

    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port

    def send_command(self, cmd):
        """
        Sends command.
        Closes socket after sending command.

        :param cmd: stringified JSON command
        :except: Throws RuntimeError if operation fails, for instance if server socket is closed
        """

        # TODO Try not opening and closing to much TCP connections
        socket = socket_lib.socket(socket_lib.AF_INET, socket_lib.SOCK_STREAM)
        socket.connect((self.server_ip, self.server_port))
        total_sent = 0
        error = False

        if type(cmd) == str:
            _cmd = cmd.encode()
        elif type(cmd) == bytes:
            _cmd = cmd
        else:
            raise RuntimeError('Unsupported type {type} for cmd'.format(type=type(cmd)))

        total_sent = socket.send(_cmd[total_sent:])
        while total_sent < cmd.__len__() and not error:
            sent = socket.send(_cmd[total_sent:])
            if sent == 0:
                error = True
            total_sent = total_sent + sent
        socket.close()

        if error:
            raise RuntimeError("Socket connection broken")
