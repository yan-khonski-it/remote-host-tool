# An example program that runs remote_host_client
import json
import threading

from core.remote_device_file_collector import RemoteDeviceFileCollector
from core.remote_server import RemoteServer
from core.utils.utils import calculate_time, start_threads, join_threads, get_script_path, get_user_home_directory, create_directory_if_not_exists, \
  get_current_time_as_string_with_random_suffix, create_directory, print_value, convert_list_to_string


def parse_input(input_file: str) -> list[dict[str, str]]:
  with open(input_file, "r") as input_f:
    file_content = input_f.read()

  return json.loads(file_content)


def parse_remote_servers(input_file: str) -> list[RemoteServer]:
  remote_servers = []

  data = parse_input(input_file)
  for remote_server_config in data:
    remote_servers.append(RemoteServer(remote_server_config))

  return remote_servers


@calculate_time
def collect_files(remote_servers: list[RemoteServer], base_directory: str) -> None:
  thread_index = 0
  threads = []

  for remote_server in remote_servers:
    if remote_server.skip:
      continue

    remote_device_file_collector = RemoteDeviceFileCollector(remote_server, base_directory)

    thread_name = "Thread-" + str(thread_index) + "-" + remote_server.name
    thread = threading.Thread(target=remote_device_file_collector.get_files, name=thread_name)
    threads.append(thread)

    thread_index = thread_index + 1

  start_threads(threads)
  join_threads(threads)


def main() -> None:
  script_path = get_script_path()
  remote_servers = parse_remote_servers("/remote_servers-config.json")
  destination_root_directory = get_user_home_directory() + "/Downloads/my-remote-servers"
  create_directory_if_not_exists(destination_root_directory)

  now_str = get_current_time_as_string_with_random_suffix()
  base_destination_directory = destination_root_directory + "/" + now_str

  create_directory(base_destination_directory)

  print_value(f"Base directory: [{base_destination_directory}]\nList of remote servers:\n" + convert_list_to_string(remote_servers) + "\n")
  collect_files(remote_servers, base_destination_directory)


if __name__ == "__main__":
  main()
