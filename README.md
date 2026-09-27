# AA EVE Online SDE Admin Status Page

[![Version](https://img.shields.io/pypi/v/aa-eveonline-sde-admin-page?label=release)](https://pypi.org/project/aa-eveonline-sde-admin-page/)
[![License](https://img.shields.io/badge/license-GPLv3-green)](https://pypi.org/project/aa-eveonline-sde-admin-page/)
[![Python](https://img.shields.io/pypi/pyversions/aa-eveonline-sde-admin-page)](https://pypi.org/project/aa-eveonline-sde-admin-page/)
[![Django](https://img.shields.io/pypi/djversions/aa-eveonline-sde-admin-page?label=django)](https://pypi.org/project/aa-eveonline-sde-admin-page/)
![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/ppfeufer/aa-eveonline-sde-admin-page/master.svg)](https://results.pre-commit.ci/latest/github/ppfeufer/aa-eveonline-sde-admin-page/master)
[![Code Style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](http://black.readthedocs.io/en/latest/)
[![Automated Checks](https://github.com/ppfeufer/aa-eveonline-sde-admin-page/actions/workflows/automated-checks.yml/badge.svg)](https://github.com/ppfeufer/aa-eveonline-sde-admin-page/actions/workflows/automated-checks.yml)
[![codecov](https://codecov.io/gh/ppfeufer/aa-eveonline-sde-admin-page/branch/master/graph/badge.svg?token=GNE88NUAKK)](https://codecov.io/gh/ppfeufer/aa-eveonline-sde-admin-page)
[![Translation status](https://weblate.ppfeufer.de/widget/alliance-auth-apps/aa-eveonline-sde-admin-page/svg-badge.svg)](https://weblate.ppfeufer.de/engage/alliance-auth-apps/)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](https://github.com/ppfeufer/aa-eveonline-sde-admin-page/blob/master/CODE_OF_CONDUCT.md)
[![Discord](https://img.shields.io/discord/399006117012832262?label=discord)](https://discord.gg/fjnHAmk)
[![Alliance Auth Compatibility](https://img.shields.io/badge/Alliance_Auth-v5-brightgreen)](https://gitlab.com/allianceauth/allianceauth)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/N4N8CL1BY)

Simple status page for EVE Online SDE data, gathered from Django EVE Online SDE.

> [!NOTE]
>
> This app requires [Django EVE Online SDE](https://pypi.org/project/django-eveonline-sde/) to be installed and configured in your Alliance Auth installation.

______________________________________________________________________

<!-- mdformat-toc start --slug=github --maxlevel=6 --minlevel=2 -->

- [Installation](#installation)
  - [Bare Metal Installation](#bare-metal-installation)
    - [Step 1: Install the App](#step-1-install-the-app)
    - [Step 2: Update Your AA Settings](#step-2-update-your-aa-settings)
- [Docker Installation](#docker-installation)
  - [Step 1: Add the App](#step-1-add-the-app)
  - [Step 2: Update Your AA Settings](#step-2-update-your-aa-settings-1)
  - [Step 3: Build Auth and Restart Your Containers](#step-3-build-auth-and-restart-your-containers)
- [Updating](#updating)
  - [Bare Metal Installation](#bare-metal-installation-1)
  - [Docker Installation](#docker-installation-1)
- [Accessing the Admin Status Page](#accessing-the-admin-status-page)

<!-- mdformat-toc end -->

______________________________________________________________________

![EVE SDE Status Page](https://raw.githubusercontent.com/ppfeufer/aa-eveonline-sde-admin-page/refs/heads/master/docs/images/aa-eveonline-sde-admin-page.jpg "EVE SDE Status Page")

## Installation<a name="installation"></a>

### Bare Metal Installation<a name="bare-metal-installation"></a>

#### Step 1: Install the App<a name="step-1-install-the-app"></a>

Make sure you're in the virtual environment (venv) of your Alliance Auth installation.
Then install the latest version:

```bash
pip install aa-eveonline-sde-admin-page==0.0.1
```

#### Step 2: Update Your AA Settings<a name="step-2-update-your-aa-settings"></a>

Configure your AA settings in your `local.py` as follows:

```python
INSTALLED_APPS += [
    # ...
    "eve_sde",  # This should already be here if you have Django EVE Online SDE installed
    "aa_eveonline_sde_admin_page",
    # ...
]

# This line right below the `INSTALLED_APPS` list, and only if not already added for another app
INSTALLED_APPS = ["modeltranslation"] + INSTALLED_APPS
```

Now, restart your Auth.

## Docker Installation<a name="docker-installation"></a>

#### Step 1: Add the App<a name="step-1-add-the-app"></a>

Add the app to your `conf/requirements.txt`:

```text
aa-eveonline-sde-admin-page==0.0.1
```

#### Step 2: Update Your AA Settings<a name="step-2-update-your-aa-settings-1"></a>

Configure your AA settings (`conf/local.py`) as follows:

```python
INSTALLED_APPS += [
    # ...
    "eve_sde",  # This should already be here if you have Django EVE Online SDE installed
    "aa_eveonline_sde_admin_page",
    # ...
]

# This line right below the `INSTALLED_APPS` list, and only if not already added for another app
INSTALLED_APPS = ["modeltranslation"] + INSTALLED_APPS
```

#### Step 3: Build Auth and Restart Your Containers<a name="step-3-build-auth-and-restart-your-containers"></a>

```shell
docker compose build --no-cache
docker compose --env-file=.env up -d
```

## Updating<a name="updating"></a>

### Bare Metal Installation<a name="bare-metal-installation-1"></a>

To update your existing installation of AFAT, first enable your
virtual environment (venv) of your Alliance Auth installation.
Then run the following command to update the app:

```bash
pip install aa-eveonline-sde-admin-page==0.0.1
```

And restart your Auth.

### Docker Installation<a name="docker-installation-1"></a>

To update your existing installation of AFAT, all you need to do is update the
respective line in your `conf/requirements.txt` file to the latest version.

```text
aa-eveonline-sde-admin-page==0.0.1
```

Then rebuild your containers:

```shell
docker compose build --no-cache
docker compose --env-file=.env up -d
```

## Accessing the Admin Status Page<a name="accessing-the-admin-status-page"></a>

Access to the status page is restricted to users with the `eve_sde.admin_access`
permission. You can assign this permission to a user or group via the Django admin
interface.
