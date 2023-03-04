import argparse
from pathlib import Path
from audio_manager import AudioMemoDirectory
from InquirerPy import inquirer

def process_memo_directory(voice_memo_dir: Path):
	while True:
		audio_memo_dir = AudioMemoDirectory(voice_memo_dir)
		for audio_file in audio_memo_dir:
			print(f'Processing file {audio_file.filepath}')
			while True:
				next_action = inquirer.select(
					message="What action would you like to perform?",
					choices=[
						"play", "skip", "delete", "quit"
					],
				).execute()

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

	process_memo_directory(voice_memo_dir)



