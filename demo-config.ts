// This is just a demonstration for how one could use a config file with an additional one in git-info

let INTERNAL_CONFIG = {
    
    // docIds
    docIds_kicFormId: "KIC_FORM_ID", //The Document ID of the Key Indicators for Conversion Report Google Form (where missionaries submit their KICs every Sunday).    gcopy:'1CbCGdXXjPmQmpLKJAaER0cSYSGrb3ES3y2XGpr3czEw'    live:'1Zc-3omEIjAeQrmUxyG8YFk4PdnPf37XiFy3PRK2cP8g'

    reportCreator: {
        docIDs: {

            zoneTemplate: "ZONE_TEMPLATE_ID",
            distTemplate: "DISTRICT_TEMPLATE_ID",
            areaTemplate: "AREA_TEMPLATE_ID",
        },
        outputDataSheetName: "Data",
        configPageSheetName: "config",
        kicDataStoreSheetName: "Data",
    },

    // general

    general_areaNameQuestionTitle: "Area Name",

    general_deleteOldResponsesAgeLimit: 0, //The max age, in days, of a response before it is deleted (from the Form, not the Google Sheet). If set to 0, old responses will never be deleted.

    // dataFlow

    dataFlow_skipMarkingPulled: false, //Stops marking Form Responses as having been pulled into the data sheet

    dataFlow_skipMarkingDuplicates: false, //TODO Re-implement?

    dataFlow_freezeContactData: false,

    dataFlow_formColumnsToExcludeFromDataSheet: [
        "responsePulled",
        "submissionEmail",
    ],

    dataFlow_forceAreaIdReloadOnUpdateDataSheet: false,

    dataFlow_areaId_cacheExpirationLimit: 1800, //Maximum time in seconds before the cache gets reset

};

const CONFIG = {
    ...INTERNAL_CONFIG,
    ...GITHUB_SECRET_DATA
    // this way, all the data written to GITHUB_SECRET_DATA just winds up in config
