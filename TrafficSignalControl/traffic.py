from enum import Enum


class TrafficLight:
    """Represents an individual traffic light."""

    def __init__(self, id):
        self.id = id
        self.state = LightState.RED

    def change_state(self, state):
        self.state = state

    def print_state(self):
        print(f"Traffic Light {self.id}: {self.state.name}")


class LightState(Enum):
    """Enum for representing traffic light states."""

    RED = 1
    GREEN = 2
    YELLOW = 3


class IntersectionController:
    """Manages traffic lights at an intersection."""

    def __init__(self):
        self.traffic_lights = {}

    def add_traffic_light(self, light):
        self.traffic_lights[light.id] = light

    def change_signal(self, light_id, state):
        if light_id in self.traffic_lights:
            self.traffic_lights[light_id].change_state(state)

    def print_all_states(self):
        for light_id, light in self.traffic_lights.items():
            light.print_state()


class ControlPanel:
    """For manual control and emergencies."""

    def __init__(self, controller):
        self.controller = controller

    def override_signal(self, light_id, state):
        self.controller.change_signal(light_id, state)


class TrafficSignalSystem:
    """Main class managing the traffic signal system."""

    def __init__(self):
        self.intersection_controllers = []

    def add_intersection_controller(self, controller):
        self.intersection_controllers.append(controller)


def main():
    # Create an intersection controller
    controller = IntersectionController()

    # Add some traffic lights
    light1 = TrafficLight("Light 1")
    light2 = TrafficLight("Light 2")

    controller.add_traffic_light(light1)
    controller.add_traffic_light(light2)

    # Simulate a traffic light cycle (replace with timers in real use)
    controller.change_signal(light1.id, LightState.GREEN)
    controller.change_signal(light2.id, LightState.RED)

    controller.print_all_states()  # Print the current light states

    # Simulate yellow light transition (replace with timers)
    controller.change_signal(light1.id, LightState.YELLOW)

    controller.print_all_states()  # Print the updated light states


if __name__ == "__main__":
    main()
