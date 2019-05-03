import argparse
import sys
import re

def artifact_list(f):
	how_many_lines = -1
	artifacts = []
	for line in f:
		if how_many_lines < 0:
			match = re.match(r"The following (\d+) artifacts were generated during his adventure", line)
			if not match is None:
				number_of_artifacts = int(match.group(1))
				how_many_lines = number_of_artifacts
		elif how_many_lines > 0:
			artifacts.append(line.strip())
			how_many_lines -= 1
	return artifacts

class always_valid:
	def valid(self, number_of_artifacts):
		return True

class at_least_artifacts:
	def __init__(self, at_least):
		self.at_least = at_least
	def valid(self, number_of_artifacts):
		return number_of_artifacts >= self.at_least

if __name__ == "__main__":
	d = "Filters ADOM memorial file"
	parser = argparse.ArgumentParser(description=d, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument("-n", "--number", help="at least how many artifacts there must be to consider", type=int)
	parser.add_argument("-e", "--exclude_common", help="exclude artifacts present in all files", action="store_true", default=False)
	parser.add_argument("-l", "--list_file_names", action="store_true", default=False)
	parser.add_argument("files", nargs="*")
	args = parser.parse_args()

	validator = always_valid() if args.number is None else at_least_artifacts(args.number)

	file_to_artifacts = dict()
	for arg_f in args.files:
		with open(arg_f) as f:
			temp = artifact_list(f)
			if validator.valid(len(temp)):
				file_to_artifacts[arg_f] = temp

	artifact_to_files = dict()
	for (f, artifacts) in file_to_artifacts.items():
		for a in artifacts:
			if not (a in artifact_to_files):
				artifact_to_files[a] = []
			artifact_to_files[a].append(f)

	if args.exclude_common:
		artifact_to_files = {a: files for (a, files) in artifact_to_files.items() if len(files) != len(file_to_artifacts)}

	for (file, artifacts) in file_to_artifacts.items():
		print(file + " " + str(len(artifacts)))

	for (artifact, files) in artifact_to_files.items():
		optional = (" " + " ".join(files)) if args.list_file_names else ""
		print(artifact + optional)

