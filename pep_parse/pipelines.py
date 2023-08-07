import time


class PepParsePipeline:
    def open_spider(self, spider):
        self.pep_count = dict()
        self.total = 0

    def process_item(self, item, spider):
        status_counter = self.pep_count.get(item['status']) or 0
        self.pep_count[item['status']] = status_counter + 1
        self.total += 1
        return item

    def close_spider(self, spider):
        filename = ('results/'
                    f'status_summary_{time.strftime("%Y-%m-%dT%H-%M-%S")}.csv')
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status in self.pep_count.keys():
                f.write(f'{status},{self.pep_count[status]}\n')
            f.write(f'Total,{self.total}\n')
