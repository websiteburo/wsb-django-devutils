.. wsb-django-devutils documentation master file, created by
   sphinx-quickstart on Thu Sep 11 11:04:57 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bienvenue sur la documentation de |project|
===========================================

|project| regroupe divers services et utilitaires transverses utiles pour le développement:

- un backend SMTP `backends.DevEmailBackend` qui redirige tous les mails vers une liste d'adresses spécifiques (par défaut les emails des admins)
- un testrunner `testrurnner.IgnoreTestSuiteRunner` qui permet d'ignorer une liste de paquetages (paramétrable) lors des tests (les tests de certains paquetages Django ou contrib sont soit cassés soit basés sur des pré-requis qui ne sont pas nécessairement valides pour un projet)
- ... (c'est tout pour le moment...)



Autres
------

.. toctree::
   :maxdepth: 2

   doc-generate





Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

