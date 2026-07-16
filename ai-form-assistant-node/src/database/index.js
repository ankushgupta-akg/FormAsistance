const sequelize = require("./sequelize");
const models = require("./registry");

module.exports = {
    sequelize,
    ...models,
};