import { writeFileSync, readFileSync } from "fs";

async function updateTimestamp() {
    const timestamp = new Date().toISOString(); // ISO format for universal readability
    const content = `# GitHub Workflow Action: Timestamp Updater

This repository is mainly for DecryptorX_Stealer - a cyberSecurity Repository that mainly focuses on the learning of cybersecurity. This contains a GitHub Action workflow that automatically updates the timestamp in this README.md file to reflect the last time the workflow ran.

## Description

This GitHub Action demonstrates automated timestamp updates for repositories, showcasing how to keep your documentation up to date dynamically.
- Configure the GitHub Action workflow to run on a schedule or on certain events.
- Each time the workflow runs, the \`README.md\` file will automatically update with the latest timestamp.

## Last Updated

> _Last Updated: ${timestamp} (in UTC)_

---

`;

    writeFileSync("README.md", content, { encoding: "utf8" });

    console.log("README.md has been updated with the latest timestamp.");
}

updateTimestamp();
