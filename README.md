# Chat-TCP-WITH-PYTHON

Python est un excellent langage de programmation pour les réseaux informatiques. Cela nous permet de créer des applications solides très rapidement et facilement. Nous allons donc  implémenter un chat TCP entièrement fonctionnel. Nous aurons un serveur qui hébergera le chat et plusieurs clients qui s'y connecteront et communiqueront entre eux.


# ARCHITECTURE CLIENT-SERVEUR

Pour notre application, nous utiliserons l'architecture client-serveur. Cela signifie que nous aurons plusieurs clients (les utilisateurs) et un serveur central qui héberge tout et fournit les données pour ces clients.


![300px-ClientServerArchitecture1](https://github.com/NomelN/Chat-TCP-WITH-PYTHON/assets/61651276/73c82999-e185-468e-9b64-92e36589bb51)

Par conséquent, nous devrons écrire deux scripts Python. L'un sera pour démarrer le serveur et l'autre pour le client. Nous devrons d'abord exécuter le serveur, afin qu'il y ait un chat auquel les clients puissent se connecter. Les clients eux-mêmes ne vont pas communiquer directement entre eux mais via le serveur central.
