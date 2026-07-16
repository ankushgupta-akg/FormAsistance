const config = require("../../../core/config");

class HealthService {

    check() {
        return {
            status: "healthy",
            service: config.APP_NAME
        };
    }

}

module.exports = new HealthService();