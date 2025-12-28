import http from 'http';
import 'dotenv/config';

const server = http.createServer( (req, res) => {
    if (req.url === '/api/time') {
        res.writeHead(200, {'Content-Type': 'application/json'});
        res.end(JSON.stringify( {time: new Date().toISOString()}));

    } else {

        res.writeHead(404, {'Content-Type': 'text/plain'});
        res.end('Not Found');
    }
})


const port = process.env.PORT
server.listen(8080, () => { console.log(`Server running on ${port} 
    `) })