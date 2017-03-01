Introduction
============

Le package *wsb-django-devutils* regroupe divers services et utilitaires transverses utiles pour le développement:

- un backend SMTP `backends.DevEmailBackend` qui redirige tous les mails vers une liste d'adresses spécifiques (par défaut les emails des admins)
- un testrunner `testrurnner.IgnoreTestSuiteRunner` qui permet d'ignorer une liste de paquetages (paramétrable) lors des tests (les tests de certains paquetages Django ou contrib sont soit cassés soit basés sur des pré-requis qui ne sont pas nécessairement valides pour un projet)
- ... (c'est tout pour le moment...)


Installation
============

wsb-django-devutils est packagé pour être installable via pip::

    pip install https://github.com/websiteburo/wsb-django-devutils.git@master

Configuration et utilisation
============================

Voir la documentation détaillé dans le répertoire ``docs/``.

Générer de la documentation au format HTML
==========================================

La documentation se trouve dans le dossier ``docs/``. Elle est rédigée
au format rst et utilise `Sphinx <http://sphinx-doc.org/>`_.

Pour la générer, il faut au préalable installer sphinx et les
dépendances du projet dans l'environnement python en cours.

Ensuite::

    cd docs/
    make html


La documentation se touvera dans le dossier ``docs/_build/``. Le point
d'entrée est (sans surprise) le fichier ``index.html``.


Mais elle est même pas responsive cette doc !
---------------------------------------------

Le thème utilisé par défaut est le thème "nature" fourni avec sphinx.
Toutefois il est possible d'utiliser le super thème responsive de `Read
the Docs <http://read-the-docs.readthedocs.org>`_ juste en
l'installant dans l'environnement ::

    pip install sphinx_rtd_theme
    make clean && make html
