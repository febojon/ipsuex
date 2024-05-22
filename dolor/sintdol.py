from typing import Union, List
from selenium.webdriver.remote.webdriver import WebDriver

def switch_to_window(driver: WebDriver, handles: Union[str, List[str]]):
    if isinstance(handles, str):
        # If handles is a single string, switch to that window directly
        driver.switch_to.window(handles)
    elif isinstance(handles, list):
        # If handles is a list, loop through the handles and switch to each one
        for handle in handles:
            driver.switch_to.window(handle)
    else:
        raise ValueError("handles must be a string or list of strings")

# Example usage:
# driver is your instance of WebDriver
current_handles = driver.window_handles  # Get the list of all window handles
switch_to_window(driver, current_handles[1])  # Switch to the second window
