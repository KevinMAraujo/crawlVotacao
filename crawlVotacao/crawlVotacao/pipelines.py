# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy.exporters import CsvItemExporter
from scrapy import signals
import csv

words_to_filter = ['project-label project', 'hoteis', 'resort', 'thermas']
class CrawlvotacaoPipeline(object):
    def process_item(self, item, spider):
        #if self.words_to_filter[0] in str(item['grupo']).lower():
		return item
        #else:
        #    raise DropItem("No contains forbidden word: %s" % self.words_to_filter[0])

class CSVWriterPipeline(object):
    pass

class MyProjectCsvItemExporter(CsvItemExporter):
    def __init__(self, *args, **kwargs):
        delimiter = settings.get('CSV_DELIMITER', ',')
        kwargs['delimiter'] = delimiter
        fields_to_export = settings.get('FIELDS_TO_EXPORT', [])
        if fields_to_export :
            kwargs['fields_to_export'] = fields_to_export
        super(MyProjectCsvItemExporter, self).__init__(*args, **kwargs)

