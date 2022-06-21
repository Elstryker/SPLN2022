from cProfile import label
import string, re, spacy
import cleantext as ct
from googletrans import Translator
from bs4 import BeautifulSoup
from autocorrect import Speller
class TextProcessor():

    def __init__(self):
        self.dataset = ''
        self.lang = ''
        self.translator = Translator()
        self.nlp = None

    def insertDataset(self, dataset):
        try:
            self.lang = self.translator.detect(dataset).lang
        except:
            self.lang = 'en'
            print("Could not detect language, assuming english")
        
        self.dataset = dataset
        print(self.lang)

        if self.lang == 'en':
            self.nlp = spacy.load('en_core_web_sm')
        elif self.lang == 'pt':
            self.nlp = spacy.load('pt_core_news_sm')
        else:
            print("Language not supported, some functionalities may not work properly")

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

    def convertToASCII(self):
        self.dataset = ct.to_ascii_unicode(self.dataset)

    def toLowerCase(self):
        self.dataset = self.dataset.lower()

    def subEmails(self,change):
        self.dataset = ct.replace_emails(self.dataset,change)

    def subURLs(self,change):
        self.dataset = ct.replace_urls(self.dataset,change)

    def removeEmojis(self):
        self.dataset = ct.emojize(self.dataset)
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

    def translateToEnglish(self):
        translator = Translator()

        if self.lang == '':
            self.lang = 'en'

        temporaryLang = 'en'

        self.dataset = translator.translate(self.dataset,temporaryLang,self.lang)

        self.dataset = self.dataset.text

    def removeStopWords(self):
        stopwords = self.nlp.Defaults.stop_words
        lst = []
        for token in self.dataset.split():
            if token.lower() not in stopwords:
                lst.append(token)

        self.dataset = ' '.join(lst)
    
    def ner(self):
        
        doc = self.nlp(self.dataset)
        html = '''
        <html>
            <head>
             <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css"> 
                <title> 
                    Named Entity Recognition 
                </title>
            </head>
        <body>
            <table class="w3-table-all">
                <tr>
                    <th> Word </th>
                    <th> Entity </th>
                    <th> Occurences </th>
                </tr>
            </table>
        </body>
        
        '''
        soup = BeautifulSoup(html,"html5lib")
        file = open("../output/NER.html","w")
        
        dic=dict()

        for ent in doc.ents:
            if ent.text not in dic:
                dic[ent.text]={"label":"NONE","count":0}
            if(dic[ent.text]["label"]==ent.label_):
                dic[ent.text]["count"]+=1
            else:    
                dic[ent.text]["label"]=ent.label_
                dic[ent.text]["count"]+=1
        
        
        for key,value in dic.items():
            text = soup.new_tag("td")
            text.string = key
            label = soup.new_tag("td")
            label.string = value["label"]
            contador = soup.new_tag("td")
            contador.string = str(value["count"])
            tr = soup.new_tag("tr")
            tr.append(text)
            tr.append(label)
            tr.append(contador)
            
            addingItem = soup.findAllNext("tr")[-1]
            addingItem.insert_after(tr)
            

            
        file.write(str(soup.prettify()))


    def lemmatization(self):
        doc = self.nlp(self.dataset)
        for token in doc:
            count = self.dataset.count(token.text)
            self.dataset = self.dataset.replace(token.text,token.lemma_,count)
    
    def spellchecking(self):
        spell = Speller(lang=self.lang)
        doc = self.nlp(self.dataset)
        for frase in doc.sents:
            for word in frase:
                if(word.text!=spell(word.text)):
                    self.dataset = self.dataset.replace(word.text,spell(word.text))

        