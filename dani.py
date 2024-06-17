class NewsAgency:
    def init(self):
        self._observers = []
        self._news = None
        def attach(self, observer):
        self._observers.append(observer)
    def detach(self, observer):
        self._observers.remove(observer)
        def notify(self):
            for observer in self._observers:
                observer.update(self._news)
                def add_news(self, news):
                    self._news = news
                    self.notify()