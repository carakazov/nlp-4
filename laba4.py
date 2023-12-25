# -*- coding: utf-8 -*-
from natasha import Segmenter, MorphVocab, NewsEmbedding, NewsMorphTagger, NewsSyntaxParser, NewsNERTagger, Doc

text = "Владимир — город и областной центр в европейской части России, он входит в число восьми городов Золотого кольца России. Древний русский город построен на левом берегу реки Клязьмы, в 190 км к востоку от Москвы. Во Владимире живет около 350 тыс. человек. Город с тысячелетней историей является крупным туристическим центром и привлекает путешественников из России и из-за рубежа"
text_with_mistakes = "Владимвир — город и областной, цевантр в европавейской   частиРоссии, он вхоавдит в чиавсло  восьми городваов   Золотого кольца Ровссии.   Дравевний  русавский город построен на левом берегу реки Квалязьмы, в 190 км к востоку от Москвы. Во, Владимире, жавивет   около 350 тыс. человек. Горовад с тывасячелетней историей являав ется крупным туристическим центром и привлекает путешавественников из Росавсии и из-за рубежа"
translit_text = "Vladimir — gorod i oblastnoj centr v evropejskoj chasti Rossii, on vhodit v chislo vos'mi gorodov Zolotogo kol'ca Rossii. Drevnij russkij gorod postroen na levom beregu reki Klyaz'my, v 190 km k vostoku ot Moskvy. Vo Vladimire zhivet okolo 350 tys. chelovek. Gorod s tysyacheletnej istoriej yavlyaetsya krupnym turisticheskim centrom i privlekaet puteshestvennikov iz Rossii i iz-za rubezha"
word_sentence = "Владимир. — город. и. областной. центр. в. европейской. части. России. он. входит. в. число. восьми. городов. Золотого. кольца. России. Древний. русский. город. построен. на. левом. берегу. реки. Клязьмы. в. 190. км. к. востоку. от. Москвы. Во. Владимире. живет. около. 350. тыс. человек. Город. с. тысячелетней. историей. является. крупным. туристическим. центром. и. привлекает. путешественников. из. России. и. из-за. рубежа"

def proceed_text(article):
    segmenter = Segmenter()
    moscow_article = Doc(article)
    moscow_article.segment(segmenter)
    print(moscow_article.tokens)
    embedding = NewsEmbedding()
    syntax_parser = NewsSyntaxParser(embedding)
    moscow_article.parse_syntax(syntax_parser)
    moscow_article.sents[0].syntax.print()

    morph_tagger = NewsMorphTagger(embedding)
    moscow_article.tag_morph(morph_tagger)
    moscow_article.sents[0].morph.print()

    morph_vocab = MorphVocab()
    for token in moscow_article.tokens:
        token.lemmatize(morph_vocab)
        print(f"{token.text} - {token.lemma}")

    ner_tagger = NewsNERTagger(embedding)
    moscow_article.tag_ner(ner_tagger)
    moscow_article.ner.print()


proceed_text(text)
proceed_text(text_with_mistakes)
proceed_text(translit_text)
proceed_text(word_sentence)
