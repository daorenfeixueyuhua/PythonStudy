import requests


r = requests.get('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1548139618097&di=bdea24e280610d6b6e79e53932de8d91&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20181220%2Fd21b3a01b4c5487ea28d2d0132e8c474.jpeg')
with open('resources/bdea24e280610d6b6e79e53932de8d91.jpg', 'wb') as f:
    f.write(r.content)
