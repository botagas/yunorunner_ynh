<!--
Nota bene : ce README est automatiquement généré par <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Il NE doit PAS être modifié à la main.
-->

# YunoRunner pour YunoHost

[![Niveau d’intégration](https://apps.yunohost.org/badge/integration/yunorunner)](https://ci-apps.yunohost.org/ci/apps/yunorunner/)
![Statut du fonctionnement](https://apps.yunohost.org/badge/state/yunorunner)
![Statut de maintenance](https://apps.yunohost.org/badge/maintained/yunorunner)

[![Installer YunoRunner avec YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=yunorunner)

*[Lire le README dans d'autres langues.](./ALL_README.md)*

> *Ce package vous permet d’installer YunoRunner rapidement et simplement sur un serveur YunoHost.*  
> *Si vous n’avez pas YunoHost, consultez [ce guide](https://yunohost.org/install) pour savoir comment l’installer et en profiter.*

## Vue d’ensemble

Yunorunner is a CI server for YunoHost apps.

It is based on Incus / LXC and uses [package_check](https://github.com/YunoHost/package_check).


**Version incluse :** 2024.12.10~ynh1

## Captures d’écran

![Capture d’écran de YunoRunner](./doc/screenshots/screenshot.png)

## Documentations et ressources

- Dépôt de code officiel de l’app : <https://github.com/YunoHost/yunorunner>
- YunoHost Store : <https://apps.yunohost.org/app/yunorunner>
- Signaler un bug : <https://github.com/YunoHost-Apps/yunorunner_ynh/issues>

## Informations pour les développeurs

Merci de faire vos pull request sur la [branche `testing`](https://github.com/YunoHost-Apps/yunorunner_ynh/tree/testing).

Pour essayer la branche `testing`, procédez comme suit :

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/yunorunner_ynh/tree/testing --debug
ou
sudo yunohost app upgrade yunorunner -u https://github.com/YunoHost-Apps/yunorunner_ynh/tree/testing --debug
```

**Plus d’infos sur le packaging d’applications :** <https://yunohost.org/packaging_apps>
