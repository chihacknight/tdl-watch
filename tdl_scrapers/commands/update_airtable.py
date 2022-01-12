from scrapy.commands import ScrapyCommand


class Command(ScrapyCommand):
    requires_project = True

    def run(self, args, opts):
        pass
