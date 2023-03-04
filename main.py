import argparse
from pathlib import Path
from audio_manager import AudioMemoDirectory
from InquirerPy import inquirer

from commands import ActionSource, UserInput

def process_memo_directory(action_source: ActionSource, memo_directory: AudioMemoDirectory):
	for audio_file in memo_directory:
		print(f'Processing file {audio_file.get_filepath()}')
		for next_action in action_source:
			if next_action == 'skip':
				break

			if next_action == 'delete':
				audio_file.delete()
				break

			if next_action == 'play':
				audio_file.play()

			if next_action == 'quit':
				return


if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		prog = 'voice-memo-file-manager',
		description = 'From a directory of voice memo files, this utility will allow you to go through and manage each one quickly and easily.'
	)

	parser.add_argument('voice_memo_dir', help='path to directory of voice memos to be managed')

	args: argparse.Namespace = parser.parse_args()

	voice_memo_dir: Path = Path(args.voice_memo_dir)

	try:
		next(voice_memo_dir.glob('*'))
	except StopIteration:
		print(f'WARNING: No files in directory {voice_memo_dir}')

	process_memo_directory(UserInput(), AudioMemoDirectory(voice_memo_dir))

	print(f'Reached the end of the directory...')
