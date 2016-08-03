# -*- coding: utf-8 -*-

BOT_NAME = 'crawlVotacao'

SPIDER_MODULES = ['crawlVotacao.spiders']
NEWSPIDER_MODULE = 'crawlVotacao.spiders'

DOWNLOAD_HANDLERS = {'s3': None}
ITEM_PIPELINES = {'crawlVotacao.pipelines.CrawlvotacaoPipeline': 1,
                  'crawlVotacao.pipelines.CSVWriterPipeline': 900,

                  }

CSV_DELIMITER = ";"
FIELDS_TO_EXPORT = [
    'nomeProjeto','nome','qtdVotos', 'grupo', 'url'
]
FEED_EXPORTERS = {
    'csv': 'crawlVotacao.pipelines.MyProjectCsvItemExporter',
}