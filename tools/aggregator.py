import json
import os

class TwitterAggregator():
	def __init__(self, output_path, file_prefix, file_ext):
		self.output_path = output_path
		self.file_prefix = file_prefix
		self.data_file_prefix = '{}_results_'.format(file_prefix)
		self.result_file_name = '{}_all.{}'.format(file_prefix, file_ext)
		self.file_ext = file_ext

	def aggregate_ids(self):
		all_data = dict()
		all_ids = set()

		# read output files
		for dir_path, dirs, files in os.walk(self.output_path):
			for f in files:
				if f.endswith(self.file_ext) and f.startswith(self.data_file_prefix):
					with open(os.path.join(dir_path, f)) as data_file:
						data = json.load(data_file)

						if not all_data:
							ids = data['data']['ids']

						else:
							ids = list(set(data['data']['ids']) - all_ids)

						all_data[data['timestamp']] = {
							'count': len(ids),
							'ids': ids
						}
						all_ids |= set(ids)

		# write aggregated results
		with open(os.path.join(dir_path, self.result_file_name), 'w') as outfile:
			json.dump(all_data, outfile)

if __name__ == '__main__':
	# test
	aggregator = TwitterAggregator('../output/api/{}'.format('20170530-160538'), 'twitter-retweets-861544307043467264', 'json')
	aggregator.aggregate_ids()














