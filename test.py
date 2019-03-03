from observer import Blog, Subscriber

blog = Blog(['anime', 'Japanese'])

lisa = Subscriber('Lisa')
bob = Subscriber('Bob')

blog.register('anime', lisa)
blog.register('Japanese', lisa)
blog.register('anime', bob)

blog.dispatch('Japanese', "New post: Teach yourself Japanese in 21 days")
blog.unregister('anime', lisa)
blog.dispatch('anime', "New episode of Black Clover aired.")
