import time

from .settings import BASE_DIR, RESULTS_DIR

FILE_NAME = 'status_summary_{}.csv'
TIME_FORMAT = r'%Y-%m-%dT%H-%M-%S'


class PepParsePipeline:
    def open_spider(self, spider):
        self.results = BASE_DIR / RESULTS_DIR
        self.results.mkdir(exist_ok=True)
        self.pep_count = dict()
        self.total = 0

    def process_item(self, item, spider):
        status_counter = self.pep_count.get(item['status']) or 0
        self.pep_count[item['status']] = status_counter + 1
        self.total += 1
        return item

    def close_spider(self, spider):
        with open(
            self.results / FILE_NAME.format(time.strftime(TIME_FORMAT)),
            mode='w',
            encoding='utf-8'
        ) as f:
            f.write('Статус,Количество\n')
            for status in self.pep_count.keys():
                f.write(f'{status},{self.pep_count[status]}\n')
            f.write(f'Total,{self.total}\n')
