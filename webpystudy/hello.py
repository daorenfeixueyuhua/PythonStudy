import web

urls = (
    '/(.*)', 'index',
)

app = web.application(urls, globals())


class index:

    def GET(self, name):
        return "hello, world!"+name


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
