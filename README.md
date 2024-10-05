# remote-host-tool
Collect logs, configuration files and setting from remote host via ssh.

> Note, these tools originally created for mac and linux. You may require modification to work on Windows.

## Installation
Clone
```shell
git clone https://github.com/yan-khonski-it/remote-host-tool.git
```

Create a virtual environment
```shell
python -m venv virtual_environment 
```

Activate the virtual environment
```shell
.\virtual_environment\Scripts\activate
```

The output will be:
```shell
(virtual_environment) PS {PATH}\remote-host-tool>
```

To deactivate the virtual environment https://stackoverflow.com/questions/990754/how-to-leave-exit-deactivate-a-python-virtualenv
```shell
deactivate
```

<details>
  <summary>Create a virtual environment on Mac</summary>

#### Mac
Follow this link
- https://github.com/yan-khonski-it/dev-utils/blob/master/README.md

Or this one the original source
- https://mnzel.medium.com/how-to-activate-python-venv-on-a-mac-a8fa1c3cb511

</details>

Install requirements
```shell
pip install -r ./requirements.txt
```

## How it works
Under the hood, it uses ssh, spc and rsync commands to download files from the remote host.
Examples:
spc
```shell
scp user@168.12.13.14:/yan-files/my-service.log /Users/yan/analized-logs/case1/
```

rsync a file, you have to include the filename in the destination path:
```shell
rsync --timeout=300 --compress user@168.12.13.14:/yan-files/my-service.log /Users/yan/analized-logs/case1/my-service.log
```

rsync a directory (it will create the destination directory on the local machine if it was not created before):
> Note, when copying a directory, the destination path should end with a slash, so it is treated as a directory.
```shell
rsync -av --timeout=600 --compress user@168.12.13.14:/yan-files /Users/yan/analized-logs/case1/
```

### Parameters:

https://www.oreilly.com/library/view/linux-pocket-guide/9780596806347/re80.html

- `--timeout` I use it, so the command will fail if the file is not downloaded within this time.
If the connection is slow, I'd rather fail faster and retry.
- `--compress` It allows to transfer files faster due to reducing their payload in the network.
Otherwise, it may fail with timeout for large files.
- `-a` Copies files attributes.
- `-v` Verbose mode: print information about what’s happening during the copy.

## Other notes
If rsync fails with timeout, you can increase it in the source code.
Additionally, you can add these lines into the server ssh_config file:

**/etc/ssh/ssh_config**

```text
KeepAlive yes
ServerAliveInterval 20
ServerAliveCountMax 6
```

https://unix.stackexchange.com/questions/68775/rsync-timed-out

In the past, I used a library
https://pypi.org/project/scp/

but I decided to write a bit of code to call rsync because for some reasons for large files scp fails,
and you cannot continue where you failed last time.