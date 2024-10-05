from paramiko import SSHClient, AutoAddPolicy, ssh_exception
from ..utils.utils import print_value
from ssh_credentials import SshCredentials


class SshClient:
  """
  Wraps ssh operations
  """

  def __init__(self, ssh_credentials: SshCredentials):
    self.ssh_credentials = ssh_credentials
    self.ssh = SshClient.__create_ssh_client(ssh_credentials)


  def close(self):
    self.ssh.close()


  def list_files(self, directory: str, filename_pattern: str) -> list[str]:
    """
    List files that match the filename_pattern in the given directory
    :param directory:
    :param filename_pattern:
    :return: list of files
    """

    try:
      stdin, stdout, stderr = self.ssh.exec_command("ls " + directory)
      files = stdout.read().split()
      files_str = []

      for file in files:
        file_str = str(file, "utf-8")
        if filename_pattern in file_str:
          files_str.append(file_str)

      return files_str

    except ssh_exception.SSHException as e:
      print_value("SSHException was thrown while listing files in the directory: [" + directory + "]")
      return []

    except Exception as e:
      print_value("An exception thrown while listing files in the directory: [" + directory + "]")
      raise e


  @staticmethod
  def __create_ssh_client(self, ssh_credentials: SshCredentials) -> SSHClient:
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())

    # If we ignore the empty password, the library will fail to connect
    client.connect(hostname=ssh_credentials.host, username=ssh_credentials.username, password="")

    if client.get_transport().active:
      print_value(f"Connected to the remote machine: [{ssh_credentials.get_ssh_line()}]")
      return client

    raise Exception("SSH connection failed.")