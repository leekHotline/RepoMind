import {readFile, writeFile} from 'fs/promises'

async function main(){

    await writeFile('hello.txt', 'hello nodejs');
    const content = await readFile("hello.txt", 'utf-8');

    console.log("content is:",content);

}

main()