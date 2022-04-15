import scrapy
import string

rootUrl = "https://www.basketball-reference.com"

class StatsSpider(scrapy.Spider):
    name = "stats"

    start_urls = ["{}/players/{}/".format(rootUrl, l) for l in string.ascii_lowercase]

    def parse(self, response):
        # Grab and follow all individual player links
        links = response.css("tbody th a::attr(href)")
        yield from response.follow_all(links, self.__parse_stats)

    def __parse_stats(self, response):
        name = response.css("#info.players #meta div h1 span::text").get()
        player_id = response.url.split("/")[-1].rstrip(".html")
        # rows = response.css("#all_totals-playoffs_totals #switcher_totals-playoffs_totals #div_totals tbody tr")
        rows = response.css("#totals tbody tr")
        if len(rows) == 0:
            self.log("Couldn't find table for {}".format(player_id))
            return

        headers = self.__getHeaders(rows.css("::attr(data-stat)").getall())

        self.log("Starting parsing for {}".format(name))

        for row in rows:
            # Get season
            season = row.css("th ::text").get()
            row_out = { "Name": name, "PlayerId": player_id, "Season": season }
            # Get all other columns
            for index, column in enumerate(row.css("td")):
                row_out[headers[index + 1]] = column.css("::text").get()
            self.log("Player: {}\tSeason: {}".format(row_out['PlayerId'], row_out["Season"]))
            yield row_out

    def __getHeaders(self, all_headers):
        first = all_headers[0]
        for index, header in enumerate(all_headers):
            # Ignore first value
            if index == 0:
                continue
            # Looped back around to the first header
            if first == header:
                return all_headers[:index]
        return all_headers