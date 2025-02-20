Yunorunner is a CI server for YunoHost apps.

It is based on Incus / LXC and uses [package_check](https://github.com/YunoHost/package_check).

This package allows you to self-host a yunorunner instance with the ability to also use it in your own github repositories. The process is:
- Create a github personal access token in github developer settings and grant it these permissions: read metadata, read/write to commit statuses and pull requests
- Clone YunoHost/apps and add necessary details within apps.toml file in your repo
- Install the app and provide the token, select domain, add the repo for apps.toml
- Create a webhook in github that points to https://example.tld/github, make it trigger on "Issue Comment" and "Pull Request"
- (OPTIONAL) Edit your README and add the status/integration badges from your server as well

PATH for status: `/api/badge/<app_name>/status`

PATH for integration: `/api/badge/<app_name>/integration`

Example integration / status badge code: 
```
[![Integration level](https://img.shields.io/endpoint?url=https://sub.domain.tld/api/badge/<app_name>/integration)](https://ci-apps.yunohost.org/ci/apps/<app_name>/)`
![Working status](https://img.shields.io/endpoint?url=https://sub.domain.tld/api/badge/<app_name>/status)
