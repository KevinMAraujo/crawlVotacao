# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item

def strip_and_join(values):
    if len(values)>0:
        value = values[0].strip()
        joined = u' '.join(value.split('\n'))
        joined = joined.replace('\r', '').replace('(', '').replace(')','')
        joined = joined.replace(u'\xc0','a').replace(u'\xc1','a').replace(u'\xc2','a').replace(u'\xc3','a').replace(u'\xe0','a').replace(u'\xe1','a').replace(u'\xe2','a').replace(u'\xe3','a').replace(u'\xe4','a')
        joined = joined.replace(u'\xca','e').replace(u'\xc9','e').replace(u'\xe8','e').replace(u'\xe9','e').replace(u'\xea','e')
        joined = joined.replace(u'\xcd','i').replace(u'\xed','i').replace(u'\xee','i').replace(u'\xef','i').replace(u'\u27a1','..')
        joined = joined.replace(u'\xd3','o').replace(u'\xd4','o').replace(u'\xf2','o').replace(u'\xf3','o').replace(u'\xf4','o').replace(u'\xf5','o').replace(u'\xf6','o')
        joined = joined.replace(u'\xda','u').replace(u'\xdc','u').replace(u'\xf9','u').replace(u'\xfa','u').replace(u'\xfb','u').replace(u'\xfc','u')
        joined = joined.replace(u'\xc7','c').replace(u'\xe7','c').replace(u'\u2013','-').replace(u'\xd5','o').replace(u'\xb0','C').replace(u'\u2022','..')
        joined = joined.replace(u'\u2018',"'").replace(u'\u2019',"'").replace(u'\u014d','o').replace(u'\u0101','a').replace(u'\u200e','o').replace(u'\u201c','').replace(u'\u201d','')
        joined = joined.replace(u'\xa0',' ').replace(u'\xa0',' ').replace(u'\u0301','').replace(u'\u0303','').replace(u'\xaa','a').replace(u'\u202c','a')
        joined = joined.replace(u'\ufeff','').replace(u'\xd8','O').replace(u'\x89','').replace(u'\xcc','I').replace(u'\xc0','A').replace(u'\xae','A')
        joined = joined.replace(u'\xba','').replace(u'\xb4','').replace(u'\xb7','').replace(u'\xbf','').replace(u'\x88','')
        joined = joined.replace(u'\xb2','2').replace(u'\xf1','n').replace(u'\xa5','y')


        return joined
    else:
        return u'0'

class CrawlvotacaoItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nomeProjeto = Field(serializer=strip_and_join)
    nome = Field(serializer=strip_and_join)
    qtdVotos = Field(serializer=strip_and_join)
    grupo = Field(serializer=strip_and_join)
    url = Field(serializer=strip_and_join)
