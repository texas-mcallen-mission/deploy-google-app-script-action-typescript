TEST_ENV_VAR='
reportCreator: {
    docIDs: {

        zoneTemplate: "ZONE_TEMPLATE_ID",
        distTemplate: "DISTRICT_TEMPLATE_ID",
        areaTemplate: "AREA_TEMPLATE_ID",
    },
    outputDataSheetName: "Data",
    configPageSheetName: "config",
    kicDataStoreSheetName: "Data",
}
'
/bin/python3 demo/demo.py "$TEST_ENV_VAR"