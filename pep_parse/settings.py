from pathlib import Path

BASE_DIR = Path(__file__).absolute().parent.parent
RESULTS_DIR = 'results'
SPIDER_NAME = 'pep'
ALLOWED_DOMAINS = ['peps.python.org']
START_URLS = ['https://peps.python.org/']

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

FEED_EXPORT_ENCODING = 'utf-8'

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': {'number': 'Номер', 'name': 'Название', 'status': 'Статус'},
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
