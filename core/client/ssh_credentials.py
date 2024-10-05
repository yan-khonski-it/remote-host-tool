DEFAULT_USER = "yan"


class SshCredentials:
  """
  Represents ssh credentials to connect to the remote machine. host is ip address of the machine.
  Password is not safe, so add the key to the remote machine.
  """

  def __init__(self, host: str, username: str = DEFAULT_USER):
    self.host = host
    self.username = username


  def __str__(self):
    return f"host: {self.host}, username: {self.username}"


  def get_ssh_line(self) -> str:
    """
    Returns ssh line to connect to the remote machine: user@<IP_ADDRESS>.
    """

    return f"{self.username}@{self.host}"