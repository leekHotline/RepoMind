import 'dotenv/config';

const PORT = process.env.PORT;
const DEBUG = process.env.DEBUG ;
const LOG_LEVEL = process.env.LOG_LEVEL;
const VERSION = process.env.VERSION;
const API_KEY = process.env.API_KEY;

console.log(`Server running on port: ${PORT}, Debug Mode : ${DEBUG}, Log Level: ${LOG_LEVEL}, Version: ${VERSION}, API Key: ${API_KEY}`);