class TweetAuthor():
    def __init__(self, data):
        self.author_id = data['id']
        self.name = data['name']
        self.username = data['screen_name']
        self.location = data['location']
        self.followers_count = data['followers_count']
        self.created_at = data['created_at']
        self.timezone = data['time_zone']
        self.lang = data['lang']
        self.profile_image_url = data['profile_image_url']
        self.url = data['url']
        self.description = data['description']

    def __repr__(self):
        from pprint import pformat
        return pformat(vars(self), indent=8)
