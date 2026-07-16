const express = require("express");
const config = require("../core/config");
const app = express();

const logger = require("../core/logger");

const healthRouter = require("./modules/health/routes");
const usersRouter = require("./modules/users/routes");

app.use("/health", healthRouter);
app.use("/users", usersRouter);

module.exports = app;