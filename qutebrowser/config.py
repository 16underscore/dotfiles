config.load_autoconfig(False)

c.changelog_after_upgrade = 'never'

c.completion.cmd_history_max_items = 15
c.completion.web_history.max_items = 0

c.content.autoplay = False
c.content.blocking.method = 'adblock'
c.content.blocking.adblock.lists = [
	"https://easylist.to/easylist/easylist.txt",
	"https://easylist.to/easylist/easyprivacy.txt",
	"https://easylist.to/easylist/fanboy-social.txt",
	"https://easylist-downloads.adblockplus.org/abp-filters-anti-cv.txt",
	"https://pgl.yoyo.org/adservers/serverlist.php?showintro=0;hostformat=hosts",
	"https://secure.fanboy.co.nz/fanboy-annoyance.txt",
	"https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
	"https://github.com/uBlockOrigin/uAssets/raw/master/filters/legacy.txt",
	"https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt",
	"https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2020.txt",
	"https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2021.txt",
	"https://github.com/uBlockOrigin/uAssets/raw/master/filters/badware.txt",
	"https://github.com/uBlockOrigin/uAssets/raw/master/filters/privacy.txt",
	"https://github.com/uBlockOrigin/uAssets/raw/master/filters/badlists.txt",
	"https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances.txt",
	"https://github.com/uBlockOrigin/uAssets/raw/master/filters/resource-abuse.txt",
	"https://github.com/uBlockOrigin/uAssets/raw/master/filters/unbreak.txt"
]
c.content.javascript.alert = False
c.content.notifications.enabled = False
c.content.pdfjs = True

c.scrolling.bar = 'never'

c.tabs.title.alignment = 'center'
c.tabs.title.format = '{current_title}'
c.tabs.tooltips = False

c.url.default_page = 'about:blank'
c.url.searchengines = {
	'DEFAULT': 'https://duckduckgo.com/?q={}',
	'ac': 'https://adventofcode.com/{}',
	'al': 'https://archlinux.org/packages/?q={}',
	'cr': 'https://crates.io/search?q={}',
	'dc': 'https://www.dict.cc/?s={}',
	'iv': 'https://invidious.lunar.icu/search?q={}'
	'mw': 'https://minecraft.fandom.com/wiki/{}',
	'os': 'https://odysee.com/$/search?q={}',
	'rd': 'https://reddit.com/r/{}',
	'lh': 'localhost:{}'
}

c.window.title_format = 'qutebrowser'

import twoam.draw
twoam.draw.purple(c)

config.bind('z', 'hint links spawn mpv --fs --volume=60 {hint-url}')
