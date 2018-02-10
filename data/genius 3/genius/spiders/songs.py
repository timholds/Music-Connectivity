# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.shell import inspect_response
from scrapy.http.request import Request
import re
import datetime
from genius.items import SongItem
from IPython import embed
from functools import partial
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import urllib
import csv
import string
import requests
class SongSpider(CrawlSpider):
    name = 'songs'
    # runtime = datetime.datetime.now(pytz.timezone('EST')).strftime('%Y-%m-%d %H:%M')
    already_scraped = set(open('./already_scraped.txt').read().split())
    allowed_domains = ['https://www.genius.com','http://www.genius.com','www.genius.com','genius.com']
    start_urls = ['https://www.genius.com']
    # start_urls = ['https://genius.com/Fabolous-doin-it-well-lyrics']
    # start_urls = ["http://www.bgasc.com/category/american-gold-eagles","http://www.bgasc.com/category/all-gold-bars","http://www.bgasc.com/category/gold-rounds-all-sizes","http://www.bgasc.com/category/gold-buffalo-coins-and-sets","http://www.bgasc.com/category/pre-1933-us-gold","http://www.bgasc.com/category/pre-1933-us-gold","http://www.bgasc.com/category/south-african-gold-krugerrands","http://www.bgasc.com/category/australian-gold-kangaroos-nuggets","http://www.bgasc.com/category/austrian-gold-coins-philharmonics-more","http://www.bgasc.com/category/chinese-gold-panda-coins","http://www.bgasc.com/category/british-gold-sovereigns-gold-britannias","http://www.bgasc.com/category/mexican-gold-coins","http://www.bgasc.com/category/american-silver-eagles-silver-dollars","http://www.bgasc.com/category/all-silver-bars","http://www.bgasc.com/category/silver-rounds-all-sizes","http://www.bgasc.com/category/90-percent-silver-dimes-10c-01","http://www.bgasc.com/category/90-percent-silver-quarters-25c-01","http://www.bgasc.com/category/90-percent-silver-half-dollars-50c-01","http://www.bgasc.com/category/90-percent-silver-dollars-02","http://www.bgasc.com/category/90-percent-silver-coins-by-the-bag-01","http://www.bgasc.com/category/canadian-silver-coins-maple-leafs-more","http://www.bgasc.com/category/british-silver-coins","http://www.bgasc.com/category/australian-silver-coins","http://www.bgasc.com/category/austrian-silver-coins-vienna-philharmonics","http://www.bgasc.com/category/china-silver-coins-chinese-pandas","http://www.bgasc.com/category/mexican-silver-coins","http://www.bgasc.com/category/morgan-silver-dollars-1878-1921-01","http://www.bgasc.com/category/peace-dollars-01","http://www.bgasc.com/category/america-the-beautiful-atb-5-oz-silver-coins","http://www.bgasc.com/category/buy-platinum","http://www.bgasc.com/category/buy-palladium"]

    rules = (
        Rule(LinkExtractor(deny=(r'com/[a-zA-Z0-9_-]+-[a-zA-Z0-9_-]+-lyrics+$'))),
        # Rule(LinkExtractor(allow=('category'),deny=('product','catalog','account') + excluded_words)),
        # Rule(LinkExtractor(allow=('artist-index/')) + excluded_words)),
            # Rule(LinkExtractor(allow=('artist-index/')) + excluded_words)),

                Rule(LinkExtractor(allow=(r'com/[a-zA-Z0-9_-]+-[a-zA-Z0-9_-]+-lyrics+$'),deny =('com/Genius-')), callback="parse_song"),

        )

    def __init__(self, *args, **kwargs):
        # XXX: needs phantomjs binary available in PATH
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1120, 550)
        super(SongSpider, self).__init__(*args, **kwargs)
    def parse_song(self, response):
        # def fix_unicode(x):
        #     if isinstance(x,unicode):
        #         t =x.encode('utf-8')
        #     else:
        #         t = x 
        #     return  filter(lambda x: x in string.printable, t)
        def fix_unicode(x):
            if isinstance(x,unicode):
                t =x.encode('utf-8')
            else:
                t = x 
            return  t

        # def split_names(x):

        # Initialize all variables as None
        producer1 = 'None'
        producer2 = 'None'
        producer3 = 'None'
        producer4 = 'None'
        producer5 = 'None'
        artist1 = 'None'
        artist2 = 'None'
        artist3 = 'None'
        feature1  ='None'
        feature2 = 'None'
        feature3 = 'None'
        feature4 = 'None'
        feature5 = 'None'
        writer1 = 'None'
        writer2 = 'None'
        writer3 = 'None'
        writer4 = 'None'
        writer5 = 'None'
        writer6 = 'None'
        song_name = 'None'
        artist = 'None'
        lyrics = 'None'
        release_date = 'None'
        recording = 'None'
        mixing = 'None'
        interpolate = 'None'
        produced_by = 'None'
        cover_art_photo = 'None'
        recorded_at = 'None'
        video_director1 = 'None'
        video_director2 = 'None'
        programmer1 = 'None'
        programmer2 = 'None'
        director_of_photography = 'None'
        record_label = 'None'
        recorded_at = 'None'
        samples = 'None'
        sampled_in = 'None'
        remix_of = 'None'
        link_to_youtube = 'None'
        page_views = 'None'
        page_contrib = 'None'
        writers = []
        produced_by = []
        video_directors = []
        programmers = []
        artists = []


        # send phantomjs browser to the requested page
        self.driver.get(response.url)
        time.sleep(.3)
        try:
            for button in self.driver.find_elements_by_class_name('metadata_unit-show_more'):
                button.click()
                time.sleep(.01)
            for button in self.driver.find_elements_by_class_name('metadata_unit-show_more'):
                button.click()
                time.sleep(.01)
        except:
            pass
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(.3)
        # Click all of the show more buttons
        try:
            for button in self.driver.find_elements_by_class_name('metadata_unit-show_more'):
                button.click()
                time.sleep(.01)
            for button in self.driver.find_elements_by_class_name('metadata_unit-show_more'):
                button.click()
                time.sleep(.01)
        except:
            pass
        page_info = BeautifulSoup(self.driver.page_source, "html.parser")
        # Parse song, artist name and lyrics
        song_name = response.css('h1::text').extract_first().encode('utf8')
        song_name = unicode(song_name.decode('utf8'))
        artist = response.css('a.header_with_cover_art-primary_info-primary_artist::text').extract_first().encode('utf8')
        artist = unicode(artist.decode('utf8'))       
        lyrics = ''.join(response.css('div.lyrics').css('::text').extract()).strip()
        # save lyrics
        file_name = u"{song_name}_{artist}".format(**locals()).replace(' ','-').encode('utf8').replace('/','-')
        lyrics_dir = 'LyricsData/{file_name}.txt'.format(**locals())
        text_file = open(lyrics_dir, "w")
        text_file.write(lyrics.encode('utf8'))
        text_file.close()


        # download cover image:
        image_url = response.css('img.cover_art-image::attr(src)').extract_first().encode('utf8')
        img_dir = 'ImgData/{file_name}.jpg'.format(**locals())
        # urllib.urlretrieve(image_url,img_dir)


        f = open(img_dir,'wb')
        f.write(requests.get(image_url).content)
        f.close()

        # Get the information for Producers, featured artist and album
        # song_data_raw = response.css('div.header_with_cover_art-primary_info').css('h3').css('::text').extract()

        song_data_raw_unparsed = page_info.select('div.header_with_cover_art-primary_info')[0].select('h3')[0].text
        song_data_raw = []
        for item in song_data_raw_unparsed.strip().split('\n'):
            item = item.replace('&','').replace(',','').strip()
            if item.strip() == '':
                continue    
            if item.strip() == '&':
                continue
            if item.strip() ==',':
                continue
            song_data_raw.append(item.strip())        

        song_data_striped = []
        # format the raw data properly
        for item in song_data_raw:
            if item.strip() == '':
                continue    
            if item.strip() == '&':
                continue
            if item.strip() ==',':
                continue
            song_data_striped.append(item.strip())        



        song_data_featuring = []
        song_data_produced = []
        song_data_album = []


        # this is for featuring
        for i in iter(partial(next, iter(song_data_striped)), 'Produced by'):
            # temp = []
            # temp.append(i)
            song_data_featuring.append(i)
        if 'Featuring' in song_data_featuring:
            song_data_featuring = song_data_featuring[1:]


        # This is for produced by
        for i in iter(partial(next, iter(song_data_striped[len(song_data_featuring) + 1:])), 'Album'):
            if '&' in i:
                continue
            if ',' in i:
                continue
            song_data_produced.append(i)



        if len(song_data_striped) == 0:
            album_name = ''
        else:
            album_name = song_data_striped[-1]

        # Get all the other information, and parse/clean it

        # all_meta_titles = page_info.select('span.metadata_unit-label')
        all_meta_titles= response.css('span.metadata_unit-label').css('::text').extract()

        all_meta_info_raw = page_info.select('span.metadata_unit-info')
        # all_meta_info_raw = response.css('span.metadata_unit-info')
        all_meta_info = []
        for i in all_meta_info_raw:
            temp_items = []
            for item in i.text.strip().split('\n'):
                item = item.replace('&','').replace(',','').strip()
                if item.strip() == '':
                    continue    
                if item.strip() == '&':
                    continue
                if item.strip() ==',':
                    continue
                temp_items.append(item.strip())

            all_meta_info.append('&'.join(temp_items))                 


        # for i in all_meta_info_raw:
        #     temp_items = []
        #     for item in i.css('::text').extract(): 
        #         if item.strip() == '':
        #             continue    
        #         if item.strip() == '&':
        #             continue
        #         if item.strip() ==',':
        #             continue
        #         temp_items.append(item.strip())

        #     all_meta_info.append('&'.join(temp_items))  


        # Iterate through and get all the info
        for index,label in enumerate(all_meta_titles):
            if label.lower() == 'release date':
                release_date = all_meta_info[index]
            if label.lower() == 'written by':
                writers = all_meta_info[index].split('&')
            if label.lower() == 'recording':
                recording = all_meta_info[index]
            if label.lower() == 'mixing':
                mixing = all_meta_info[index]
            if label.lower() == 'interpolated by':
                interpolate = all_meta_info[index]
            if label.lower() == 'produced by':
                produced_by = all_meta_info[index].split('&')
            if label.lower() == 'recorded at':
                recorded_at = all_meta_info[index]
            if label.lower() == 'director of photography':
                director_of_photography = all_meta_info[index]
            if label.lower() == 'record label':
                record_label = all_meta_info[index]
            if label.lower() == 'video director':
                video_directors = all_meta_info[index].split('&')
            if label.lower() == 'programming':
                programmers = all_meta_info[index].split('&')
            if label.lower() == 'sampled in':
                sampled_in = all_meta_info[index]
            if label.lower() == 'remix of':
                remix_of = all_meta_info[index]
            if label.lower() == 'artists':
                artists = all_meta_info[index].split('&')


        # samples = 'None'
        # sampled_in = 'None'
        # remix_of = 'None'

        # assign all the writers, producers and other multiple person fields
        while len(artists) < 3:
            artists.append('None')
        while len(video_directors) < 2:
            video_directors.append('None')
        while len(programmers) < 2:
            programmers.append('None')
        while len(writers) < 6:
            writers.append('None')
        while len(produced_by) < 5:
            produced_by.append('None')
        while len(song_data_featuring) < 5:
            song_data_featuring.append('None')
        writer1,writer2,writer3,writer4,writer5,writer6 = writers
        producer1,producer2,producer3,producer4,producer5 = produced_by
        feature1,feature2,feature3,feature4,feature5 = song_data_featuring
        video_director1,video_director2 = video_directors
        programmer1,programmer2 = programmers
        artist1,artist2,artist3 = artists

        # video url and contributer/view stats
        if len(page_info.select('div.song_media_controls-provider-icon')) == 0:
            link_to_youtube = 'None'
        else:
            link_to_youtube = page_info.select('div.song_media_controls-provider-icon')[0].select('a')[0]['href']
        if len(page_info.select('div[ng-if=song.stats.pageviews]')) == 0:
            page_views = 'None'
        else:
            page_views = page_info.select('div[ng-if=song.stats.pageviews]')[0]['title'].replace('views','').strip()
        if len(page_info.select('span.text_label.text_label--x_small_text_size')) == 0:
            page_contrib = 'None'
        else:
            try:
                page_contrib = page_info.select('span.metadata_with_icon-link')[0].text.replace('contributors','').strip()
            except:
                try:
                    page_contrib = page_info.select('span.text_label.text_label--x_small_text_size')[-1].text.strip()
                except:
                    page_contrib = 'None'

        with open('./already_scraped.txt', "a") as filename:
            filename.write(response.url + '\n')
        # add everything to a scrapy song item, with one last unicode run
        if feature1 == album_name:
            feature1 = 'None'

        item = SongItem()
        item['producer1'] = fix_unicode(producer1)
        item['producer2'] = fix_unicode(producer2)
        item['producer3'] = fix_unicode(producer3)
        item['producer4'] = fix_unicode(producer4)
        item['producer5'] = fix_unicode(producer5)
        item['feature1' ] = fix_unicode(feature1)
        item['feature2'] = fix_unicode(feature2)
        item['feature3'] = fix_unicode(feature3)
        item['feature4'] = fix_unicode(feature4)
        item['feature5'] = fix_unicode(feature5)
        item['writer1'] = fix_unicode(writer1)
        item['writer2'] = fix_unicode(writer2)
        item['writer3'] = fix_unicode(writer3)
        item['writer4'] = fix_unicode(writer4)
        item['writer5'] = fix_unicode(writer5)
        item['writer6'] = fix_unicode(writer6)
        item['song_name'] = fix_unicode(song_name)
        item['artist'] = fix_unicode(artist)
        item['lyrics'] = fix_unicode(lyrics_dir)
        item['release_date'] = fix_unicode(release_date)
        item['recording'] = fix_unicode(recording)
        item['mixing'] = fix_unicode(mixing)
        item['interpolate'] = fix_unicode(interpolate)
        item['cover_art_photo'] = fix_unicode(img_dir)
        item['album'] = fix_unicode(album_name)
        item['views'] = fix_unicode(page_views)
        item['contributors'] = fix_unicode(page_contrib)
        item['video_director1'] = fix_unicode(video_director1)
        item['video_director2'] = fix_unicode(video_director2)
        item['programmer1'] = fix_unicode(programmer1)
        item['programmer2'] = fix_unicode(programmer2)
        item['director_of_photography'] = fix_unicode(director_of_photography)
        item['record_label'] = fix_unicode(record_label)
        item['recorded_at'] = fix_unicode(recorded_at)
        item['samples'] = fix_unicode(samples)
        item['sampled_in'] = fix_unicode(sampled_in)
        item['remix_of'] = fix_unicode(remix_of)
        item['link_to_youtube'] = fix_unicode(link_to_youtube)
        full = [item['producer1'],item['producer2'],item['producer3'],item['producer4'],item['producer5'],item['feature1' ],item['feature2'],item['feature3'],item['feature4'],item['feature5'],item['writer1'],item['writer2'],item['writer3'],item['writer4'],item['writer5'],item['writer6'],item['song_name'],item['artist'],item['lyrics'],item['release_date'],item['recording'],item['mixing'],item['interpolate'],item['cover_art_photo'],item['album'],item['views'],item['contributors'],item['video_director1'],item['video_director2'],item['programmer1'],item['programmer2'],item['director_of_photography'],item['record_label'],item['recorded_at'],item['samples'],item['sampled_in'],item['remix_of']]
        # a = ' '.join(full)
        # if 'more' in a:
        #     embed()
        with open('songs.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(full)        
        yield item
