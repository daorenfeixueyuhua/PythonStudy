import configparser
cfg = configparser.ConfigParser()
print(cfg)
cfg.read('imooc.txt')
for se in cfg.sections():
    print(se)
    print(cfg.items(se))

cfg.set('userinfo','pwd','123')
for se in cfg.sections():
    print(se)
    print(cfg.items(se))

cfg.set('userinfo','email','pengda.com')
for se in cfg.sections():
    print(se)
    print(cfg.items(se))

cfg.remove_option('userinfo','email')
for se in cfg.sections():
    print(se)
    print(cfg.items(se))
print(cfg.keys())