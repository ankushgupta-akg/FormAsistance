const app = require("./app");
const config = require("../core/config");
const logger = require("../core/logger");

app.listen(config.PORT, () => {
    logger.info(`Server running on ${config.PORT}`);
});