import string, re, langdetect, cleantext as ct

class TextProcessor():

    def __init__(self):
        self.dataset = ''

    def insertDataset(self, dataset):
        lang = langdetect.detect(dataset)
        self.dataset = dataset
        print(lang)

    def getDataset(self):
        return self.dataset

    def removePonctuation(self):
        remove = string.punctuation + '–'
        remove = remove.replace("-", "") # Don't remove hyphens
        pattern = r"[{}]".format(remove) # Create the pattern

        self.dataset = re.sub(rf'{pattern}', "", self.dataset) # Remove all punctuation except hyphen
        self.dataset = re.sub(r'\s+\-', "", self.dataset) # Remove isolated hyphens (This is pretended if we want to mantain hyphenized words)
        self.dataset = re.sub(r'\-\s+', "", self.dataset)
        

    def normalizeWhitespaces(self):
        self.dataset = ct.normalize_whitespace(self.dataset)

    def toLowerCase(self):
        self.dataset = self.dataset.lower()

    def subEmails(self,change):
        self.dataset = ct.replace_emails(self.dataset,change)

    def subURLs(self,change):
        self.dataset = ct.replace_urls(self.dataset,change)

    


    def getEnglish():
        # en_core_web_sm
        # pt_core_news_sm
        pass
