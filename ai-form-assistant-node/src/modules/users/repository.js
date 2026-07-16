const BaseRepository = require("../../common/repositories/baseRepository");
const User = require("./model");

class UserRepository extends BaseRepository {
    constructor() {
        super(User);
    }
}

module.exports = new UserRepository();