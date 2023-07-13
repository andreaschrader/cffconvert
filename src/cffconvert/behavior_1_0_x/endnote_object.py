from cffconvert.behavior_1_x_x.endnote_author import EndnoteAuthor
from cffconvert.behavior_1_0_x.endnote_url import EndnoteUrl
from cffconvert.behavior_1_x_x.endnote_object_shared import EndnoteObjectShared as Shared


class EndnoteObject(Shared):

    supported_cff_versions = [
        '1.0.1',
        '1.0.2',
        '1.0.3'
    ]

    def add_author(self):
        authors_cff = self.cffobj.get('authors', [])
        authors_endnote = [EndnoteAuthor(a).as_string() for a in authors_cff]
        authors_endnote_filtered = [a for a in authors_endnote if a is not None]
        self.author = ''.join(authors_endnote_filtered)
        return self

    def add_doi(self):
        if 'doi' in self.cffobj.keys():
            self.doi = f"%R {self.cffobj['doi']}\n"
        return self

    def add_url(self):
        self.url = EndnoteUrl(self.cffobj).as_string()
        return self

    def add_year(self):
        if 'date-released' in self.cffobj.keys():
            self.year = f"%D {self.cffobj['date-released'].year}\n"
        return self
