from django.db.models import Manager

class PostManager(Manager):
    
    def get_published_posts(self):
        '''
            Get all publsihed posts 
        '''
        return self.filter(status='P')

    
    def get_recent_posts(self):
        '''
            Get the recent 10 posts 
        '''
        return self.order_by('-publish')[:10]
    

    def get_most_clapped_posts(self):
        '''
            Get most 10 clapped posts 
        '''
        return self.order_by('-clapped')[:10]