import { writeFileSync } from "fs";

async function updateTimestamp() {
  const timestamp = new Date().toLocaleString();

  const content = `
> _Last Updated: ${timestamp} (in GMT)_
`;

  writeFileSync("README.md", content);
}

updateTimestamp();
