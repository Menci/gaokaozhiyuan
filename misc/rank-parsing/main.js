const cheerio = require('cheerio');
const fs = require('fs');
const path = require('path');

const dataDir = 'data';

const files = fs.readdirSync('data').map(filename => ({
  path: path.join(dataDir, filename),
  id: filename.substr(0, 4),
  name: filename.substring(5, filename.length - 5),
  items: []
}));

for (file of files) {
  const $ = cheerio.load(fs.readFileSync(file.path));
  delete file.path;

  let level = '';
  $('table[bgcolor="#c2d8e5"] tr').each((i, tr) => {
    const levelCell = $(tr).find('td:nth-last-child(2)');
    if (levelCell.length > 0) level = levelCell.text().trim();
    const idAndName = $(tr).find('td:nth-last-child(1)').text().split(String.fromCharCode(160)).join(' ').split(' ').filter(x => x);
    file.items.push({
      level,
      schoolID: idAndName[0],
      schoolName: idAndName[1]
    });
  });
}

console.log(JSON.stringify(files, null, 1));
