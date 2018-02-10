# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
        # Initialize all variables as None
    producer1 = scrapy.Field()
    producer2 = scrapy.Field()
    producer3 = scrapy.Field()
    producer4 = scrapy.Field()
    producer5 = scrapy.Field()
    feature1  = scrapy.Field()
    feature2 = scrapy.Field()
    feature3 = scrapy.Field()
    feature4 = scrapy.Field()
    feature5 = scrapy.Field()
    writer1 = scrapy.Field()
    writer2 = scrapy.Field()
    writer3 = scrapy.Field()
    writer4 = scrapy.Field()
    writer5 = scrapy.Field()
    writer6 = scrapy.Field()
    song_name = scrapy.Field()
    artist = scrapy.Field()
    artist1 = scrapy.Field()
    artist2  = scrapy.Field()
    artist3 = scrapy.Field()
    lyrics = scrapy.Field()
    release_date = scrapy.Field()
    recording = scrapy.Field()
    mixing = scrapy.Field()
    interpolate = scrapy.Field()
    cover_art_photo = scrapy.Field()
    album = scrapy.Field()
    views = scrapy.Field()
    contributors = scrapy.Field()
    video_director1 = scrapy.Field()
    video_director2 = scrapy.Field()
    programmer1 = scrapy.Field() 
    programmer2 = scrapy.Field()
    director_of_photography = scrapy.Field()
    record_label = scrapy.Field()
    recorded_at = scrapy.Field()
    samples = scrapy.Field()
    sampled_in = scrapy.Field()
    remix_of = scrapy.Field()
    link_to_youtube = scrapy.Field()
