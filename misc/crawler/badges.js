const request = require('request-promise');
const fs = require('fs-extra');
const path = require('path');
const schoolList = JSON.parse(fs.readFileSync(process.argv[2]));
const async = require('async');
const Promise = require('bluebird');

const targetDir = process.argv[3];
fs.ensureDirSync(targetDir);

async.parallelLimit(Object.keys(schoolList).map(
  schoolName => async () => {
    const schoolID = schoolList[schoolName].school_id;
    console.log(`Start schoolID = '${schoolID}', schoolName = '${schoolName}'.`);
    for (let i = 1; ; i++) {
      try {
        await fs.writeFile(path.join(targetDir, `${schoolID}.jpg`), await request(`https://static-data.eol.cn/upload/logo/${schoolID}.jpg`, { encoding: null }));
        break;
      } catch (e) {
        console.log(`Error caught: '${e}', retrying for ${i} time(s).`);
        await Promise.delay(500);
      }
    }
    console.log(`Finished schoolID = '${schoolID}', schoolName = '${schoolName}'.`);
  }
), 50);
