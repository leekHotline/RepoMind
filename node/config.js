import { readFile, writeFile } from "fs/promises";


async function updateConfig(){
    const config = {"version": "1.0.0", "debug": true};

    await writeFile('./config.json', JSON.stringify(config, null , 2));
    const  raw = await readFile('./config.json','utf-8');
    const parsed = JSON.parse(raw);

    console.log('Config loaded:', parsed);

}

updateConfig();