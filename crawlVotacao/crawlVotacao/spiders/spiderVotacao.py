# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import CrawlvotacaoItem
import logging
from scrapy.utils.log import configure_logging

configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='log.txt',
    format='%(levelname)s: %(message)s',
    level=logging.INFO
)


class SpidervotacaoSpider(scrapy.Spider):
    name = "spiderVotacao"
    allowed_domains = ["fund.bedream.me"]
    start_urls = (
        'http://fund.bedream.me/#projects',
    )

    def parse(self, response):
        #maxPage = int(response.xpath('//*[@id="projects_to_refresh"]/div[3]/nav/span[8]/a/@href()').extract())
        maxPage = 285
        yield scrapy.Request(response.url, callback=self.extraiLinkDeCadaProjeto)

        for page in range(2, maxPage):
            urlPagina = "http://fund.bedream.me/?page="+str(page)
            self.logger.debug('Retrieved URL: %s', urlPagina)
            yield scrapy.Request(urlPagina, callback=self.extraiLinkDeCadaProjeto)

    def extraiLinkDeCadaProjeto(self, response):
        self.logger.debug('#####################')
        for href in response.xpath('//*[@id="projects-list"]/div/div/a/@href'):
            urlProjeto = response.urljoin(href.extract())
            self.logger.debug('Retrieved URL: %s', urlProjeto)
            yield scrapy.Request(urlProjeto, callback=self.extrairDados)
        self.logger.debug('******####**********')

    def extrairDados(self, response):
        item = CrawlvotacaoItem()
        item['nomeProjeto'] = response.xpath('//*[@id="project-cover"]/div/div/div/div/h1/text()').extract()
        item['nome'] = response.xpath('//*[@id="project-cover"]/div/div/div/div/span[2]/b/text()').extract()
        item['qtdVotos'] = response.xpath('//*[@id="project-cover"]/div/div/div/div/div/b/text()').extract()
        item['grupo'] = response.xpath('//*[@id="project-cover"]/div/div/div/div/span[1]/@class').extract()
        item['url'] = response.url
        yield item