from datetime import datetime

import random
import os
import time
import sys
import threading


def print_value(value: str) -> None:
  now_str = get_current_time_as_string()
  current_thread_name = threading.current_thread().name
  print(now_str + " | " + current_thread_name + " | " + value)


def convert_list_to_string(list_of_elements: list) -> str:
  """
  Converts a list to string
  """

  separator = "\n"
  return separator.join(map(str, list_of_elements))


def get_current_time_as_string() -> str:
  """
  Returns current time as string in format 2024-10-12T13-00-00. It could be used as filename or directory prefix.
  """

  now = datetime.now() # current date and time
  return str(now.strftime("%Y-%m-%dT%H-%M-%S"))


def get_current_time_as_string_with_random_suffix() -> str:
  """
  Returns current time as string with random one digit suffix. It could be used as filename or directory prefix.
  """

  now_str = get_current_time_as_string()
  return now_str + "--" + str(random.randint(0, 9))


def create_directory(directory_path: str) -> None:
  """
  Creates directory
  """

  os.makedirs(directory_path)


def create_directory_if_not_exists(directory_path: str) -> None:
  """
  Creates directory if it does not exist.
  """

  if not os.path.exists(directory_path):
    create_directory(directory_path)


def get_user_home_directory() -> str:
  return os.path.expanduser("~")


def get_script_path() -> str:
  return os.path.dirname(os.path.realpath(sys.argv[0]))


def calculate_time(func):
  """
  Used as a decorator around a function to measure time that the function invocation takes.
  It prints take time into console.
  """

  def inner1(*args, **kwargs):
    start_time = time.time()

    func(*args, **kwargs)

    end_time = time.time()
    total_time = end_time - start_time
    total_time_str = str(total_time)

    print_value(f"Function: {func.__name__} took time: {total_time_str} seconds.")

  return inner1


def start_threads(threads: list[threading.Thread]) -> None:
  """
  Starts thread. Used when we want to parallelize tasks. Each thread runs a task.
  """

  for thread in threads:
    thread.start()


def join_threads(threads: list[threading.Thread]) -> None:
  """
  Waits until all the threads finish, then the caller thread will continue.
  """

  for thread in threads:
    thread.join()


if __name__ == "__main__":
  raise Exception("Utils module should not be initialized.")
