import pandas as pd


class MetaDataQc:

    def __init__(self, metadata: dict):
        """

        """
        self._metadata = metadata
        self._metadatareport = dict.fromkeys(metadata.keys(), True)
        print(metadata.keys())

    @property
    def report(self):
        return self._metadatareport

    def run_automatic_qc(self):

        self.check_wadep()

    def check_wadep(self):

        if max(map(int, self._metadata["DEPH"].split(', '))) > self._metadata['WADEP']:
            self._metadatareport['WADEP'] = False
            return False

