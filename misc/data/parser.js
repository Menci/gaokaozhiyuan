const cheerio = require('cheerio');
const fs = require('fs');
const path = require('path');

const records = [];
fs.readdirSync(process.argv[2]).map(filename => path.join(process.argv[2], filename)).forEach(file => {
  const $ = cheerio.load(fs.readFileSync(file).toString());
  $('table.tbL2 tr:not(.tbL2title)').each((_, elem) => {
    const record = Array.from($(elem).find('td')).slice(0, -1).map(td => $(td).text());
    record[3] = record[3].replace('分及以上', '');
    records.push(record);
  });
});

console.log(JSON.stringify(records, null, 1));
