import twint

config = twint.Config()
config.Username = 'github'
config.Lang = "en"
twint.run.Search(config)
