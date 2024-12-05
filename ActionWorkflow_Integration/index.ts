import { writeFileSync } from "fs";

async function updateTimestamp() {
    const timestamp = new Date().toLocaleString();
    const content = `\n> _Last Updated: ${timestamp} (in GMT)_\n`;
    writeFileSync("README.md", content);
}

updateTimestamp();
