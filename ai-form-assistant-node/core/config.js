require("dotenv").config();

const config = {
    APP_NAME: process.env.APP_NAME,
    APP_ENV: process.env.APP_ENV,
    PORT: Number(process.env.PORT),
    HOST: process.env.HOST,

    DEBUG: process.env.DEBUG === "true",

    JWT_SECRET: process.env.JWT_SECRET,

    DATABASE_URL: process.env.DATABASE_URL,

    OPENAI_API_KEY: process.env.OPENAI_API_KEY
};

module.exports = config;