class nhDetail:
    def __init__(self, doujin):
        self.__doujin = doujin
        self.__tag = []
        self.__artist = []
        self.__language = []
        for tags in self.__doujin.tags:
            if tags.type == 'tag':
                self.__tag.append(tags.name)
            elif tags.type == 'artist':
                self.__artist.append(tags.name)
            elif tags.type == 'language':
                self.__language.append(tags.name)

    def replace_doujin(self, doujin):
        self.__doujin = doujin
        self.__tag = []
        self.__artist = []
        self.__language = []
        for tags in self.__doujin.tags:
            if tags.type == 'tag':
                self.__tag.append(tags.name)
            elif tags.type == 'artist':
                self.__artist.append(tags.name)
            elif tags.type == 'language':
                self.__language.append(tags.name)

    def get_doujin(self):
        return self.__doujin

    def get_url(self):
        return self.__doujin.url

    def get_id(self):
        return self.__doujin.id
    
    def get_title_en(self):
        return self.__doujin.titles['english']
    
    def get_title_jp(self):
        return self.__doujin.titles['japanese']
    
    def get_tag(self):
        if len(self.__tag) < 1:
            self.__tag.append("None")
        return self.__tag
    
    def get_author(self):
        if len(self.__artist) < 1:
            self.__artist.append("None")
        return self.__artist

    def get_language(self):
        if len(self.__language) < 1:
            self.__language.append("None")
        return self.__language
    
    def get_page_len(self):
        return len(self.__doujin.pages)

    def get_pages(self, page):
        return self.__doujin.pages[page].url

    def get_thumbnail(self):
        return self.__doujin.thumbnail