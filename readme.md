# Github -> AppsScript Bridge

<!--  WYLO: FIGURE OUT A GOOD NAME FOR THIS PROJECT -->

*Send your code directly from Github to Google's AppsScript environment.*

<details>
  <summary> Why does this exist? </summary>
  
This is a project that got started because we use Google AppsScript a *lot*- we've built a [massive project](githu.com/texas-mcallen-mission/key-indicator-system) on top of it.  Google's internal editor has some problems- it doesn't support TypeScript (which seems like a necessity for a project as large as ours), it's nowhere near as powerful as vsCode is, and it doesn't have a nice dark mode.  To get around these shortcomings, we adapted somebody else's work and made this thing. It's built off of [CLASP](https://github.com/google/clasp), which lets you use your favorite desktop editor to do things, but instead of running CLASP from your computer, you do it *in the cloud* (isn't that cool?)

Part of the reason that we're using this instead of something that uses Google Cloud Platform is that our org doesn't use GCP, but we do have access to AppsScript.

</details>





There's a minimum viable project demo available here: [deploy-tester](https://github.com/texas-mcallen-mission/deploy-tester) that has a guide on how to get the absolute bare minimum necessary set up to get something into AppScript.


## Getting Started

 <!-- - see the wiki, or [the demo repo](https://github.com/texas-mcallen-mission/deploy-tester/) -->

Copy ``new-reusable.yml`` into your own project, change the branch name to whatever branch you're working on.

### Using the Default Workflow

 1. Create a personal access token with read and write access to secrets. 
  [Create a secret](https://docs.github.com/en/actions/security-guides/encrypted-secrets) named ``REPO_ACCESS_TOKEN`` and store it there.
 2. Install [Clasp](https://github.com/google/clasp) locally, and log in.
    * *if you haven't used clasp before, [here's a tutorial](https://codelabs.developers.google.com/codelabs/clasp#0)*
 3. Go to your home directory, and find .clasprc.json.  Copy the contents of the file.
 4. Create a secret named ``CLASPRC_JSON``, and paste all the contents from step 3 in here.
 5. Create a secret named ``SCRIPT_ID`` and put your script id in it.
    * *you can technically replace ``${{ secrets.SCRIPT_ID }}`` with your script id, but this isn't recommended as it could be less secure.
 6. After that's all saved, you should be able to run your workflow in your repository and see a file named ``aaa-git-info`` show up in your appsscript editor.


## Inputs

| Input Value | Description | Required | Default Value |
| :---: | :--- | :---: | :---: |
| CLASP_TOKEN_VALUE | Clasp login token value. |  true |  |
| CLASP_TOKEN_NAME | ``clasprc`` token name - used to update the access token and keep it alive.<sup>1</sup> |  false | ``CLASPRC_JSON`` |
| REPO_ACCESS_TOKEN | Personal access token that has secrets modifying scopes.<sup>2</sup>  |  true |  |
| USES_ORG_SECRET | Updates org secret instead of repo secret if set to true |  false | FALSE |
| ORG_VISIBILITY | Only used if ``USES_ORG_SECRET`` is true, for changing what repositories have access to the value. | false | ``all`` |
| SCRIPT_ID | Script id for script to be modified |  true |  |
| PARENT_ID | Parent id - if you have a project connected to a Google Sheet, for instance, put the id of that sheet here.  Works with Docs, Slides, & Sheets at the very least. |  false |  |
| DEPLOYMENT_ID | For larger deployments and version control inside of AppsScript. |  false |  |
| CONFIG_DATA | JSON config data to pass into git-info.js<sup>3</sup> |  false |  |

<sup>

1. *This is mostly useful to give a more meaningful name if you have a ton of secrets in your project.*

2. *For organizations, needs R/W access to repo and org secrets.*

3. *JSON format, but don't encapsulate it. Should look something like this:*
    ```js
    config_value: "string",
    config_submodule: {
        demoThingy1: false
    }
    ```

</sup>

## Demo Workflows

```yaml
uses: texas-mcallen-mission/deploy-google-app-script-action-typescript/@v3.0.1
```

<table>
<tr>
<td> Clasp token stored on repo </td>
<td> 

```yaml
with:
  CLASP_TOKEN_VALUE: ${{ secrets.CLASPRC_JSON }}
  CLASP_TOKEN_NAME: 'CLASPRC_JSON'
  REPO_ACCESS_TOKEN: ${{ secrets.REPO_ACCESS_TOKEN }}
  SCRIPT_ID: ${{ secrets.SCRIPT_ID }}

```

</td>
</tr>
<tr>
<td> Clasp token stored in org </td>
<td>

```yaml
with:
  CLASP_TOKEN_VALUE: ${{ secrets.CLASPRC_JSON }}
  CLASP_TOKEN_NAME: 'CLASPRC_JSON'
  REPO_ACCESS_TOKEN: ${{ secrets.REPO_ACCESS_TOKEN }}
  USES_ORG_SECRET: true
  ORG_VISIBILITY: all # optional, default all.
  SCRIPT_ID: ${{ secrets.SCRIPT_ID }}
```

</td>
</tr>
</table>


## Attribution

This is built off of [deploy-google-app-script-action](https://GitHub.com/ericanastas/deploy-google-app-script-action) written by [ericanastas](https://github.com/ericanastas) but has some significant changes made to it to make it easier to use, get started with, more powerful, and more reliable.