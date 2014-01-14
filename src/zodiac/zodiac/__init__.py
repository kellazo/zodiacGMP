# -*- coding: utf-8 -*-
from pyramid.config import Configurator
from resources import Root
import views
import pyramid_jinja2
import os

__here__ = os.path.dirname(os.path.abspath(__file__))


def make_app():
    """ This function returns a Pyramid WSGI application.
    """
    settings = {}
    settings['mako.directories'] = os.path.join(__here__, 'templates')
    config = Configurator(root_factory=Root, settings=settings )
    #config.add_renderer('.jinja2', pyramid_jinja2.Jinja2Renderer)
    #config.add_view(views.my_view,
     #               context=Root,
      #              renderer='mytemplate.jinja2')
    
    #per afegir una nova pagina
    #home
    # afegim la URL "/" a la que accedim amb "http://localhost:8080/" 
    config.add_route( "root", "/" ) # root=view, /=URL
    config.add_view( views.root_view, route_name="root", renderer="root.mako" )
    
    #el meu zodiac
    # afegim la URL "/elmeu" a la que accedim amb "http://localhost:8080/elmeu"
    config.add_route( "elmeu", "/elmeu" ) # elmeu=view, /elmeu=URL
    config.add_view( views.elmeu_view, route_name="elmeu", renderer="elmeu.mako" )
    
    
    config.add_static_view(name='static',
                           path=os.path.join(__here__, 'static'))
    return config.make_wsgi_app()

application = make_app()
