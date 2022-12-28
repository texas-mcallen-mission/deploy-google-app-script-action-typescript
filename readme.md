# Google AppsScript Deployment Manager

<!--  WYLO: FIGURE OUT A GOOD NAME FOR THIS PROJECT -->

*A fairly simple and pretty robust way to get your code from GitHub to a Google AppsScript project that all happens in the cloud.*

This is a project that got started because we use Google AppsScript a *lot*- we've built a [massive project](githu.com/texas-mcallen-mission/key-indicator-system) on top of it.  Google's internal editor has some problems- it doesn't support TypeScript (which seems like a necessity for a project as large as ours), it's nowhere near as powerful as vsCode is, and it doesn't have a nice dark mode.  To get around these shortcomings, we adapted somebody else's work and made this thing. It's built off of [CLASP](https://github.com/google/clasp), which lets you use your favorite desktop editor to do things, but instead of running CLASP from your computer, you do it *in the cloud* (isn't that cool?)

This is built off of [deploy-google-app-script-action](https://GitHub.com/ericanastas/deploy-google-app-script-action) written by [ericanastas](https://github.com/ericanastas) but has some significant changes made to it to make it easier to use, get started with, more powerful, and more reliable.

There's a minimum viable project demo available here: [deploy-tester](https://github.com/texas-mcallen-mission/deploy-tester) that has a guide on how to get the absolute bare minimum necessary set up to get something into AppScript.

Part of the reason that we're using this instead of something that uses Google Cloud Platform is that our org doesn't use GCP.

## Getting Started

 - see the wiki, or [the demo repo](https://GitHub.com/texas-mcallen-mission/deploy-demo/)

# Inputs

| Input Value | Description | Required | Default Value |
| :---: | :--- | :---: | :---: |
| CLASP_TOKEN_VALUE |  |  true |  |
| CLASP_TOKEN_NAME | ``clasp.rc`` token name - used to update the access token and keep it alive. |  false | ``CLASPRC_JSON`` |
| REPO_ACCESS_TOKEN | personal access token that has secrets modifying scopes |  true |  |
| USES_ORG_SECRET | Updates org secret instead of repo secret if set to true |  false | FALSE |
| ORG_VISIBILITY | only used if ``USES_ORG_SECRET`` is true, for changing what repositories have access to the value. | false | ``all`` |
| SCRIPT_ID | script id for script to be modified |  true |  |
| PARENT_ID | parent id |  false |  |
| DEPLOYMENT_ID | for larger deployments and version control inside of gas |  false |  |
| CONFIG_DATA | json-based config data to pass into git-info.js |  false |  |
| sha | hash of git commit. |  false |  |
| event_name | if scheduled, used to avoid uploading code and just refresh clasprc |  false |  |
| actor | for git info |  false |  |
| job | for git info |  false |  |
| repository | for git info |  false |  |
| ref_name | for git info |  false |  |