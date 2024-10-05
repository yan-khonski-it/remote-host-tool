import subprocess
from ssh_credentials import SshCredentials
from ..utils.utils import print_value


class RsyncClient:
  """
  Downloads files (for example logs or config files) from a remote server using rsync.
  """

  def __init__(self, ssh_credentials: SshCredentials):
    self.ssh_credentials = ssh_credentials


  def get_file(self, source_file: str, destination_file: str) -> None:
    """
    Downloads a file from remote server.
    :param source_file: source file on the remote server
    :param destination_file: destination file on the local machine. For example, "/Downloads/my-file.txt".
    """

    print_value(f"Downloading from remote machine: [{self.ssh_credentials.host}]" +
                f" source file: [{source_file}] to destination directory: [{destination_file}].")
    subprocess.call(f"rsync --timeout=300 --compress {self.ssh_credentials.get_ssh_line()}:{source_file} {destination_file}".split())


  def get_directory(self, source_directory: str, destination_directory: str) -> None:
    """
    Downloads directory from remote server. Destination directory does not have to exist - it will be created.
    :param source_directory:
    :param destination_directory:
    """

    print_value(f"Downloading from remote machine: [{self.ssh_credentials.host}]" +
                f" source directory: [{source_directory}] to destination: [{destination_directory}].")
    subprocess.call(f"rsync -av --timeout=600 --compress {self.ssh_credentials.get_ssh_line()}:{source_directory} {destination_directory}".split())