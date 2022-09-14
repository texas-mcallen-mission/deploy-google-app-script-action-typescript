# GASmantis

<!--  WYLO: FIGURE OUT A GOOD NAME FOR THIS PROJECT -->

*A fairly simple and pretty robust way to get your code from GitHub to a Google AppsScript project.*

This is a project that got started because we use Google AppsScript a *lot*- we've built a [massive project](githu.com/texas-mcallen-mission/key-indicator-system) on top of it.  The internal editor has some problems- it doesn't support TypeScript (which has come in *really* handy), it's nowhere near as powerful as vsCode is, and it doesn't have a nice dark mode.  To get around these shortcomings, we adapted somebody else's work and made this thing. It's built off of [CLASP](https://github.com/google/clasp), which lets you use your favorite desktop editor to do things, but instead of running CLASP from your computer, you do it *in the cloud* (isn't that cool?)

This is built off of [deploy-google-app-script-action](https://GitHub.com/ericanastas/deploy-google-app-script-action) written by [ericanastas](https://github.com/ericanastas) but has some significant changes made to it to make it easier to use, get started with, more powerful, and more reliable.

There's a minimum viable project demo available here: [deploy-tester](https://github.com/texas-mcallen-mission/deploy-tester) that has a guide on how to get the absolute bare minimum necessary set upto get something into AppScript.

Part of the reason that we're using this instead of something that uses Google Cloud Platform is that our org doesn't use GCP.

## Getting Started

 - see the wiki, or [the demo repo](https://GitHub.com/texas-mcallen-mission/deploy-demo/)