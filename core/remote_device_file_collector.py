from core.client.remote_host_client import RemoteHostClient
from core.client.ssh_credentials import SshCredentials
from core.remote_server import RemoteServer
from core.utils.utils import calculate_time, create_directory


class RemoteDeviceFileCollector:
  """
  Collects logs, configuration files from remote server.
  """

  def __init__(self, remote_server: RemoteServer, destination_base_directory: str):
    self.ssh_credentials = SshCredentials(remote_server.ip)
    self.destination_base_directory = destination_base_directory


  @calculate_time
  def get_files(self) -> None:
    remote_host_client = RemoteHostClient(self.ssh_credentials)

    destination_logs_directory = self.destination_base_directory + "/logs"
    create_directory(destination_logs_directory)

    remote_host_client.get_file("/var/my-service/logs/catalina.log", destination_logs_directory + "/catalina.log")
    remote_host_client.get_file("/var/my-service/logs/tomcat.log", destination_logs_directory + "/tomcat.log")

    remote_host_client.get_file("/var/my-service/logs/my-service.log", destination_logs_directory + "/my-service.log")
    remote_host_client.get_directory("/var/my-service/logs/previous-logs", destination_logs_directory + "/previous-logs/")

    # TODO collect configuration files