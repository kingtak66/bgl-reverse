# glossary file parameter, may contain format identification information, at the beginning of a BGR
RC_PARAM=0
# glossary property
RC_PROP=3
# term
RC_TERM1=0x1
RC_TERMA=0xA
RC_TERMB=0xB
# resource
RC_RES=2

# no data

RC_NULLS=set([0x6,0x4,0x5])

LEXICAL_CLASS = {
    0x30:'n.',
    0x31:'adj.',
    0x32:'v.',
    0x33:'adv.',
    0x34:'interj.',
    0x35:"pron.",
    0x36:"prep.",
    0x37:"conj.",
    0x38:"suff.",
    0x39:"pref.",
    0x3A:"art." 
    }

DERIVATION = (
    'V-0',# Verb
    'V-0.0',# Verb
    'V-0.1',# Infinivtive
    'V-0.1.1',# ?
    'V-1.0',
    'V-1.1',
    'V-1.1.1', # Present Simple
    'V-1.1.2', #Present Simple (3rd pers. sing.)
    'V-2.0',#
    'V-2.1',#
    'V-2.1.1',# Past Simple
    'V-3.0',#
    'V-3.1',#
    'V-3.1.1',# Present Participle
    'V-4.0',#
    'V-4.1',#
    'V-4.1.1',#Past Participle
    'V-5.0',#
    'V-5.1',#
    'V-5.1.1',#Future
    'V2-0',#
    'V2-0.0',#
    'V2-0.1',#Infinitive
    'V2-0.1.1',#
    'V2-1.0',#
    'V2-1.1',#
    'V2-1.1.1',#Present Simple (1st pers. sing.)
    'V2-1.1.2',#Present Simple (2nd pers. sing. & plural forms)
    'V2-1.1.3',#Present Simple (3rd pers. sing.)
    'V2-2.0',#
    'V2-2.1',#
    'V2-2.1.1',#Past Simple (1st & 3rd pers. sing.)
    'V2-2.1.2',#Past Simple (2nd pers. sing. & plural forms)
    'V2-3.0',#
    'V2-3.1',#
    'V2-3.1.1',#Present Participle
    'V2-4.0',#
    'V2-4.1',#
    'V2-4.1.1',#Past Participle
    'V2-5.0',#
    'V2-5.1',#
    'V2-5.1.1',#Future
    'N-0',#Noun
    'N-1.0',#
    'N-1.1',#
    'N-1.1.1',#Singular
    'N-2.0',#
    'N-2.1',#
    'N-2.1.1',#Plural
    'N4-1.0',#
    'N4-1.1',#
    'N4-1.1.1',#Singular Masc.
    'N4-1.1.2',#Singular Fem.
    'N4-2.0',#
    'N4-2.1',#
    'N4-2.1.1',#Plural Masc.
    'N4-2.1.2',#Plural Fem.
    'ADJ-0',#Adjective
    'ADJ-1.0',#
    'ADJ-1.1',#
    'ADJ-1.1.1',#Adjective
    'ADJ-1.1.2',#Comparative
    'ADJ-1.1.3',#Superlative
    )

LANGUAGE = (
    "English", 
    "French",
    "Italian",
    "Spanish",
    "Dutch",
    "Portuguese",
    "German",
    "Russian",
    "Japanese",
    "Traditional Chinese",
    "Simplified Chinese",
    "Greek",
    "Korean",
    "Turkish",
    "Hebrew",
    "Arabic",
    "Thai",
    "Other",
    "Other Simplified Chinese dialects",
    "Other Traditional Chinese dialects",
    "Other Eastern-European languages",
    "Other Western-European languages",
    "Other Russian languages",
    "Other Japanese languages",
    "Other Baltic languages",
    "Other Greek languages",
    "Other Korean dialects",
    "Other Turkish dialects",
    "Other Thai dialects",
    "Polish",
    "Hungarian",
    "Czech",
    "Lithuanian",
    "Latvian",
    "Catalan",
    "Croatian",
    "Serbian",
    "Slovak",
    "Albanian",
    "Urdu",
    "Slovenian",
    "Estonian",
    "Bulgarian",
    "Danish",
    "Finnish",
    "Icelandic",
    "Norwegian",
    "Romanian",
    "Swedish",
    "Ukrainian",
    "Belarusian",
    "Farsi",
    "Basque",
    "Macedonian",
    "Afrikaans",
    "Faeroese",
    "Latin",
    "Esperanto",
    "Tamazight",
    "Armenian"
    )

GLS_PROP={
    0x01:"Title",
    0x02:"Author Name",
    0x03:"Author Email",
    0x04:"Copyright",
    0x07:"Source Language",
    0x08:"Target Language",
    0x09:"Description",
    0x0B:"Icon",
    0x0C:"Entry Count",
    0x1A:"Source Charset",
    0x1B:"Target Charset",
    0x27:"Word Class Name", # localized word class name
    0x33:"Create Time",
    0x1C:"Update Time",
    0x3B:"Morphological Derivation Type", # localized names of word variation type
    0x41:"Glossary Manual"
    }

CHARSET = {
    0x41: "ISO-8859-1", #Default
    0x42: "ISO-8859-1", #Latin
    0x43: "ISO-8859-2", #Eastern European
    0x44: "ISO-8859-5", #Cyriilic
    0x45: "ISO-8859-14",#Japanese
    0x46: "BIG5",       #Traditional Chinese
    0x47: "GB2312",     #Simplified Chinese
    0x48: "CP1257",     #Baltic
    0x49: "CP1253",     #Greek
    0x4A: "ISO-8859-15",#Korean
    0x4B: "ISO-8859-9", #Turkish
    0x4C: "ISO-8859-9", #Hebrew
    0x4D: "CP1256",     #Arabic
    0x4E: "CP874"       #Thai
    }

TERM_PROP_NAME={
    0x18: "Display Name",
    
    }

def getTermPropName(spec):
    pass

class Term:
    def __init__(self,title,alt=[],prop={},defin=[]):
        self.title=title
        self.alt=alt
        self.prop=prop
        self.defin=defin

class Resource:
    def __init__(self,title,data):
        self.title=title
        self.data=data