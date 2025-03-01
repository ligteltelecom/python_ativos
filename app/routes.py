from mvc_flask import Router

Router.get('/', 'home#index')
Router.get('/ping', 'home#ping')
#Router.post('/auth/register', 'user#register_user')