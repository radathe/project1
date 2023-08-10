class MyFile:
    def __init__(self, filename, mode, enc):
        self.filename = filename
        self.mode = mode
        self.enc = enc

    def __enter__(self):
        f = open(self.filename, self.mode, encoding=self.enc)
        self.f = f
        return f
 
        
    def __exit__(self, exc_type, exc_val, exc_tb):
    
        self.f.close()

        
with MyFile('Итераторы, контекст-менеджер.txt', 'w', 'utf-8'):
    MyFile.write('111111111111111111111111111111111')