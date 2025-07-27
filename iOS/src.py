from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class Helper:
    def __init__(self, driver):
        self.driver = driver

    def swipe_left_on_element(self, element, distance):
        location = element.location
        size = element.size

        start_x = location['x'] + size['width'] - 5
        start_y = location['y'] + size['height'] // 2
        end_x = start_x - distance
        end_y = start_y

        finger = PointerInput("touch", "finger")
        actions = ActionBuilder(self.driver, mouse=finger)

        actions.pointer_action.move_to_location(start_x, start_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pause(0.2)
        actions.pointer_action.move_to_location(end_x, end_y)
        actions.pointer_action.pointer_up()

        actions.perform()

    def swipe_right_on_element(self, element, distance):
        location = element.location
        size = element.size

        start_x = location['x'] + size['width'] - 5
        start_y = location['y'] + size['height'] // 2
        end_x = start_x
        end_y = start_y - distance

        finger = PointerInput("touch", "finger")
        actions = ActionBuilder(self.driver, mouse=finger)

        actions.pointer_action.move_to_location(start_x, start_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pause(0.2)
        actions.pointer_action.move_to_location(end_x, end_y)
        actions.pointer_action.pointer_up()

        actions.perform()
