from cloudlink import cloudlink

class example_callbacks:
    def __init__(self, parent):
        self.parent = parent
class example_events:
    def __init__(self):
        pass

    async def on_close(self, client):
        print("Client", client.id, "disconnected.")

    async def on_connect(self, client):
        print("Client", client.id, "connected.")


class example_commands:
    def __init__(self, parent):
        self.parent = parent
        self.supporter = parent.supporter

        # If you want to have commands with very specific formatting, use the validate() function.
        self.validate = parent.validate

        # Various ways to send messages
        self.send_packet_unicast = parent.send_packet_unicast
        self.send_packet_multicast = parent.send_packet_multicast
        self.send_packet_multicast_variable = parent.send_packet_multicast_variable
        self.send_code = parent.send_code

    async def foobar(self, client, message, listener):
        print("Foobar!")

        # Reading the IP address of the client is as easy as calling get_client_ip from the server object.
        print(self.parent.get_client_ip(client))

        # In case you need to report a status code, use send_code.
        await self.send_code(
            client=client,
            code="OK",
            listener=listener
        )


if __name__ == "__main__":
    # Initialize Cloudlink. You will only need to initialize one instance of the main cloudlink module.
    cl = cloudlink()

    # Create a new server object. This supports initializing many servers at once.
    server = cl.server(logs=True)

    # Create examples for various ways to extend the functionality of Cloudlink Server.
    callbacks = example_callbacks(server)
    commands = example_commands(server)
    events = example_events()

    # Set the message-of-the-day.
    server.set_motd("WorldSprites", True)

    # Here are some extra parameters you can specify to change the functionality of the server.
    server.ip_blocklist = ["127.0.0.1"]
    server.reject_clients = False
    server.check_ip_addresses = True

    # Run the server.
    server.run(ip="0.0.0.0", port=3000)
