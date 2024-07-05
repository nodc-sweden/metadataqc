import pandas as pd


class MetaDataQc:

    def __init__(self, metadatacolumns):
        """
        data: en dataframe med all data från en station
        """
        self._metadata_report = dict.fromkeys(metadatacolumns)
