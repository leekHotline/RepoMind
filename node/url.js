import {URL} from 'url'

const myURL = new URL('https://example.com/search?q=node&lang=zh'
)

console.log(myURL.searchParams.get('q'));
console.log(myURL.searchParams.get('lang'));