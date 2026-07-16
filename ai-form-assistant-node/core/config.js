require("dotenv").config();

const config = {
    APP_NAME: process.env.APP_NAME,
    APP_ENV: process.env.APP_ENV,
    PORT: Number(process.env.PORT),
    HOST: process.env.HOST,

    DEBUG: process.env.DEBUG === "true",

    JWT_SECRET: process.env.JWT_SECRET,

    DB_USER: process.env.DB_USER,
    DB_PASSWORD: process.env.DB_PASSWORD,
    DB_HOST: process.env.DB_HOST,
    DB_PORT: Number(process.env.DB_PORT) || 5432,
    DB_NAME: process.env.DB_NAME,

    OPENAI_API_KEY: process.env.OPENAI_API_KEY
};

module.exports = config;