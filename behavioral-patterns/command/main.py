# Command interface
class Command:
    def execute(self):
        pass

# Concrete Command classes
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

# Receiver class
class Light:
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")

# Invoker class
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

# Client code
if __name__ == "__main__":
    # Create a Light object (Receiver)
    light = Light()

    # Create Command objects
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    # Create an Invoker (RemoteControl) and set commands
    remote = RemoteControl()
    remote.set_command(light_on)

    # Press the button to turn the light on
    remote.press_button()

    # Change the command to turn the light off
    remote.set_command(light_off)

    # Press the button to turn the light off
    remote.press_button()
