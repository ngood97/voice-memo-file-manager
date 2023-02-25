from pathlib import Path
from typing import Iterator

class AudioMemoDirectory(Iterator):
	def __init__(self, memo_dir: Path):
		# avoid dot underscore files
		self.current_file_iter = memo_dir.glob('*')

	def __next__(self):
		return AudioMemo(next(self.current_file_iter))

class AudioMemo:
	def __init__(self, filepath: Path):
		self.filepath = filepath

	def play(self):
		print(f'playing file {self.filepath}!')

	def delete(self):
		print(f'deleting file {self.filepath}')