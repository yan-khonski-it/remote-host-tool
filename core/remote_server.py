class RemoteServer:
  """
  Represents a remote server with ip address.
  """

  def __init__(self, remote_server_config: dict[str, str]):
    self.name = remote_server_config["serverName"]
    self.ip = remote_server_config["ip"]
    self.skip = RemoteServer.resolve_skip(remote_server_config)


  def __str__(self) -> str:
    return f"Server name: {self.name}, ip: {self.ip}"


  @staticmethod
  def resolve_skip(remote_server_config: dict[str, str]) -> bool:
    skip_value = remote_server_config.get("skip")
    if skip_value is not None:
      return skip_value == True

    return False