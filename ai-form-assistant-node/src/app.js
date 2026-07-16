const express = require("express");
const config = require("../core/config");
const app = express();

const logger = require("../core/logger");

const healthRouter = require("./modules/health/routes");

app.use("/health", healthRouter);

module.exports = app;