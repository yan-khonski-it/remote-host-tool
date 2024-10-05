import gzip
import os


def uncompress(root: str, filename: str) -> None:
  """
  Un-compresses a file with .gz filename extension.
  A new file is created without .gz extension. The original .gz file is removed.

  :param root: directory path where the imput .gz file is located.
  :param filename: input .gz file.
  """

  zipped_file_path = os.path.join(root, filename)
  output_filename = filename[0:len(filename) - 3] # filename without .gz extension
  output_file_path = os.path.join(root, output_filename)

  __unzip_file(zipped_file_path, output_file_path)


def __unzip_file(input_filename: str, output_filename: str) -> None:
  file_content = ""
  with gzip.open(input_filename, "rb") as input_f:
    file_content = input_f.read()

  with open(output_filename, "wb") as output_f:
    output_f.write(file_content)


  os.remove(input_filename)


if __name__ == "__main__":
  raise Exception("Utils module should not be initialized.")
