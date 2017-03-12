import serve from 'koa-static';
import Koa from 'koa';

const app = new Koa();

app.use(serve('src/'));

app.listen(3030);

console.log('Listening on port 3030');
