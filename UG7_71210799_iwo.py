class Browser:
    def __init__(self):
        self.history = []
        self.current_url = None
        self.future = []

    def go(self, url):
        self.history.append(url)
        self.current_url = url
        self.future = []

    def back(self):
        if len(self.history) > 1:
            self.future.append(self.current_url)
            self.history.pop()
            self.current_url = self.history[-1]

    def forward(self):
        if self.future:
            self.history.append(self.future[-1])
            self.current_url = self.future[-1]
            self.future.pop()

    def printAll(self):
        for url in self.history:
            print(url)


browser = Browser()

browser.go("https://google.com")

browser.go("https://ukdw.ac.id")

browser.go("https://facebook.com")

browser.back() #output: https://ukdw.ac.id

browser.back() #output: https://google.com

browser.forward() #output: https://ukdw.ac.id

browser.go("https://twitter.com")

browser.printAll() #output: https://google.com https://ukdw.ac.id https://twitter.com
