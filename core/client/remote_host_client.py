from rsync_client import RsyncClient
from ssh_credentials import SshCredentials
from ssh_client import SshClient


class RemoteHostClient:
  """
  Used to connect to the remote host via ssh / rsync and copy files and directories to the local machine.
  """

  def __init__(self, ssh_credentials: SshCredentials):
    self.ssh_credentials = ssh_credentials
    self.ssh = SshClient(ssh_credentials)
    self.rsync = RsyncClient(ssh_credentials)


  def get_file(self, source_file: str, destination_file: str) -> None:
    self.rsync.get_file(source_file, destination_file)


  def get_directory(self, source_directory: str, destination_directory: str) -> None:
    self.rsync.get_directory(source_directory, destination_directory)


  def list_files(self, directory: str, filename_pattern: str) -> list[str]:
    return self.ssh.list_files(directory, filename_pattern)


  def close(self):
    self.ssh.close()