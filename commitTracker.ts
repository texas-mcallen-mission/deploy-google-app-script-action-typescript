class dataEntry {
    constructor(header, data) {
    for (let i = 0; i < header.length; i++) {
      this[header[i]] = data[i];
    }
  }
}

function splitDataIntoArrayOfObjs_(dataArray, header) {
  let outData = [];
  for (let entry of dataArray) {
    Logger.log(entry);
    let dataLine = new dataEntry(header, entry);
    outData.push(dataLine);
  }
  return outData;
}

function turnArrayOfObjsIntoData_(objArray) {
  let keys = [];
  for (let key in objArray[0]) {
    Logger.log(key);
    keys.push(key);
  }

  let outData = [];
  for (let entry of objArray) {
    let singleEntry = [];
    for (let key of keys) {
      singleEntry.push(entry[key]);
    }
    outData.push(singleEntry);
  }
  return outData;
}

function checkForAndAddCommit() {
  let worksheet = SpreadsheetApp.getActiveSpreadsheet();

  let sheet = worksheet.getSheetByName("commitLog");

  let baseData = sheet.getDataRange().getValues();
  Logger.log(baseData);

  let header = baseData.shift();

  let objArray = splitDataIntoArrayOfObjs_(baseData, header);

  let commits = [];
  for (let entry of objArray) {
    commits.push(entry["commit_sha"]);
  }

  if (commits.includes(GITHUB_DATA.commit_sha)) {
    Logger.log("Commit already there");
  } else {
    objArray.unshift(GITHUB_DATA);
  }

    let finalData = turnArrayOfObjsIntoData_(objArray)
    sendDataToDisplayV3_commitTracker_(header, finalData, sheet)
}

function sendDataToDisplayV3_commitTracker_(header, finalData, sheet) {
  // responsible for actually displaying the data.  Clears first to get rid of anything that might be left over.
  sheet.clearContents();
  sheet.appendRow(header);
  Logger.log(finalData.length);
  Logger.log("adding Header");
  Logger.log(header);
  sheet.getRange(1, 1, 1, header.length).setValues([header]);
  Logger.log("added header, adding data");
  if (finalData.length == 0 || typeof finalData == null) {
    Logger.log("no data, skipping");
    return;
  } else {
    sheet.getRange(2, 1, finalData.length, finalData[0].length).setValues(finalData);
    // Logger.log("Data added, sorting");
    // sheet.getRange(2, 1, finalData.length, header.length)

    // Logger.log("data added")
  }
}