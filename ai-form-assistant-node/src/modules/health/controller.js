const healthService = require("./service");

class HealthController {

    check(req, res) {
        res.json(healthService.check());
    }

}

module.exports = new HealthController();