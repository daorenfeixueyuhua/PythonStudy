# URL完全匹配
# / index
# URL模糊匹配
# / post /\d +
# URL带组匹配
# / post.(\d +)

import web

urls = (
    '/index', 'index',
    '/blog/\b+', 'blog',
    '/(.*)', 'hello',
)

app = web.application(urls, globals())


class index:
    def GET(self):
        return "hello method"

class blog:
    def GTE(self):
        return "blog method"

    def POST(self):
        return "blog post method"

class hello:
    def GET(self, name):
        return "hello " + name


if __name__ == '__main__':
    app.run()