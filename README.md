<!--
N.B.: This README was automatically generated by <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
It shall NOT be edited by hand.
-->

# YunoRunner for YunoHost

[![Integration level](https://apps.yunohost.org/badge/integration/yunorunner)](https://ci-apps.yunohost.org/ci/apps/yunorunner/)
![Working status](https://apps.yunohost.org/badge/state/yunorunner)
![Maintenance status](https://apps.yunohost.org/badge/maintained/yunorunner)

[![Install YunoRunner with YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=yunorunner)

*[Read this README in other languages.](./ALL_README.md)*

> *This package allows you to install YunoRunner quickly and simply on a YunoHost server.*  
> *If you don't have YunoHost, please consult [the guide](https://yunohost.org/install) to learn how to install it.*

## Overview

Yunorunner is a CI server for YunoHost apps.

It is based on Incus / LXC and uses [package_check](https://github.com/YunoHost/package_check).

This package allows you to self-host a yunorunner instance with the ability to also use it in your own github repositories. The process is:
- Create a github personal access token in github developer settings and grant it these permissions: read metadata, read/write to commit statuses and pull requests
- Clone YunoHost/apps or add a apps.toml file in your repo with necessary details (example in apps.toml of YunoHost/apps.toml)
- Install the app and provide the token, select domain, add the repo for apps.toml
- Create a webhook in github that points to https://example.tld/github, make it trigger on "Issue Comment" and "Pull Request"

**Shipped version:** 2024.12.10~ynh1

## Screenshots

![Screenshot of YunoRunner](./doc/screenshots/screenshot.png)

## Documentation and resources

- Upstream app code repository: <https://github.com/YunoHost/yunorunner>
- YunoHost Store: <https://apps.yunohost.org/app/yunorunner>
- Report a bug: <https://github.com/YunoHost-Apps/yunorunner_ynh/issues>

## Developer info

Please send your pull request to the [`testing` branch](https://github.com/YunoHost-Apps/yunorunner_ynh/tree/testing).

To try the `testing` branch, please proceed like that:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/yunorunner_ynh/tree/testing --debug
or
sudo yunohost app upgrade yunorunner -u https://github.com/YunoHost-Apps/yunorunner_ynh/tree/testing --debug
```

**More info regarding app packaging:** <https://yunohost.org/packaging_apps>
