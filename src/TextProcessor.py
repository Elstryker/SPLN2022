import string, re, cleantext as ct, spacy
from googletrans import Translator

class TextProcessor():

    def __init__(self):
        self.dataset = ''
        self.lang = ''
        self.translator = Translator()
        self.nlp = None

    def insertDataset(self, dataset):
        self.lang = self.translator.detect(dataset).lang
        self.dataset = dataset
        print(self.lang)

        if self.lang == 'en':
            self.nlp = spacy.load('en_core_web_sm')
        elif self.lang == 'pt':
            self.nlp = spacy.load('pt_core_news_sm')
        else:
            "Language not supported, some functionalities may not work properly"

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

    def removeEmojis(self):
        self.dataset = ct.remove_emoji(self.dataset)

    def demojize(self):
        self.dataset = ct.demojize(self.dataset)

    def removeHTMLTags(self):
        pattern = re.compile(r'<.*?>')
        self.dataset = pattern.sub('',self.dataset)

    def translateAllTextToOriginalLanguage(self):
        translator = Translator()

        if self.lang == '':
            self.lang = 'en'

        temporaryLang = 'en' if self.lang != 'en' else 'de'


        self.dataset = translator.translate(self.dataset,temporaryLang,self.lang)
        self.dataset = translator.translate(self.dataset.text,self.lang,temporaryLang)

        self.dataset = self.dataset.text

    def removeStopWords(self):
        stopwords = self.nlp.Defaults.stop_words
        lst = []
        for token in self.dataset.split():
            if token.lower() not in stopwords:
                lst.append(token)

        self.dataset = ' '.join(lst)