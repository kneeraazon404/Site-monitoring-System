module.exports = ({ env }) => ({
  host: env('HOST', '0.0.0.0'),
  port: env.int('PORT', 1337),
  url:"https://d00ab38ba21a.ngrok.io",
  admin: {
    auth: {
      secret: env('ADMIN_JWT_SECRET', '8457be26b4303f44aa17670377feb547'),
    },
  },
});
